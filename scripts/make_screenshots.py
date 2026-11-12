"""Write one PNG per lecture step of the Day 76 analysis."""

import argparse
import logging
import os
from pathlib import Path

from play_store.domain.rules import DEFAULT_DATA_PATH
from play_store.infrastructure.data import load_apps
from play_store.presentation.export import write_images

DEFAULT_OUT = Path("docs/images")
logger = logging.getLogger(__name__)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Read the command line."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--data",
        type=Path,
        default=Path(os.environ.get("PLAY_STORE_DATA", str(DEFAULT_DATA_PATH))),
        help="path to the course CSV (default: PLAY_STORE_DATA or data/apps.csv)",
    )
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """Load the data and export the images."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    args = parse_args(argv)
    paths = write_images(load_apps(args.data), args.out)
    logger.info("Wrote %d images to %s", len(paths), args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
