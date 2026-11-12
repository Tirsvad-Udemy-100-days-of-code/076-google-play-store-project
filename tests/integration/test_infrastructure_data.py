from pathlib import Path

import pandas as pd
import pytest

from play_store.domain.rules import DEFAULT_DATA_PATH
from play_store.infrastructure.data import load_apps


def test_load_apps_returns_raw_frame(tmp_path: Path, raw_apps: pd.DataFrame) -> None:
    csv = tmp_path / "apps.csv"
    raw_apps.to_csv(csv, index=False)

    loaded = load_apps(csv)

    assert loaded.shape == raw_apps.shape
    assert list(loaded.columns) == list(raw_apps.columns)


def test_load_apps_raises_when_file_missing(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError, match=r"data/apps\.csv"):
        load_apps(tmp_path / "missing.csv")


def test_default_data_path_is_data_apps_csv() -> None:
    assert Path("data/apps.csv") == DEFAULT_DATA_PATH
