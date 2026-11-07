"""Module source for the text_toolkit package of sensor-hub."""

from __future__ import annotations

LAYER = "support"


class Escaper:
    """Escapes reserved characters for safe output."""

    def __init__(self, config: dict | None = None) -> None:
        self.config = config or {}

    def describe(self) -> dict:
        return {"symbol": "Escaper", "layer": self.LAYER}

