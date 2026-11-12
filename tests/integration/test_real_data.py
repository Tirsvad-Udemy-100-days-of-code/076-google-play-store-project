"""Checks against the real course CSV; skipped when the file is not present."""

import os
from pathlib import Path

import pandas as pd
import pytest

from play_store.application.aggregations import count_genres, median_paid_price
from play_store.application.cleaning import (
    clean_apps,
    drop_missing_ratings,
    drop_unused_columns,
    remove_duplicates,
)
from play_store.application.exploration import top_grossing_paid_apps
from play_store.domain.rules import DEFAULT_DATA_PATH
from play_store.infrastructure.data import load_apps

DATA_PATH = Path(os.environ.get("PLAY_STORE_DATA", str(DEFAULT_DATA_PATH)))

pytestmark = pytest.mark.skipif(
    not DATA_PATH.is_file(), reason=f"course CSV not found at {DATA_PATH}"
)


@pytest.fixture(scope="module")
def raw() -> pd.DataFrame:
    return load_apps(DATA_PATH)


@pytest.fixture(scope="module")
def rated(raw: pd.DataFrame) -> pd.DataFrame:
    return drop_missing_ratings(drop_unused_columns(raw))


@pytest.fixture(scope="module")
def cleaned(raw: pd.DataFrame) -> pd.DataFrame:
    return clean_apps(raw)


def test_raw_shape_matches_course(raw: pd.DataFrame) -> None:
    assert raw.shape == (10841, 12)


def test_rows_after_dropping_missing_ratings(rated: pd.DataFrame) -> None:
    assert len(rated) == 9367


def test_rows_after_removing_duplicates(rated: pd.DataFrame) -> None:
    assert len(remove_duplicates(rated)) == 8199


def test_instagram_has_four_rows_before_and_one_after_dedup(
    rated: pd.DataFrame,
) -> None:
    before = (rated["App"] == "Instagram").sum()
    deduped = remove_duplicates(rated)
    after = (deduped["App"] == "Instagram").sum()

    assert (before, after) == (4, 1)


def test_rows_after_full_cleaning(cleaned: pd.DataFrame) -> None:
    assert len(cleaned) == 8184


def test_median_paid_price(cleaned: pd.DataFrame) -> None:
    assert median_paid_price(cleaned) == pytest.approx(2.99)


def test_category_and_genre_counts(cleaned: pd.DataFrame) -> None:
    assert cleaned["Category"].nunique() == 33
    assert len(count_genres(cleaned)) == 53


def test_minecraft_is_top_grossing_paid_app(cleaned: pd.DataFrame) -> None:
    first = top_grossing_paid_apps(cleaned).iloc[0]

    assert first["App"] == "Minecraft"
    assert first["Revenue_Estimate"] == pytest.approx(69_900_000)


def test_median_installs_free_versus_paid(cleaned: pd.DataFrame) -> None:
    medians = cleaned.groupby("Type")["Installs"].median()

    assert (medians["Free"], medians["Paid"]) == (500_000, 5_000)
