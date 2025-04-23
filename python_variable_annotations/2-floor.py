#!/usr/bin/env python3
"""Module pour les opérations mathématiques de base.

Ce module fournit des fonctions de base avec des annotations de type.
"""

import math


def floor(n: float) -> int:
    """Retourne l'arrondi inférieur (floor) d'un nombre flottant.
    Args:
        n: Nombre flottant à arrondir vers le bas
    Returns:
        L'entier résultant de l'arrondi vers le bas (floor)
    """
    return math.floor(n)
