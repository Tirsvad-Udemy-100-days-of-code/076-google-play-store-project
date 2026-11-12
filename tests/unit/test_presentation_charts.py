import pandas as pd
import plotly.express as px
from plotly.graph_objects import Figure

from play_store.presentation import charts


def test_content_rating_pie_has_outside_percent_and_label(
    store_apps: pd.DataFrame,
) -> None:
    fig = charts.content_rating_pie(store_apps)

    assert isinstance(fig, Figure)
    assert fig.layout.title.text == "Content Rating"
    assert list(fig.data[0].labels) == ["Everyone", "Teen"]
    assert list(fig.data[0].values) == [7, 2]
    assert fig.data[0].textposition == "outside"
    assert fig.data[0].textinfo == "percent+label"


def test_content_rating_donut_has_hole_and_inside_percent(
    store_apps: pd.DataFrame,
) -> None:
    fig = charts.content_rating_donut(store_apps)

    assert isinstance(fig, Figure)
    assert fig.data[0].hole == 0.6
    assert fig.data[0].textposition == "inside"
    assert fig.data[0].textfont.size == 15
    assert fig.data[0].textinfo == "percent"


def test_top10_categories_bar_is_vertical(store_apps: pd.DataFrame) -> None:
    fig = charts.top10_categories_bar(store_apps)

    assert isinstance(fig, Figure)
    assert fig.layout.title.text == "Top 10 Categories by Number of Apps"
    assert list(fig.data[0].x) == ["GAME", "FAMILY", "TOOLS"]
    assert list(fig.data[0].y) == [4, 3, 2]
    assert fig.data[0].orientation == "v"


def test_category_popularity_bar_is_horizontal(store_apps: pd.DataFrame) -> None:
    fig = charts.category_popularity_bar(store_apps)

    assert isinstance(fig, Figure)
    assert fig.data[0].orientation == "h"
    assert list(fig.data[0].y) == ["TOOLS", "FAMILY", "GAME"]
    assert fig.layout.title.text == "Category Popularity"
    assert fig.layout.xaxis.title.text == "Number of Downloads"
    assert fig.layout.yaxis.title.text == "Category"


def test_category_concentration_scatter_uses_log_installs(
    store_apps: pd.DataFrame,
) -> None:
    fig = charts.category_concentration_scatter(store_apps)

    assert isinstance(fig, Figure)
    assert fig.layout.title.text == "Category Concentration"
    assert set(fig.data[0].hovertext) == {"GAME", "FAMILY", "TOOLS"}
    assert list(fig.data[0].x) == [4, 3, 2] or set(fig.data[0].x) == {2, 3, 4}
    assert fig.layout.xaxis.title.text == "Number of Apps (Lower=More Concentrated)"
    assert fig.layout.yaxis.title.text == "Installs"
    assert fig.layout.yaxis.type == "log"
    assert fig.layout.coloraxis.colorbar.title.text == "Installs"
    assert fig.data[0].marker.size is not None


def test_top_genres_bar_uses_colour_scale_without_axis(
    store_apps: pd.DataFrame,
) -> None:
    fig = charts.top_genres_bar(store_apps)

    expected = [colour for _, colour in px.colors.get_colorscale("Agsunset")]
    actual = [colour for _, colour in fig.layout.coloraxis.colorscale]
    assert isinstance(fig, Figure)
    assert fig.layout.title.text == "Top Genres"
    assert fig.data[0].x[0] == "Action"
    assert fig.data[0].y[0] == 4
    assert fig.layout.coloraxis.showscale is False
    assert actual == expected
    assert fig.layout.xaxis.title.text == "Genre"
    assert fig.layout.yaxis.title.text == "Number of Apps"


def test_free_vs_paid_bar_is_grouped_and_ordered(store_apps: pd.DataFrame) -> None:
    fig = charts.free_vs_paid_bar(store_apps)

    assert isinstance(fig, Figure)
    assert fig.layout.title.text == "Free vs Paid Apps by Category"
    assert {trace.name for trace in fig.data} == {"Free", "Paid"}
    assert fig.layout.barmode == "group"
    assert fig.layout.xaxis.categoryorder == "total descending"
    assert fig.layout.yaxis.type == "log"
    assert fig.layout.xaxis.title.text == "Category"
    assert fig.layout.yaxis.title.text == "Number of Apps"


def test_installs_box_is_notched_with_all_points(store_apps: pd.DataFrame) -> None:
    fig = charts.installs_box(store_apps)

    assert isinstance(fig, Figure)
    assert fig.layout.title.text == "How Many Downloads are Paid Apps Giving Up?"
    assert {trace.name for trace in fig.data} == {"Free", "Paid"}
    assert all(trace.notched for trace in fig.data)
    assert all(trace.boxpoints == "all" for trace in fig.data)
    assert fig.layout.yaxis.type == "log"


def test_paid_revenue_box_shows_paid_apps_only(store_apps: pd.DataFrame) -> None:
    fig = charts.paid_revenue_box(store_apps)

    values = sorted(v for trace in fig.data for v in trace.y)
    assert isinstance(fig, Figure)
    assert fig.layout.title.text == "How Much Can Paid Apps Earn?"
    assert len(values) == 4
    assert values[0] == 100 * 2.99
    assert fig.layout.xaxis.title.text == "Category"
    assert fig.layout.yaxis.title.text == "Paid App Ballpark Revenue"
    assert fig.layout.xaxis.categoryorder == "min ascending"
    assert fig.layout.yaxis.type == "log"


def test_paid_price_box_shows_paid_prices(store_apps: pd.DataFrame) -> None:
    fig = charts.paid_price_box(store_apps)

    values = sorted(v for trace in fig.data for v in trace.y)
    assert isinstance(fig, Figure)
    assert fig.layout.title.text == "Price per Category"
    assert values == [0.99, 2.99, 2.99, 4.99]
    assert fig.layout.xaxis.title.text == "Category"
    assert fig.layout.yaxis.title.text == "Paid App Price"
    assert fig.layout.xaxis.categoryorder == "max descending"
    assert fig.layout.yaxis.type == "log"
