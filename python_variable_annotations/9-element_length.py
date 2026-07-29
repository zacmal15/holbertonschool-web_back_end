#!/usr/bin/env python3
"""This module provides a function that pairs sequences with their lengths."""

from typing import Iterable, List, Sequence, Tuple


def element_length(
        lst: Iterable[Sequence],
) -> List[Tuple[Sequence, int]]:
    """Return each sequence together with its length."""
    return [(i , len(i)) for i in lst]
