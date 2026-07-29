#!/usr/bin/env python3
"""This module provides a function that returns the sum of a mixed list."""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list containing integers and floats."""
    return float(sum(mxd_lst))
