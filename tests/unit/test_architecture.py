import ast
from pathlib import Path

import pytest

SOURCE = Path(__file__).resolve().parents[2] / "src" / "play_store"
FORBIDDEN = {
    "domain": ("application", "infrastructure", "presentation"),
    "application": ("infrastructure", "presentation"),
    "infrastructure": ("application", "presentation"),
}
FRAMEWORKS = ("pandas", "plotly")


def _imported_modules(path: Path) -> list[str]:
    modules: list[str] = []
    for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
        if isinstance(node, ast.Import):
            modules.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            modules.append(node.module)
    return modules


@pytest.mark.parametrize("layer", sorted(FORBIDDEN))
def test_inner_layer_imports_no_outer_layer(layer: str) -> None:
    offenders = [
        f"{path.name} imports {module}"
        for path in (SOURCE / layer).glob("*.py")
        for module in _imported_modules(path)
        for outer in FORBIDDEN[layer]
        if module.startswith(f"play_store.{outer}")
    ]

    assert offenders == []


def test_domain_imports_no_dataframe_or_chart_library() -> None:
    offenders = [
        f"{path.name} imports {module}"
        for path in (SOURCE / "domain").glob("*.py")
        for module in _imported_modules(path)
        if module.split(".")[0] in FRAMEWORKS
    ]

    assert offenders == []
