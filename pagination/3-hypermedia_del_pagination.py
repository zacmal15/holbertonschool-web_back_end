#!/usr/bin/env python3
"""Module for deletion-resilient hypermedia pagination."""

import csv
import math
from typing import Dict, List, Optional, Union


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize the server dataset caches."""
        self.__dataset: Optional[List[List[str]]] = None
        self.__indexed_dataset: Optional[Dict[int, List[str]]] = None

    def dataset(self) -> List[List[str]]:
        """Return the cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List[str]]:
        """Return the dataset indexed by its original sorting position."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }

        return self.__indexed_dataset

    def get_hyper_index(
            self, index: Optional[int] = None,
            page_size: int = 10) -> Dict[
                str, Union[int, List[List[str]]]]:
        """Return a deletion-resilient page with pagination metadata."""
        if index is None:
            index = 0

        assert isinstance(index, int)
        assert 0 <= index < len(self.dataset())
        assert isinstance(page_size, int) and page_size > 0

        indexed_data = self.indexed_dataset()
        data: List[List[str]] = []
        next_index: int = index

        while len(data) < page_size:
            if next_index in indexed_data:
                data.append(indexed_data[next_index])
            next_index += 1

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index,
        }
