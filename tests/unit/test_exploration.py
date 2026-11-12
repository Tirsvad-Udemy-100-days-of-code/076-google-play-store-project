import pandas as pd

from play_store.application.exploration import (
    highest_rated,
    largest_apps,
    most_reviewed,
    top_grossing_paid_apps,
)


def test_top_grossing_paid_apps_ranks_paid_by_revenue(
    numeric_apps: pd.DataFrame,
) -> None:
    df = numeric_apps.assign(Revenue_Estimate=[999_999, 2000, 2001, 50])

    result = top_grossing_paid_apps(df, n=2)

    assert list(result["App"]) == ["C", "B"]


def test_highest_rated_returns_n_sorted(numeric_apps: pd.DataFrame) -> None:
    result = highest_rated(numeric_apps, n=2)

    assert list(result["App"]) == ["B", "C"]


def test_largest_apps_sorts_by_size(numeric_apps: pd.DataFrame) -> None:
    result = largest_apps(numeric_apps, n=2)

    assert list(result["App"]) == ["D", "B"]


def test_most_reviewed_returns_all_when_fewer_than_n(
    numeric_apps: pd.DataFrame,
) -> None:
    result = most_reviewed(numeric_apps)

    assert list(result["App"]) == ["D", "B", "C", "A"]


def test_exploration_does_not_mutate_input(numeric_apps: pd.DataFrame) -> None:
    before = numeric_apps.copy(deep=True)

    highest_rated(numeric_apps)
    largest_apps(numeric_apps)
    most_reviewed(numeric_apps)

    pd.testing.assert_frame_equal(numeric_apps, before)
