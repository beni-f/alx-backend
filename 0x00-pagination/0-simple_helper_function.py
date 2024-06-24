#!/usr/bin/env python3
"""
    Simple helper function
"""
from typing import Tuple


def index_range(page, page_size) -> Tuple:
    return ((page - 1) * page_size, page * page_size)
