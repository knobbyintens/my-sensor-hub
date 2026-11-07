"""Module source for the text_toolkit package of sensor-hub."""

from __future__ import annotations

LAYER = "support"


class Padder:
    """Aligns text blocks with padding characters."""

    def __init__(self, config: dict | None = None) -> None:
        self.config = config or {}

    def describe(self) -> dict:
        return {"symbol": "Padder", "layer": self.LAYER}

