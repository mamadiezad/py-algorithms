"""Quick Sort — O(n log n) divide-and-conquer, in-place algorithm."""

from typing import List, TypeVar

T = TypeVar("T")


def quick_sort(arr: List[T], low: int = 0, high: int | None = None) -> List[T]:
    """
    Sort an array in-place using the quick sort algorithm.

    Args:
        arr: List of comparable elements.
        low: Starting index (default: 0).
        high: Ending index (default: len(arr) - 1).

    Returns:
        The sorted list (same reference as input).

    Examples:
        >>> quick_sort([3, 1, 4, 1, 5, 9, 2, 6])
        [1, 1, 2, 3, 4, 5, 6, 9]
        >>> quick_sort([])
        []
    """
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_idx = _partition(arr, low, high)
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)

    return arr


def _partition(arr: List[T], low: int, high: int) -> int:
    """Partition array around pivot and return pivot index."""
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
