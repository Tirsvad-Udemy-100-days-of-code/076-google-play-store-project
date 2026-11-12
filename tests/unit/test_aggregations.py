import pandas as pd

from play_store.application.aggregations import (
    category_concentration,
    category_installs,
    content_rating_counts,
    count_genres,
    free_vs_paid_by_category,
    median_paid_price,
    paid_apps,
    top_categories,
)


def test_content_rating_counts_counts_each_rating(store_apps: pd.DataFrame) -> None:
    result = content_rating_counts(store_apps)

    assert result.to_dict() == {"Everyone": 7, "Teen": 2}


def test_top_categories_limits_to_n(store_apps: pd.DataFrame) -> None:
    result = top_categories(store_apps, n=2)

    assert list(result.index) == ["GAME", "FAMILY"]
    assert list(result.values) == [4, 3]


def test_top_categories_defaults_to_ten(store_apps: pd.DataFrame) -> None:
    assert len(top_categories(store_apps)) == 3


def test_category_installs_sorts_ascending(store_apps: pd.DataFrame) -> None:
    result = category_installs(store_apps)

    assert list(result.index) == ["TOOLS", "FAMILY", "GAME"]
    assert result["GAME"] == 1_000_000 + 500_000 + 1_000 + 5_000
    assert result.is_monotonic_increasing


def test_category_concentration_merges_apps_and_installs(
    store_apps: pd.DataFrame,
) -> None:
    result = category_concentration(store_apps)

    assert list(result.columns) == ["App", "Installs"]
    assert result.loc["GAME", "App"] == 4
    assert result.loc["TOOLS", "Installs"] == 20_000


def test_count_genres_counts_each_genre_of_multi_genre_apps(
    store_apps: pd.DataFrame,
) -> None:
    result = count_genres(store_apps)

    assert result["Action"] == 4
    assert result["Adventure"] == 1
    assert result["Art & Design"] == 1
    assert result["Pretend Play"] == 1


def test_free_vs_paid_by_category_counts_per_type(store_apps: pd.DataFrame) -> None:
    result = free_vs_paid_by_category(store_apps)

    assert list(result.columns) == ["Category", "Type", "App"]
    game_paid = result[(result["Category"] == "GAME") & (result["Type"] == "Paid")]
    assert game_paid["App"].iloc[0] == 2
    assert len(result) == 6


def test_paid_apps_keeps_only_paid(store_apps: pd.DataFrame) -> None:
    result = paid_apps(store_apps)

    assert set(result["Type"]) == {"Paid"}
    assert len(result) == 4


def test_median_paid_price_is_the_median_of_paid_prices(
    store_apps: pd.DataFrame,
) -> None:
    assert median_paid_price(store_apps) == 2.99
