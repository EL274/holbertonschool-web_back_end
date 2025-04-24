#!/usr/bin/env python3
"""Module pour la conversion d'une valeur en tuple
Ce module fournit la fonction pour convertir une valeur en tuple
"""
from typing import Union, tuple


def to_kv(k:str, v: Union[int, float]) -> tuple[str, float]:
    """Crée un tuple contenant une clé et la valeur au carré
    Args:
        k: la clé sous forme de chaine de caractères
        v: la valeur sous forme d'entier ou de flottant à mettre au carré
        returns:
            Un tuple contenant:
                la chaine original k
                le carré de v sous forme flottante
    """
    return (k, float(v ** 2))
