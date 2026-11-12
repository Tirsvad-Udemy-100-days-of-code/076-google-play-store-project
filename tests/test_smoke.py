"""Smoke test: the package imports."""

import play_store


def test_package_has_version() -> None:
    assert play_store.__version__ == "0.1.0"
