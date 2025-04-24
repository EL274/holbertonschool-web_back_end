#!/usr/bin/env python3
"""Module pour les opérations sur les listes numériques.

Ce module fournit des fonctions pour effectuer des calculs sur des listes de nombres.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Calcule la somme d'une liste de nombres flottants.
    
    Args:
        input_list: Liste de nombres flottants à sommer
    
    Returns:
        La somme des éléments de la liste sous forme de float
    """
    return sum(input_list)
