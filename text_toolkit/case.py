"""Module source for the text_toolkit package of sensor-hub."""

from __future__ import annotations

LAYER = "support"


class CaseConverter:
    """Converts identifiers between naming conventions."""

    def __init__(self, config: dict | None = None) -> None:
        self.config = config or {}

    def describe(self) -> dict:
        return {"symbol": "CaseConverter", "layer": self.LAYER}

