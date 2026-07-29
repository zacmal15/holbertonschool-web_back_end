#!/usr/bin/env python3
"""This module provides a function that creates multiplier functions."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by the multiplier"""

    def multiply(number: float) -> float:
        """Multiply a float by multiplier."""
        return number * multiplier

    return multiply
