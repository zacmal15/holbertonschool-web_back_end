#!/usr/bin/env python3
"""This module provides a function that reutns a k-v pair."""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple containing a string and square of a number."""
    return (k, float(v ** 2))
