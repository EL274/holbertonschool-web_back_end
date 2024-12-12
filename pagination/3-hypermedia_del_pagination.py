#!/usr/bin/env python3

import math
from typing import List, Tuple, Dict

# Fonction index_range


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)

# Classe Pagination


class Pagination:
    def __init__(self, dataset: List, page: int, page_size: int):
        self.dataset = dataset
        self.page = page
        self.page_size = page_size

    def get_page(self) -> List:
        start_index, end_index = index_range(self.page, self.page_size)
        return self.dataset[start_index:end_index]

    def get_hyper(self) -> Dict:
        data = self.get_page()
        total_items = len(self.dataset)
        total_pages = math.ceil(total_items / self.page_size)
        next_page = self.page + 1 if self.page < total_pages else None
        prev_page = self.page - 1 if self.page > 1 else None

        return {
            'page_size': len(data),
            'page': self.page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
