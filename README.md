# Py-Algorithms — Python Algorithms & Data Structures 🧮

> **Python** implementations of classic **algorithms** and **data structures** — perfect for **coding interviews**, **competitive programming**, and **CS fundamentals**.

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://python.org)
[![Tests](https://img.shields.io/badge/Tests-Passing-success?logo=pytest)](https://docs.pytest.org)
[![Coverage](https://img.shields.io/badge/Coverage-95%25-brightgreen)](https://coverage.readthedocs.io)
[![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE)

---

## 📚 What's Inside?

This repository contains clean, well-documented Python implementations of essential **data structures** and **algorithms** that every developer should know. Each algorithm includes **time/space complexity analysis**, **type hints**, and **unit tests**.

---

## 📑 Contents

### 🔄 Sorting Algorithms
| Algorithm | Average Time | Worst Time | Space | Stable |
|-----------|:-----------:|:----------:|:-----:|:-----:|
| **Bubble Sort** | O(n²) | O(n²) | O(1) | ✅ |
| **Selection Sort** | O(n²) | O(n²) | O(1) | ❌ |
| **Insertion Sort** | O(n²) | O(n²) | O(1) | ✅ |
| **Merge Sort** | O(n log n) | O(n log n) | O(n) | ✅ |
| **Quick Sort** | O(n log n) | O(n²) | O(log n) | ❌ |
| **Heap Sort** | O(n log n) | O(n log n) | O(1) | ❌ |
| **Counting Sort** | O(n + k) | O(n + k) | O(k) | ✅ |

### 🔍 Searching Algorithms
- **Linear Search** — O(n)
- **Binary Search** — O(log n) — Iterative & Recursive
- **Jump Search** — O(√n)
- **Exponential Search** — O(log n)
- **Ternary Search** — O(log₃ n)

### 🏗️ Data Structures
- **Singly Linked List** — Complete CRUD + Reverse
- **Doubly Linked List** — Bidirectional traversal
- **Stack** — LIFO with array & linked list
- **Queue** — FIFO with array & linked list
- **Binary Search Tree (BST)** — Insert, delete, search, traversal
- **AVL Tree** — Self-balancing BST
- **Heap** — Min & Max heap implementations
- **Hash Table** — Custom hash map with collision handling

### 🌐 Graph Algorithms
- **BFS** — Breadth-first search for shortest path
- **DFS** — Depth-first search
- **Dijkstra's Algorithm** — Shortest path (weighted)
- **Bellman-Ford** — Negative weight handling
- **Kruskal's MST** — Minimum spanning tree
- **Prim's MST** — Minimum spanning tree (greedy)
- **Topological Sort** — DAG ordering

### 🧠 Dynamic Programming
- **Fibonacci** — Memoization & tabulation
- **0/1 Knapsack** — Classic DP problem
- **Fractional Knapsack** — Greedy approach
- **Longest Common Subsequence** — String matching
- **Longest Increasing Subsequence** — Array optimization
- **Edit Distance** — Levenshtein distance
- **Matrix Chain Multiplication** — Optimal parenthesization

---

## 🚀 Usage

```python
from algorithms.sorting import merge_sort
from algorithms.searching import binary_search

# Sort an array
arr = [3, 7, 1, 9, 4, 2, 8, 5, 6]
sorted_arr = merge_sort(arr)
print(f"Sorted: {sorted_arr}")

# Search in sorted array
index = binary_search(sorted_arr, 7)
print(f"Found at index: {index}")
```

---

## 🧪 Testing

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest

# Verbose mode
pytest -v

# With coverage
pytest --cov=algorithms --cov-report=term-missing

# Run specific test
pytest tests/test_sorting.py -v
```

---

## 📊 Benchmarks

```bash
python -m benchmarks.sorting_benchmark
```

---

## 🎯 Why This Repo?

- ✅ **Interview Prep** — Everything you need for FAANG interviews
- ✅ **Clean Code** — PEP 8 compliant, type hints everywhere
- ✅ **Well Tested** — 95%+ test coverage
- ✅ **Educational** — Docstrings with examples for every function
- ✅ **Production Quality** — Ready to use in real projects

---

## 🔗 Related Projects

- [FastAPI Tasks](https://github.com/mamadiezad/fastapi-tasks) — Task management API
- [TS Design Patterns](https://github.com/mamadiezad/ts-design-patterns) — Design patterns in TypeScript

---

## 📄 License

**MIT** — Free to use for learning, interviews, and production.

---

<p align="center">
  <sub>Built with ❤️ by <a href="https://github.com/mamadiezad">Mohammad</a></sub>
</p>
<p align="center">ساخته شده با ❤️ توسط <a href="https://github.com/mamadiezad">Mohammad</a> | <a href="https://t.me/llllxyz">📱 تلگرام</a></p>