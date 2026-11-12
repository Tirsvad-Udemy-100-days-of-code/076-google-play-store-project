"""Pure cleaning steps for the Google Play Store data, in lecture order."""

import pandas as pd

from play_store.domain.rules import DUPLICATE_KEY, PRICE_LIMIT, UNUSED_COLUMNS


def drop_unused_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy without the Last_Updated and Android_Ver columns."""
    return df.drop(columns=UNUSED_COLUMNS)


def drop_missing_ratings(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy without rows that have a missing value."""
    return df.dropna()


def find_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Return every row that shares App, Type and Price with another row."""
    return df[df.duplicated(subset=DUPLICATE_KEY, keep=False)]


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Keep, per App, Type and Price, the row with the most reviews."""
    most_reviews_first = df.sort_values("Reviews", ascending=False)
    unique = most_reviews_first.drop_duplicates(subset=DUPLICATE_KEY, keep="first")
    return unique.sort_index()


def convert_installs(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy with Installs as numbers (commas and '+' removed)."""
    cleaned = (
        df["Installs"].astype(str).str.replace(r"[,+]", "", regex=True).str.strip()
    )
    return df.assign(Installs=pd.to_numeric(cleaned))


def convert_price(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy with Price as numbers (dollar sign removed)."""
    cleaned = df["Price"].astype(str).str.replace("$", "", regex=False).str.strip()
    return df.assign(Price=pd.to_numeric(cleaned))


def remove_expensive_apps(df: pd.DataFrame, limit: float = PRICE_LIMIT) -> pd.DataFrame:
    """Keep apps priced below the limit; this removes the "I am Rich" apps."""
    return df[df["Price"] < limit]


def add_revenue_estimate(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy with Revenue_Estimate = Installs * Price."""
    return df.assign(Revenue_Estimate=df["Installs"] * df["Price"])


def clean_apps(df: pd.DataFrame) -> pd.DataFrame:
    """Run all cleaning steps in lecture order on the raw data frame."""
    steps = (
        drop_unused_columns,
        drop_missing_ratings,
        remove_duplicates,
        convert_installs,
        convert_price,
        remove_expensive_apps,
        add_revenue_estimate,
    )
    result = df
    for step in steps:
        result = step(result)
    return result
