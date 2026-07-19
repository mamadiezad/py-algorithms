"""Tests for Dijkstra's algorithm."""

from algorithms.graph.dijkstra import dijkstra, get_shortest_path


def test_simple_graph():
    graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("C", 1), ("D", 5)],
        "C": [("D", 8), ("E", 10)],
        "D": [("E", 2)],
        "E": [],
    }
    dist, pred = dijkstra(graph, "A")
    assert dist["A"] == 0
    assert dist["B"] == 4
    assert dist["C"] == 2
    assert dist["D"] == 8  # A->C->B->D = 2+1+5
    assert dist["E"] == 10  # A->C->B->D->E = 2+1+5+2

    path = get_shortest_path(pred, "E")
    assert path == ["A", "C", "B", "D", "E"]


def test_disconnected():
    graph = {"A": [("B", 1)], "B": [], "C": []}
    dist, _ = dijkstra(graph, "A")
    assert dist["A"] == 0
    assert dist["B"] == 1
    assert dist["C"] == float("inf")


def test_single_node():
    graph = {"A": []}
    dist, _ = dijkstra(graph, "A")
    assert dist["A"] == 0
