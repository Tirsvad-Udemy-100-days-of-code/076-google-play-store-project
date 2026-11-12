"""Pure exploration queries on the cleaned Google Play Store data."""

import pandas as pd

from play_store.domain.rules import (
    HIGHEST_RATED_COUNT,
    LARGEST_APPS_COUNT,
    MOST_REVIEWED_COUNT,
    TOP_GROSSING_COUNT,
)


def top_grossing_paid_apps(
    df: pd.DataFrame, n: int = TOP_GROSSING_COUNT
) -> pd.DataFrame:
    """Return the n paid apps with the highest Revenue_Estimate."""
    paid = df[df["Type"] == "Paid"]
    return paid.sort_values("Revenue_Estimate", ascending=False).head(n)


def highest_rated(df: pd.DataFrame, n: int = HIGHEST_RATED_COUNT) -> pd.DataFrame:
    """Return the n apps with the highest Rating."""
    return df.sort_values("Rating", ascending=False).head(n)


def largest_apps(df: pd.DataFrame, n: int = LARGEST_APPS_COUNT) -> pd.DataFrame:
    """Return the n apps with the largest Size_MBs."""
    return df.sort_values("Size_MBs", ascending=False).head(n)


def most_reviewed(df: pd.DataFrame, n: int = MOST_REVIEWED_COUNT) -> pd.DataFrame:
    """Return the n apps with the most Reviews."""
    return df.sort_values("Reviews", ascending=False).head(n)
