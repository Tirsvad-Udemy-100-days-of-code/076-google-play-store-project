"""Integration test: the course notebook runs from top to bottom."""

import os
from pathlib import Path

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[2]
NOTEBOOK = ROOT / "notebooks" / "google_play_store.ipynb"
TIMEOUT_SECONDS = 180
MIN_CODE_CELLS = 20


def test_notebook_executes_without_error(
    tmp_path: Path,
    course_like_apps: pd.DataFrame,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Run an in-memory copy of the notebook; the repo file is not changed."""
    nbformat = pytest.importorskip("nbformat", reason="nbformat is not installed")
    nbclient = pytest.importorskip("nbclient", reason="nbclient is not installed")
    pytest.importorskip("ipykernel", reason="ipykernel is not installed")
    csv = tmp_path / "apps.csv"
    course_like_apps.to_csv(csv, index=False)
    monkeypatch.setenv("PLAY_STORE_DATA", str(csv))
    monkeypatch.setenv(
        "PYTHONPATH", str(ROOT / "src") + os.pathsep + os.environ.get("PYTHONPATH", "")
    )

    notebook = nbformat.read(NOTEBOOK, as_version=4)
    nbclient.NotebookClient(
        notebook,
        timeout=TIMEOUT_SECONDS,
        kernel_name="python3",
        resources={"metadata": {"path": str(ROOT)}},
    ).execute()

    code_cells = [c for c in notebook.cells if c.cell_type == "code"]
    assert len(code_cells) >= MIN_CODE_CELLS


def test_committed_notebook_has_no_outputs() -> None:
    import json

    cells = json.loads(NOTEBOOK.read_text(encoding="utf-8"))["cells"]

    assert all(not c.get("outputs") for c in cells if c["cell_type"] == "code")
