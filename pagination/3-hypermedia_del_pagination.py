#!/usr/bin/env python3
"""Module for deletion-resilient hypermedia pagination."""

import csv
import math
from typing import List, Dict, Union


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the server dataset caches."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Return the cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Return the dataset indexed by its original sorting position."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }

        return self.__indexed_dataset

    def get_hyper_index(
            self, index: int = None, page_size: int = 10) -> Dict:
        """Return a deletion-resilient page with pagination metadata."""
        dataset = self.indexed_dataset()

        assert index is None or index >= 0
        assert index < len(dataset)

        if index is None:
            index = 0

        data = []
        i = index

        while len(data) < page_size and i < len(dataset):
            if i in dataset:
                data.append(dataset[i])
            i = i + 1

        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': i
        }
