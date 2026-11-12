import pandas as pd
import pytest

from play_store.application.cleaning import clean_apps

COLUMNS = [
    "App",
    "Category",
    "Rating",
    "Reviews",
    "Size_MBs",
    "Type",
    "Price",
    "Content_Rating",
    "Genres",
    "Last_Updated",
    "Android_Ver",
    "Installs",
]


def _row(
    app: str,
    rating: float,
    reviews: int,
    size: float,
    kind: str,
    price: str,
    installs: str,
) -> list[object]:
    return [
        app,
        "TEST",
        rating,
        reviews,
        size,
        kind,
        price,
        "Everyone",
        "Test",
        "January 1, 2018",
        "4.0 and up",
        installs,
    ]


@pytest.fixture
def raw_apps() -> pd.DataFrame:
    """Raw synthetic apps: NaN rating, 3 Instagram copies, an "I am Rich" app."""
    rows = [
        _row("Instagram", 4.5, 1000, 12.0, "Free", "0", "1,000,000+"),
        _row("Instagram", 4.5, 5000, 12.0, "Free", "0", "5,000,000+"),
        _row("Instagram", 4.5, 3000, 12.0, "Free", "0", "3,000,000+"),
        _row("Minecraft", 4.6, 500, 90.0, "Paid", "$6.99", "10,000"),
        _row("I am Rich", 3.8, 40, 1.5, "Paid", "$399.99", "10"),
        _row("Nova", 4.1, 70, 5.0, "Paid", "$4.99", "1,000+"),
        _row("Calculator", 4.9, 20, 2.0, "Free", "0", "500"),
        _row("Unrated", float("nan"), 3, 1.0, "Free", "0", "100"),
    ]
    return pd.DataFrame(rows, columns=COLUMNS)


@pytest.fixture
def numeric_apps() -> pd.DataFrame:
    """Synthetic apps after Installs and Price became numbers."""
    rows = [
        _row("A", 4.0, 10, 1.0, "Free", "0", "100"),
        _row("B", 4.8, 300, 50.0, "Paid", "2", "1000"),
        _row("C", 4.2, 200, 9.0, "Paid", "5", "400"),
        _row("D", 3.0, 900, 70.0, "Paid", "1", "50"),
    ]
    df = pd.DataFrame(rows, columns=COLUMNS)
    df["Price"] = pd.to_numeric(df["Price"]).astype(float)
    df["Installs"] = pd.to_numeric(df["Installs"])
    return df


def _store_row(
    app: str,
    category: str,
    kind: str,
    price: str,
    installs: str,
    content_rating: str,
    genres: str,
    reviews: int,
) -> list[object]:
    return [
        app,
        category,
        4.0,
        reviews,
        10.0,
        kind,
        price,
        content_rating,
        genres,
        "January 1, 2018",
        "4.0 and up",
        installs,
    ]


@pytest.fixture
def store_apps() -> pd.DataFrame:
    """Cleaned synthetic apps: 3 categories, 2 ratings, free and paid, multi-genre."""
    free, paid = ("Free", "0"), "Paid"
    rows = [
        _store_row("A1", "GAME", *free, "1,000,000+", "Everyone", "Action", 1),
        _store_row("A2", "GAME", *free, "500,000+", "Teen", "Action;Adventure", 2),
        _store_row(
            "A3",
            "FAMILY",
            *free,
            "100,000+",
            "Everyone",
            "Art & Design;Pretend Play",
            3,
        ),
        _store_row("A4", "FAMILY", *free, "50,000+", "Everyone", "Education", 4),
        _store_row("A5", "TOOLS", *free, "10,000+", "Everyone", "Tools", 5),
        _store_row("P1", "GAME", paid, "$2.99", "1,000+", "Teen", "Action", 6),
        _store_row("P2", "GAME", paid, "$4.99", "5,000+", "Everyone", "Action", 7),
        _store_row("P3", "FAMILY", paid, "$2.99", "100+", "Everyone", "Education", 8),
        _store_row("P4", "TOOLS", paid, "$0.99", "10,000+", "Everyone", "Tools", 9),
    ]
    return clean_apps(pd.DataFrame(rows, columns=COLUMNS))
