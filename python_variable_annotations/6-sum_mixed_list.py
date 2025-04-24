#!/usr/bin/env python3
"""Module pour les opérations mixées sur les listes numériques

Ce module fournit les fonctions pour  calculer la somme d'une liste
de nombres qui peuvent contenir des entiers et des flottants.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Calcul la somme d'une liste contenant intiers et des flottants

    Args:
       mxd_lst: Liste contenant des entiers et/ou des flottants 

    Returns:
        La somme de tous les éléments dans la liste comme un flottant
    """
    return float(sum(mxd_lst))
