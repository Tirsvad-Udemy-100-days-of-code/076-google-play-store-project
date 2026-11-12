"""One image per lecture step: table figures for exploration, charts otherwise."""

from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
from plotly.graph_objects import Figure

from play_store.application.cleaning import (
    clean_apps,
    convert_installs,
    convert_price,
    drop_missing_ratings,
    drop_unused_columns,
    remove_duplicates,
    remove_expensive_apps,
)
from play_store.application.exploration import (
    highest_rated,
    largest_apps,
    most_reviewed,
    top_grossing_paid_apps,
)
from play_store.presentation import charts

SAMPLE_SIZE = 5
SAMPLE_SEED = 1
MOST_REVIEWED_SHOWN = 10
DEFAULT_WIDTH = 1200
DEFAULT_HEIGHT = 700

FigureBuilder = Callable[[pd.DataFrame], Figure]


@dataclass(frozen=True, slots=True)
class LectureStep:
    """One lecture step and the builder of its figure from the raw data."""

    slug: str
    title: str
    builder: FigureBuilder


def table_figure(df: pd.DataFrame, title: str) -> Figure:
    """Render a data frame as a Plotly table figure."""
    shown = df.reset_index(drop=True)
    fig = go.Figure(
        go.Table(
            header={"values": [str(column) for column in shown.columns]},
            cells={"values": [shown[column].astype(str) for column in shown.columns]},
        )
    )
    fig.update_layout(title=title)
    return fig


def _explore_table(raw: pd.DataFrame) -> Figure:
    rows, columns = raw.shape
    title = f"Raw data: {rows} rows, {columns} columns"
    return table_figure(raw.sample(SAMPLE_SIZE, random_state=SAMPLE_SEED), title)


def _cleaning_table(raw: pd.DataFrame) -> Figure:
    unused_dropped = drop_unused_columns(raw)
    rated = drop_missing_ratings(unused_dropped)
    unique = remove_duplicates(rated)
    affordable = remove_expensive_apps(convert_price(convert_installs(unique)))
    stages = [
        ("Raw data", raw),
        ("Drop unused columns", unused_dropped),
        ("Drop NaN ratings", rated),
        ("Remove duplicates", unique),
        ("Remove expensive apps", affordable),
    ]
    counts = pd.DataFrame(
        {
            "Stage": [name for name, _ in stages],
            "Rows": [len(frame) for _, frame in stages],
            "Columns": [frame.shape[1] for _, frame in stages],
        }
    )
    return table_figure(counts, "Rows after each cleaning stage")


def _top_table(
    pick: Callable[[pd.DataFrame], pd.DataFrame], title: str, columns: list[str]
) -> FigureBuilder:
    def build(raw: pd.DataFrame) -> Figure:
        return table_figure(pick(clean_apps(raw))[columns], title)

    return build


def _chart(builder: FigureBuilder) -> FigureBuilder:
    def build(raw: pd.DataFrame) -> Figure:
        return builder(clean_apps(raw))

    return build


def _most_reviewed_top(df: pd.DataFrame) -> pd.DataFrame:
    return most_reviewed(df, MOST_REVIEWED_SHOWN)


LECTURE_STEPS: tuple[LectureStep, ...] = (
    LectureStep("step-1-explore", "Explore the raw data", _explore_table),
    LectureStep("step-2-clean", "Clean the data", _cleaning_table),
    LectureStep(
        "step-3-highest-rated",
        "Highest rated apps",
        _top_table(
            highest_rated,
            "Top 5 highest rated apps",
            ["App", "Category", "Rating", "Reviews"],
        ),
    ),
    LectureStep(
        "step-4-largest-apps",
        "Largest apps",
        _top_table(
            largest_apps,
            "Top 5 largest apps",
            ["App", "Category", "Size_MBs", "Rating"],
        ),
    ),
    LectureStep(
        "step-5-most-reviewed",
        "Most reviewed apps",
        _top_table(
            _most_reviewed_top,
            "Top 10 most reviewed apps",
            ["App", "Category", "Reviews", "Type"],
        ),
    ),
    LectureStep(
        "step-6-content-rating-pie",
        "Content rating pie chart",
        _chart(charts.content_rating_pie),
    ),
    LectureStep(
        "step-7-content-rating-donut",
        "Content rating donut chart",
        _chart(charts.content_rating_donut),
    ),
    LectureStep(
        "step-8-top-categories-bar",
        "Top 10 categories",
        _chart(charts.top10_categories_bar),
    ),
    LectureStep(
        "step-9-category-popularity-bar",
        "Category popularity",
        _chart(charts.category_popularity_bar),
    ),
    LectureStep(
        "step-10-category-concentration-scatter",
        "Category concentration",
        _chart(charts.category_concentration_scatter),
    ),
    LectureStep("step-11-top-genres-bar", "Top genres", _chart(charts.top_genres_bar)),
    LectureStep(
        "step-12-free-vs-paid-bar",
        "Free vs paid apps",
        _chart(charts.free_vs_paid_bar),
    ),
    LectureStep(
        "step-13-installs-box",
        "Installs of free and paid apps",
        _chart(charts.installs_box),
    ),
    LectureStep(
        "step-14-top-grossing",
        "Top grossing paid apps",
        _top_table(
            top_grossing_paid_apps,
            "Top 10 paid apps by estimated revenue",
            ["App", "Category", "Price", "Installs", "Revenue_Estimate"],
        ),
    ),
    LectureStep(
        "step-15-paid-revenue-box",
        "Paid app revenue",
        _chart(charts.paid_revenue_box),
    ),
    LectureStep(
        "step-16-paid-price-box", "Paid app price", _chart(charts.paid_price_box)
    ),
)


def write_images(
    raw_df: pd.DataFrame,
    out_dir: Path,
    width: int = DEFAULT_WIDTH,
    height: int = DEFAULT_HEIGHT,
) -> list[Path]:
    """Write one PNG per lecture step to out_dir and return the paths.

    Raises RuntimeError when the optional kaleido package is not installed.
    """
    try:
        import kaleido  # noqa: F401  # optional "docs" extra used by write_image
    except ImportError as error:
        msg = "PNG export needs kaleido; install it with: pip install '.[docs]'"
        raise RuntimeError(msg) from error
    out_dir.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []
    for step in LECTURE_STEPS:
        path = out_dir / f"{step.slug}.png"
        step.builder(raw_df).write_image(path, width=width, height=height)
        paths.append(path)
    return paths
