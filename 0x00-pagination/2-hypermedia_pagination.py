#!/usr/bin/env python3
"""
    Hypermedia pagination
"""
from typing import List, Tuple
import csv
import math


def index_range(page, page_size) -> Tuple:
    """
        return a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list for those
        particular pagination parameters
    """
    return ((page - 1) * page_size, page * page_size)


class Server:
    """
        Server class to paginate a database of popular baby names.
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
            Implements a pagination on a csv file
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)

        dataset = self.dataset()

        if int(start) >= len(dataset):
            return []

        return dataset[start: end]

    def get_hyper(self, page=1, page_size=10):
        """
            Hypermedia pagination
        """
        start, end = index_range(page, page_size)
        data = self.get_page(page, page_size)
        total_rows = len(self.dataset())
        total_pages = math.ceil(total_rows / page_size)

        result = {
            'page_size': page_size if page_size * page < total_rows else 0,
            'page': page,
            'data': data,
            'next_page': page + 1 if total_rows >= page_size * page else None,
            'prev_page': page - 1 if not (page - 1 <= 0) else None,
            'total_pages': total_pages
        }
        return result
