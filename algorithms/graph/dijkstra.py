"""Dijkstra's shortest path algorithm — O((V + E) log V)."""

from typing import Dict, Tuple, List
import heapq


def dijkstra(
    graph: Dict[str, List[Tuple[str, int]]], start: str
) -> Tuple[Dict[str, int], Dict[str, str | None]]:
    """
    Find shortest paths from start node to all other nodes.

    Args:
        graph: Adjacency list {node: [(neighbor, weight), ...]}.
        start: Source node.

    Returns:
        (distances, predecessors) dictionaries.

    Examples:
        >>> graph = {
        ...     'A': [('B', 4), ('C', 2)],
        ...     'B': [('C', 1), ('D', 5)],
        ...     'C': [('D', 8), ('E', 10)],
        ...     'D': [('E', 2)],
        ...     'E': []
        ... }
        >>> dist, _ = dijkstra(graph, 'A')
        >>> dist['A']
        0
        >>> dist['B']
        4
        >>> dist['D']  # A->C->B->D = 2+1+5 = 8
        8
    """
    distances: Dict[str, int] = {node: float("inf") for node in graph}  # type: ignore
    predecessors: Dict[str, str | None] = {node: None for node in graph}
    distances[start] = 0

    # Priority queue: (distance, node)
    pq = [(0, start)]

    while pq:
        current_dist, current = heapq.heappop(pq)

        if current_dist > distances[current]:
            continue

        for neighbor, weight in graph.get(current, []):
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current
                heapq.heappush(pq, (distance, neighbor))

    return distances, predecessors


def get_shortest_path(predecessors: Dict[str, str | None], target: str) -> List[str]:
    """Reconstruct shortest path from predecessors dict."""
    path = []
    current: str | None = target
    while current is not None:
        path.append(current)
        current = predecessors.get(current)
    return path[::-1]
