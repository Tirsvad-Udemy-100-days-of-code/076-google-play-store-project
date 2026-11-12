import sys
from pathlib import Path

import pandas as pd
import pytest
from plotly.graph_objects import Figure

from play_store.presentation.export import (
    LECTURE_STEPS,
    LectureStep,
    table_figure,
    write_images,
)

EXPECTED_STEP_COUNT = 16


def test_lecture_steps_cover_sixteen_steps_in_order() -> None:
    numbers = [int(step.slug.split("-")[1]) for step in LECTURE_STEPS]

    assert numbers == list(range(1, EXPECTED_STEP_COUNT + 1))


def test_lecture_step_slugs_are_unique() -> None:
    slugs = [step.slug for step in LECTURE_STEPS]

    assert len(set(slugs)) == len(slugs)


@pytest.mark.parametrize("step", LECTURE_STEPS, ids=lambda step: step.slug)
def test_builder_returns_figure(
    step: LectureStep, course_like_apps: pd.DataFrame
) -> None:
    assert isinstance(step.builder(course_like_apps), Figure)


def test_cleaning_table_counts_rows_after_each_stage(
    course_like_apps: pd.DataFrame,
) -> None:
    step = next(s for s in LECTURE_STEPS if s.slug == "step-2-clean")

    rows = step.builder(course_like_apps).data[0].cells.values[1]

    assert list(rows) == ["11", "11", "10", "9", "8"]


def test_table_figure_has_header_per_column() -> None:
    fig = table_figure(pd.DataFrame({"a": [1], "b": [2]}), "title")

    assert list(fig.data[0].header.values) == ["a", "b"]


def test_write_images_without_kaleido_raises_clear_error(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path, course_like_apps: pd.DataFrame
) -> None:
    monkeypatch.setitem(sys.modules, "kaleido", None)

    with pytest.raises(RuntimeError, match="kaleido"):
        write_images(course_like_apps, tmp_path)
