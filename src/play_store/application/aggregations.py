"""Pure data preparation for the charts; no chart library is used here."""

import pandas as pd

from play_store.domain.rules import GENRE_SEPARATOR, PAID_TYPE, TOP_CATEGORY_COUNT


def content_rating_counts(df: pd.DataFrame) -> pd.Series:
    """Count the apps per content rating."""
    return df["Content_Rating"].value_counts()


def top_categories(df: pd.DataFrame, n: int = TOP_CATEGORY_COUNT) -> pd.Series:
    """Count the apps of the n categories with the most apps."""
    return df["Category"].value_counts()[:n]


def category_installs(df: pd.DataFrame) -> pd.Series:
    """Sum the installs per category, fewest first."""
    return df.groupby("Category")["Installs"].sum().sort_values(ascending=True)


def category_concentration(df: pd.DataFrame) -> pd.DataFrame:
    """Return the number of apps and the installs per category (index)."""
    app_counts = df.groupby("Category")["App"].count().to_frame()
    installs = category_installs(df).to_frame()
    return pd.merge(app_counts, installs, left_index=True, right_index=True)


def count_genres(df: pd.DataFrame) -> pd.Series:
    """Count the apps per genre; an app with several genres counts in each."""
    split = df["Genres"].str.split(GENRE_SEPARATOR, expand=True)
    return split.stack().value_counts()


def free_vs_paid_by_category(df: pd.DataFrame) -> pd.DataFrame:
    """Count the apps per category and type (Free or Paid)."""
    return df.groupby(["Category", "Type"], as_index=False).agg({"App": "count"})


def paid_apps(df: pd.DataFrame) -> pd.DataFrame:
    """Keep the paid apps."""
    return df[df["Type"] == PAID_TYPE]


def median_paid_price(df: pd.DataFrame) -> float:
    """Return the median price of the paid apps."""
    return float(paid_apps(df)["Price"].median())
