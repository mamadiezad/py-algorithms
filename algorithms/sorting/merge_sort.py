"""Merge Sort — O(n log n) divide-and-conquer algorithm."""

from typing import List, TypeVar

T = TypeVar("T")


def merge_sort(arr: List[T]) -> List[T]:
    """
    Sort an array using the merge sort algorithm.

    Args:
        arr: List of comparable elements.

    Returns:
        A new sorted list.

    Examples:
        >>> merge_sort([3, 1, 4, 1, 5, 9, 2, 6])
        [1, 1, 2, 3, 4, 5, 6, 9]
        >>> merge_sort([])
        []
        >>> merge_sort([1])
        [1]
    """
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return _merge(left, right)


def _merge(left: List[T], right: List[T]) -> List[T]:
    """Merge two sorted lists into one sorted list."""
    result: List[T] = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
