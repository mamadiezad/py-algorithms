"""0/1 Knapsack problem — O(n * W) dynamic programming."""

from typing import List, Tuple


def knapsack_01(weights: List[int], values: List[int], capacity: int) -> Tuple[int, List[int]]:
    """
    Solve 0/1 knapsack problem using dynamic programming.

    Args:
        weights: List of item weights.
        values: List of item values.
        capacity: Maximum weight capacity.

    Returns:
        (max_value, selected_indices) tuple.

    Examples:
        >>> knapsack_01([2, 3, 4, 5], [3, 4, 5, 6], 5)
        (7, [0, 1])
        >>> knapsack_01([1, 2, 3], [6, 10, 12], 5)
        (22, [1, 2])
    """
    n = len(weights)
    # DP table: dp[i][w] = max value using first i items with weight <= w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find selected items
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)
            w -= weights[i - 1]

    return dp[n][capacity], selected[::-1]


def knapsack_fractional(weights: List[int], values: List[int], capacity: int) -> float:
    """
    Solve fractional knapsack using greedy approach.

    Examples:
        >>> knapsack_fractional([2, 3, 5], [50, 60, 100], 8)
        170.0
    """
    items = [(values[i] / weights[i], weights[i], values[i]) for i in range(len(weights))]
    items.sort(reverse=True, key=lambda x: x[0])

    total_value = 0.0
    remaining = capacity

    for ratio, weight, value in items:
        if weight <= remaining:
            total_value += value
            remaining -= weight
        else:
            total_value += ratio * remaining
            break

    return total_value
