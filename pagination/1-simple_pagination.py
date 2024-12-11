#!/usr/bin/env python3


def index_range(page, page_size):
    start_index =(page - 1) * page_size
    end_index = start_index + page_size 
    return (start_index, end_index)

class Pagination:
    def __init__(self, page, page_size):
        self.page = page 
        self.page_size = page_size

    def get_index_range(self):
        return index_range(self.page, self.page_size)
