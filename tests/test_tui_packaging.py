from pathlib import Path

import tomllib


def test_pyproject_exposes_arcs_tui_console_script():
    data = tomllib.loads(Path("pyproject.toml").read_text())

    assert data["project"]["scripts"]["arcs-tui"] == "companion_safety_eval.tui:app"


def test_pyproject_declares_tui_optional_dependency():
    data = tomllib.loads(Path("pyproject.toml").read_text())

    assert any(dep.startswith("textual") for dep in data["project"]["optional-dependencies"]["tui"])
