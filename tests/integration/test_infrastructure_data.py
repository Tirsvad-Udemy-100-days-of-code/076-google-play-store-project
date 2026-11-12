import re
from pathlib import Path

import pandas as pd
import pytest

from play_store.domain.rules import DEFAULT_DATA_PATH
from play_store.infrastructure import data
from play_store.infrastructure.data import load_apps

REAL_ROOT = Path(__file__).resolve().parents[2]


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


def _use_fake_root(
    monkeypatch: pytest.MonkeyPatch, root: Path, raw_apps: pd.DataFrame
) -> None:
    (root / "data").mkdir(parents=True)
    raw_apps.to_csv(root / "data" / "apps.csv", index=False)
    (root / "notebooks").mkdir()
    monkeypatch.setattr(data, "_project_root", lambda: root)
    monkeypatch.chdir(root / "notebooks")


def test_load_apps_finds_relative_path_at_project_root(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, raw_apps: pd.DataFrame
) -> None:
    _use_fake_root(monkeypatch, tmp_path, raw_apps)

    loaded = load_apps(DEFAULT_DATA_PATH)

    assert loaded.shape == raw_apps.shape


def test_load_apps_prefers_file_in_current_directory(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, raw_apps: pd.DataFrame
) -> None:
    _use_fake_root(monkeypatch, tmp_path, raw_apps)
    local = tmp_path / "notebooks" / "data"
    local.mkdir()
    raw_apps.head(2).to_csv(local / "apps.csv", index=False)

    assert len(load_apps(DEFAULT_DATA_PATH)) == 2


def test_load_apps_error_names_the_paths_tried(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(data, "_project_root", lambda: tmp_path)
    monkeypatch.chdir(tmp_path)

    with pytest.raises(FileNotFoundError, match=re.escape(str(tmp_path / "data"))):
        load_apps(DEFAULT_DATA_PATH)


def test_load_apps_without_project_root_uses_path_as_given(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(data, "_project_root", lambda: None)
    monkeypatch.chdir(tmp_path)

    with pytest.raises(FileNotFoundError, match="tried: data"):
        load_apps(DEFAULT_DATA_PATH)


def test_project_root_holds_pyproject() -> None:
    root = data._project_root()

    assert root is not None
    assert (root / "pyproject.toml").is_file()


@pytest.mark.skipif(
    not (REAL_ROOT / DEFAULT_DATA_PATH).is_file(), reason="data/apps.csv is absent"
)
def test_default_path_loads_from_another_directory(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.chdir(tmp_path)

    assert not load_apps().empty
