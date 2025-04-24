#!/usr/bin/env python3
"""Module pour créer un multiplicateur
Ce module fournit la fonction pour créer un multiplicateur
"""
from typing import Callable


def make_multiplier (multiplier: float) -> Callable[[float], float]:
    """Crée une fonction qui multiplie un nombre par un multiplicateur
     Args:
        multiplier: le mutiplicateur
        Returns:
            Une fonction qui multiplie un nombre par le multiplicateur
            """
    def multiplier_function (x: float) -> float:
        return x * multiplier
    return multiplier_function
