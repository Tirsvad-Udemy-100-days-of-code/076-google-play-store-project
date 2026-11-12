"""Plotly figure builders for the six market questions."""

import pandas as pd
import plotly.express as px
from plotly.graph_objects import Figure

from play_store.application.aggregations import (
    category_concentration,
    category_installs,
    content_rating_counts,
    count_genres,
    free_vs_paid_by_category,
    paid_apps,
    top_categories,
)
from play_store.domain.rules import COLOUR_SCALE, DONUT_HOLE, TOP_GENRE_COUNT


def content_rating_pie(df: pd.DataFrame) -> Figure:
    """Pie chart of the apps per content rating."""
    ratings = content_rating_counts(df)
    fig = px.pie(values=ratings.values, names=ratings.index, title="Content Rating")
    fig.update_traces(textposition="outside", textinfo="percent+label")
    return fig


def content_rating_donut(df: pd.DataFrame) -> Figure:
    """Donut chart of the apps per content rating."""
    ratings = content_rating_counts(df)
    fig = px.pie(
        values=ratings.values,
        names=ratings.index,
        title="Content Rating",
        hole=DONUT_HOLE,
    )
    fig.update_traces(textposition="inside", textfont_size=15, textinfo="percent")
    return fig


def top10_categories_bar(df: pd.DataFrame) -> Figure:
    """Vertical bar chart of the categories with the most apps."""
    categories = top_categories(df)
    return px.bar(
        x=categories.index,
        y=categories.values,
        title="Top 10 Categories by Number of Apps",
    )


def category_popularity_bar(df: pd.DataFrame) -> Figure:
    """Horizontal bar chart of the installs per category."""
    installs = category_installs(df)
    fig = px.bar(
        x=installs.values,
        y=installs.index,
        orientation="h",
        title="Category Popularity",
    )
    fig.update_layout(xaxis_title="Number of Downloads", yaxis_title="Category")
    return fig


def category_concentration_scatter(df: pd.DataFrame) -> Figure:
    """Scatter plot of apps against installs per category."""
    concentration = category_concentration(df)
    fig = px.scatter(
        concentration,
        x="App",
        y="Installs",
        title="Category Concentration",
        size="App",
        hover_name=concentration.index,
        color="Installs",
    )
    fig.update_layout(
        xaxis_title="Number of Apps (Lower=More Concentrated)",
        yaxis_title="Installs",
        yaxis={"type": "log"},
    )
    return fig


def top_genres_bar(df: pd.DataFrame) -> Figure:
    """Bar chart of the genres with the most apps."""
    genres = count_genres(df)[:TOP_GENRE_COUNT]
    fig = px.bar(
        x=genres.index,
        y=genres.values,
        hover_name=genres.index,
        color=genres.values,
        color_continuous_scale=COLOUR_SCALE,
        title="Top Genres",
    )
    fig.update_layout(
        xaxis_title="Genre",
        yaxis_title="Number of Apps",
        coloraxis_showscale=False,
    )
    return fig


def free_vs_paid_bar(df: pd.DataFrame) -> Figure:
    """Grouped bar chart of free and paid apps per category."""
    fig = px.bar(
        free_vs_paid_by_category(df),
        x="Category",
        y="App",
        title="Free vs Paid Apps by Category",
        color="Type",
        barmode="group",
    )
    fig.update_layout(
        xaxis={"categoryorder": "total descending"},
        yaxis={"type": "log"},
        xaxis_title="Category",
        yaxis_title="Number of Apps",
    )
    return fig


def installs_box(df: pd.DataFrame) -> Figure:
    """Box plot of the installs of free and paid apps."""
    fig = px.box(
        df,
        y="Installs",
        x="Type",
        color="Type",
        notched=True,
        points="all",
        title="How Many Downloads are Paid Apps Giving Up?",
    )
    fig.update_layout(yaxis={"type": "log"})
    return fig


def paid_revenue_box(df: pd.DataFrame) -> Figure:
    """Box plot of the estimated revenue of paid apps per category."""
    fig = px.box(
        paid_apps(df),
        x="Category",
        y="Revenue_Estimate",
        title="How Much Can Paid Apps Earn?",
    )
    fig.update_layout(
        xaxis_title="Category",
        yaxis_title="Paid App Ballpark Revenue",
        xaxis={"categoryorder": "min ascending"},
        yaxis={"type": "log"},
    )
    return fig


def paid_price_box(df: pd.DataFrame) -> Figure:
    """Box plot of the price of paid apps per category."""
    fig = px.box(
        paid_apps(df),
        x="Category",
        y="Price",
        title="Price per Category",
    )
    fig.update_layout(
        xaxis_title="Category",
        yaxis_title="Paid App Price",
        xaxis={"categoryorder": "max descending"},
        yaxis={"type": "log"},
    )
    return fig
