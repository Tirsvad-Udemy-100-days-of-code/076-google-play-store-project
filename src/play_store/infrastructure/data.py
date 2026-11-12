"""Loading of the Google Play Store data set."""

from pathlib import Path

import pandas as pd

from play_store.domain.rules import DEFAULT_DATA_PATH

PROJECT_MARKER = "pyproject.toml"


def _project_root() -> Path | None:
    """Return the folder holding pyproject.toml above this file, if any."""
    for parent in Path(__file__).resolve().parents:
        if (parent / PROJECT_MARKER).is_file():
            return parent
    return None


def _candidates(path: Path) -> list[Path]:
    """List where to look: the path itself, then below the project root."""
    if path.is_absolute():
        return [path]
    root = _project_root()
    return [path] if root is None else [path, root / path]


def load_apps(path: Path | str = DEFAULT_DATA_PATH) -> pd.DataFrame:
    """Read the course CSV into a raw data frame.

    A relative path is tried from the current directory, then from the project
    root, so a notebook started in notebooks/ finds data/apps.csv.
    Raises FileNotFoundError, telling where to place the file, when it is missing.
    """
    candidates = _candidates(Path(path))
    for candidate in candidates:
        if candidate.is_file():
            return pd.read_csv(candidate)
    tried = ", ".join(str(candidate) for candidate in candidates)
    msg = (
        f"Data file not found (tried: {tried}). Place the course CSV at data/apps.csv."
    )
    raise FileNotFoundError(msg)
