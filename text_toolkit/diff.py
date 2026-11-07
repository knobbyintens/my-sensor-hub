"""Module source for the text_toolkit package of sensor-hub."""

from __future__ import annotations

LAYER = "support"


class LineDiffer:
    """Computes line-level differences between documents."""

    def __init__(self, config: dict | None = None) -> None:
        self.config = config or {}

    def describe(self) -> dict:
        return {"symbol": "LineDiffer", "layer": self.LAYER}

