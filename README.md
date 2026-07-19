# Py-Algorithms 🧮

A comprehensive collection of classic **algorithms** and **data structures** implemented in **Python** with clean code, type hints, tests, and benchmarks.

## 📚 Contents

### Sorting Algorithms
| Algorithm | Time (Avg) | Time (Worst) | Space |
|-----------|-----------|--------------|-------|
| Bubble Sort | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n²) | O(log n) |
| Heap Sort | O(n log n) | O(n log n) | O(1) |
| Counting Sort | O(n + k) | O(n + k) | O(k) |

### Searching Algorithms
- Linear Search
- Binary Search
- Jump Search
- Exponential Search
- Ternary Search

### Data Structures
- Linked List (Singly & Doubly)
- Stack & Queue
- Binary Search Tree
- AVL Tree
- Heap (Min & Max)
- Hash Table
- Graph (Adjacency List)

### Graph Algorithms
- BFS & DFS
- Dijkstra's Shortest Path
- Bellman-Ford
- Kruskal's MST
- Prim's MST
- Topological Sort

### Dynamic Programming
- Fibonacci Series
- Knapsack (0/1 & Fractional)
- Longest Common Subsequence
- Longest Increasing Subsequence
- Edit Distance
- Matrix Chain Multiplication

## 🚀 Usage

```python
from algorithms.sorting.merge_sort import merge_sort
from algorithms.searching.binary_search import binary_search

arr = [3, 7, 1, 9, 4, 2, 8, 5, 6]
sorted_arr = merge_sort(arr)
print(f"Sorted: {sorted_arr}")

idx = binary_search(sorted_arr, 7)
print(f"Found 7 at index: {idx}")
```

## 🧪 Testing

```bash
# Run all tests
pytest

# With coverage
pytest --cov=algorithms --cov-report=term-missing

# Run specific test
pytest tests/test_sorting.py -v
```

## 📊 Benchmarks

```bash
python -m benchmarks.sorting_benchmark
```

## 📄 License

MIT
