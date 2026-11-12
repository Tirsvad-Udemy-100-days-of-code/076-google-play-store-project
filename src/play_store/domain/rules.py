"""Constants the cleaning and exploration rules share."""

from pathlib import Path

DEFAULT_DATA_PATH = Path("data/apps.csv")
UNUSED_COLUMNS = ["Last_Updated", "Android_Ver"]
DUPLICATE_KEY = ["App", "Type", "Price"]
PRICE_LIMIT = 250
TOP_GROSSING_COUNT = 10
HIGHEST_RATED_COUNT = 5
LARGEST_APPS_COUNT = 5
MOST_REVIEWED_COUNT = 50
