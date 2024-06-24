#!/usr/bin/env python3
"""
    Hypermedia pagination
"""
from typing import List, Tuple
import csv

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
        result = {
            'page_size': page_size,
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': page + 1 if page + 1 <= 3000 else None,
            'prev_page': page - 1 if not (page - 1 <= 0) else None,
            'total_pages': len(self.dataset())
        }
        return result


server = Server()

print(server.get_hyper(1, 2))
print("---")
print(server.get_hyper(2, 2))
print("---")
print(server.get_hyper(100, 3))
print("---")
print(server.get_hyper(3000, 100))