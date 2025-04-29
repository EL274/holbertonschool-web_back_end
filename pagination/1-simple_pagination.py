#!/usr/bin/env python3
""" Simple pagination """
import csv
import math
from typing import List, Tuple


class Server:
    """Classe de serveur pour paginer une base de données
    de noms de bébé populaires.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Ensemble de données mises en cache
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            Obtenir la page

            Args:
                page: page actuelle
                page_size: Taille de la page

            Return:
                Liste des paginations effectuées
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        range: Tuple = index_range(page, page_size)
        pagination: List = self.dataset()

        return (pagination[range[0]:range[1]])


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
