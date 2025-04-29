#!/usr/bin/env python3
""" Hypermedia pagination """
import csv
from math import ceil
from typing import List, Tuple, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
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
                page_size: taille totale de la page

            Return:
                Liste des paginations effectuées
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        range: Tuple = index_range(page, page_size)
        pagination: List = self.dataset()

        return (pagination[range[0]:range[1]])

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
            Portée de la page

            Args:
                page: Page actuelle
                page_size: Taille totale de la page

            Return:
                Dictionnaires avec différents arguments
                page_size: la longueur de la page du jeu de données renvoyé
                page: le numéro de la page actuelle
                data: la page du jeu de données
                (equivalent to return from previous task)
                next_page: numéro de la page suivante,aucun s'il n'ya pas
                prev_page: numéro de la page précédente,
                Aucun s'il n'y a pas de page précédente
                total_pages: le nombre total de pages
                dans l'ensemble de données sous forme d'entier
        """

        data = []
        try:
            data = self.get_page(page, page_size)
        except AssertionError:
            return {}

        dataset: List = self.dataset()
        totalpag: int = len(dataset) if dataset else 0
        totalpag = ceil(totalpag / page_size)
        prevpag: int = (page - 1) if (page - 1) >= 1 else None
        nextpag: int = (page + 1) if (page + 1) <= totalpag else None

        hypermedia: Dict = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': nextpag,
            'prev_page': prevpag,
            'total_pages': totalpag,
        }

        return hypermedia


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Portée de la page
    Args:
        page: Page actuelle
        page_size: Taille totale de la page
    Return:
        tuple avec la plage de taille de début et de fin de page
    """

    final_size: int = page * page_size
    start_size: int = final_size - page_size

    return (start_size, final_size)
