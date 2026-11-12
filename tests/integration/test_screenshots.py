import importlib.util
import subprocess
import sys
from pathlib import Path

import pandas as pd
import pytest

from play_store.presentation.export import LECTURE_STEPS, write_images

ROOT = Path(__file__).resolve().parents[2]
PNG_SIGNATURE = b"\x89PNG"

pytestmark = pytest.mark.skipif(
    importlib.util.find_spec("kaleido") is None, reason="kaleido is not installed"
)


def test_write_images_writes_one_png_per_step(
    tmp_path: Path, course_like_apps: pd.DataFrame
) -> None:
    paths = write_images(course_like_apps, tmp_path / "images", width=600, height=400)

    assert [p.name for p in paths] == [f"{s.slug}.png" for s in LECTURE_STEPS]
    assert all(p.read_bytes().startswith(PNG_SIGNATURE) for p in paths)


def test_make_screenshots_script_writes_images(
    tmp_path: Path, course_like_apps: pd.DataFrame
) -> None:
    csv = tmp_path / "apps.csv"
    course_like_apps.to_csv(csv, index=False)
    out = tmp_path / "out"

    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "make_screenshots.py"),
            "--data",
            str(csv),
            "--out",
            str(out),
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert len(list(out.glob("*.png"))) == len(LECTURE_STEPS)
