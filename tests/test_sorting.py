"""Tests for sorting algorithms."""

import pytest
from algorithms.sorting.merge_sort import merge_sort
from algorithms.sorting.quick_sort import quick_sort


class TestMergeSort:
    def test_empty(self):
        assert merge_sort([]) == []

    def test_single(self):
        assert merge_sort([1]) == [1]

    def test_sorted(self):
        assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reversed(self):
        assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_duplicates(self):
        assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]

    def test_strings(self):
        assert merge_sort(["banana", "apple", "cherry"]) == ["apple", "banana", "cherry"]


class TestQuickSort:
    def test_empty(self):
        assert quick_sort([]) == []

    def test_single(self):
        assert quick_sort([1]) == [1]

    def test_sorted(self):
        assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_reversed(self):
        assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_duplicates(self):
        assert quick_sort([3, 1, 4, 1, 5, 9]) == [1, 1, 3, 4, 5, 9]
