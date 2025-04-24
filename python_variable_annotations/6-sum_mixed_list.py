#!/usr/bin/env python3
"""Module for operations on mixed numeric lists.

This module provides functions for performing calculations on lists containing
both integers and floating-point numbers.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Calculates the sum of a list containing integers and floats.

    Args:
        mxd_lst: List containing integers and/or floating-point numbers

    Returns:
        The sum of all elements in the list as a floating-point number
    """
    return float(sum(mxd_lst))
