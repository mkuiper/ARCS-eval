from __future__ import annotations

from pathlib import Path
from typing import Iterable

import yaml

from .schemas import Scenario


def load_scenario(path: str | Path) -> Scenario:
    scenario_path = Path(path)
    with scenario_path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return Scenario.model_validate(data)


def load_scenarios(path: str | Path) -> list[Scenario]:
    directory = Path(path)
    scenario_paths: Iterable[Path]
    if directory.is_file():
        scenario_paths = [directory]
    else:
        scenario_paths = sorted(directory.glob("*.yaml")) + sorted(directory.glob("*.yml"))
    return [load_scenario(p) for p in scenario_paths]
