from collections.abc import Callable

import pandas as pd
import pytest

from play_store.application.cleaning import (
    add_revenue_estimate,
    clean_apps,
    convert_installs,
    convert_price,
    drop_missing_ratings,
    drop_unused_columns,
    find_duplicates,
    remove_duplicates,
    remove_expensive_apps,
)


def test_drop_unused_columns_removes_two_columns(raw_apps: pd.DataFrame) -> None:
    result = drop_unused_columns(raw_apps)

    assert "Last_Updated" not in result.columns
    assert "Android_Ver" not in result.columns
    assert result.shape[1] == raw_apps.shape[1] - 2


def test_drop_missing_ratings_removes_nan_rows(raw_apps: pd.DataFrame) -> None:
    result = drop_missing_ratings(raw_apps)

    assert len(result) == len(raw_apps) - 1
    assert "Unrated" not in set(result["App"])


def test_find_duplicates_returns_all_instagram_copies(raw_apps: pd.DataFrame) -> None:
    result = find_duplicates(raw_apps)

    assert list(result["App"]) == ["Instagram"] * 3


def test_remove_duplicates_keeps_most_reviewed(raw_apps: pd.DataFrame) -> None:
    result = remove_duplicates(raw_apps)

    instagram = result[result["App"] == "Instagram"]
    assert len(instagram) == 1
    assert instagram["Reviews"].iloc[0] == 5000
    assert len(result) == len(raw_apps) - 2


def test_remove_duplicates_keeps_same_name_with_other_price() -> None:
    df = pd.DataFrame(
        {
            "App": ["X", "X"],
            "Type": ["Free", "Free"],
            "Price": ["0", "1"],
            "Reviews": [1, 2],
        }
    )

    assert len(remove_duplicates(df)) == 2


def test_convert_installs_strips_commas_and_plus(raw_apps: pd.DataFrame) -> None:
    result = convert_installs(raw_apps)

    assert pd.api.types.is_numeric_dtype(result["Installs"])
    assert result["Installs"].iloc[0] == 1_000_000
    assert result["Installs"].iloc[3] == 10_000
    assert result["Installs"].iloc[5] == 1_000


def test_convert_price_strips_dollar_sign(raw_apps: pd.DataFrame) -> None:
    result = convert_price(raw_apps)

    assert pd.api.types.is_numeric_dtype(result["Price"])
    assert result["Price"].iloc[0] == 0
    assert result["Price"].iloc[3] == pytest.approx(6.99)


def test_remove_expensive_apps_drops_i_am_rich(numeric_apps: pd.DataFrame) -> None:
    df = numeric_apps.copy()
    df.loc[0, "Price"] = 399.99

    result = remove_expensive_apps(df)

    assert len(result) == len(df) - 1
    assert (result["Price"] < 250).all()


def test_remove_expensive_apps_limit_is_exclusive(
    numeric_apps: pd.DataFrame,
) -> None:
    result = remove_expensive_apps(numeric_apps, limit=5)

    assert set(result["App"]) == {"A", "B", "D"}


def test_add_revenue_estimate_multiplies_installs_and_price(
    numeric_apps: pd.DataFrame,
) -> None:
    result = add_revenue_estimate(numeric_apps)

    assert list(result["Revenue_Estimate"]) == [0, 2000, 2000, 50]


def test_clean_apps_pipeline_final_shape(raw_apps: pd.DataFrame) -> None:
    result = clean_apps(raw_apps)

    assert len(result) == 4
    assert set(result["App"]) == {"Instagram", "Minecraft", "Nova", "Calculator"}
    assert "Revenue_Estimate" in result.columns
    assert "Last_Updated" not in result.columns
    minecraft = result[result["App"] == "Minecraft"]
    assert minecraft["Revenue_Estimate"].iloc[0] == pytest.approx(69_900)


@pytest.mark.parametrize(
    "step",
    [
        drop_unused_columns,
        drop_missing_ratings,
        find_duplicates,
        remove_duplicates,
        convert_installs,
        convert_price,
        clean_apps,
    ],
)
def test_steps_do_not_mutate_input(
    raw_apps: pd.DataFrame, step: Callable[[pd.DataFrame], pd.DataFrame]
) -> None:
    before = raw_apps.copy(deep=True)

    step(raw_apps)

    pd.testing.assert_frame_equal(raw_apps, before)


def test_numeric_steps_do_not_mutate_input(numeric_apps: pd.DataFrame) -> None:
    before = numeric_apps.copy(deep=True)

    remove_expensive_apps(numeric_apps)
    add_revenue_estimate(numeric_apps)

    pd.testing.assert_frame_equal(numeric_apps, before)
