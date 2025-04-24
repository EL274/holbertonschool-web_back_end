#!/usr/bin/env python3
"""Module pour annoter une fonction.

Ce module fournit la fonction pour annoter une fonction.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Renvoie une liste de tuples contenant la longueur de chaque élément.
    
    Args:
        lst: Une liste de séquences
        
    Returns:
        Une liste de tuples contenant chaque séquence et sa longueur
    """
    return [(i, len(i)) for i in lst]
