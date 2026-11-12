"""Loading of the Google Play Store data set."""

from pathlib import Path

import pandas as pd

from play_store.domain.rules import DEFAULT_DATA_PATH


def load_apps(path: Path | str = DEFAULT_DATA_PATH) -> pd.DataFrame:
    """Read the course CSV into a raw data frame.

    Raises FileNotFoundError, telling where to place the file, when it is missing.
    """
    csv_path = Path(path)
    if not csv_path.is_file():
        msg = f"Data file not found: {csv_path}. Place the course CSV at data/apps.csv."
        raise FileNotFoundError(msg)
    return pd.read_csv(csv_path)
