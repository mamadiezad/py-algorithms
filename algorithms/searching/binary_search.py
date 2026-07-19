"""Binary Search — O(log n) on sorted arrays."""

from typing import List, TypeVar

T = TypeVar("T")


def binary_search(arr: List[T], target: T) -> int:
    """
    Find the index of target in a sorted array using binary search.

    Args:
        arr: Sorted list of elements.
        target: Element to search for.

    Returns:
        Index of target if found, otherwise -1.

    Examples:
        >>> binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)
        4
        >>> binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
        -1
        >>> binary_search([], 1)
        -1
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search_recursive(arr: List[T], target: T, left: int = 0, right: int | None = None) -> int:
    """Recursive binary search."""
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
