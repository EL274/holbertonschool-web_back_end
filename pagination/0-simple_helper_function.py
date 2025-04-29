#!/usr/bin/env python3
"""Gamme simple aide amusante"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        Portée de la page

        Args:
            page: Page actuelle
            page_size: Taille totale de la page

        Return:
           tuple avec la plage de taille de début et de fin
           de page
    """

    final_size: int = page * page_size
    start_size: int = final_size - page_size

    return (start_size, final_size)
