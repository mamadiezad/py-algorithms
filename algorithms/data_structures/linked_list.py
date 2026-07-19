"""Singly Linked List implementation."""

from __future__ import annotations
from typing import Any, Optional, Generator


class ListNode:
    """Node in a singly linked list."""

    def __init__(self, value: Any):
        self.value = value
        self.next: Optional[ListNode] = None


class LinkedList:
    """Singly linked list with common operations."""

    def __init__(self):
        self.head: Optional[ListNode] = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Generator[Any, None, None]:
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __repr__(self) -> str:
        return "[" + " -> ".join(str(v) for v in self) + "]"

    def is_empty(self) -> bool:
        """Check if list is empty."""
        return self.head is None

    def append(self, value: Any) -> None:
        """Add value to the end of the list. O(n)"""
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1

    def prepend(self, value: Any) -> None:
        """Add value to the beginning of the list. O(1)"""
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def insert(self, index: int, value: Any) -> None:
        """Insert value at given index. O(n)"""
        if index < 0 or index > self._size:
            raise IndexError("Index out of range")

        if index == 0:
            self.prepend(value)
            return

        new_node = ListNode(value)
        current = self.head
        for _ in range(index - 1):
            current = current.next  # type: ignore
        new_node.next = current.next  # type: ignore
        current.next = new_node  # type: ignore
        self._size += 1

    def delete(self, value: Any) -> bool:
        """Delete first occurrence of value. Returns True if found."""
        if not self.head:
            return False

        if self.head.value == value:
            self.head = self.head.next
            self._size -= 1
            return True

        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next
        return False

    def search(self, value: Any) -> Optional[int]:
        """Search for value, return index or None."""
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return None

    def reverse(self) -> None:
        """Reverse the linked list in-place. O(n)"""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def to_list(self) -> list:
        """Convert linked list to Python list."""
        return list(self)
