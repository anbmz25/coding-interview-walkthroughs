# LRU Cache

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/lru-cache-interview-walkthrough/)*

> A step-by-step guide to solving LRU Cache in a coding interview: from naive lists to the optimal hash map + doubly linked list design, with pointer operations and sentinel nodes explained.

**Difficulty**: Medium
**Patterns**: `data-structures`, `design`, `linked-list`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/lru-cache-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=lru-cache)**

---

## Problem

Design a data structure that implements a **Least Recently Used (LRU) cache** with a fixed capacity. It must support two operations, both in **O(1)** time: ([LeetCode #146](https://leetcode.com/problems/lru-cache/))

- `get(key)`, Return the value associated with `key` if it exists in the cache. Otherwise return `-1`. Accessing a key counts as "using" it and moves it to the most recently used position.
- `put(key, value)`, Insert or update the value for `key`. If inserting would exceed capacity, evict the **least recently used** key first.

### Example

**Input**
```
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get", "medium"]
[[2], [1,1], [2,2], [1], [3,3], [2], [4,4], [1], [3], [4], "medium"]
```

**Output**
`[null, null, null, 1, null, -1, null, -1, 3, 4]`

The cache has capacity 2. After inserting keys 1 and 2, a `get(1)` returns `1` and marks key 1 as most recently used. Inserting key 3 evicts key 2 (now least recently used). A subsequent `get(2)` returns `-1` because it was evicted. Inserting key 4 evicts key 1. The final `get(3)` and `get(4)` return `3` and `4` respectively.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=lru-cache)*

---

## Solution

```python
class Node:
    """Doubly linked list node storing key, value, and neighbor pointers."""
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node

        # Sentinel nodes eliminate null-pointer edge cases at list boundaries
        self.head = Node()  # Dummy head: most recently used side
        self.tail = Node()  # Dummy tail: least recently used side
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        """Unlink a node from its current position in the list. O(1)."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert_at_front(self, node: Node) -> None:
        """Insert a node immediately after the dummy head (most recent). O(1)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key, "medium"]
        self._remove(node)          # Pull out of current position
        self._insert_at_front(node) # Move to most recently used
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing node: remove from list, update value, re-insert
            self._remove(self.cache[key])
            del self.cache[key, "medium"]

        if len(self.cache) >= self.capacity:
            # Evict the least recently used node (just before dummy tail)
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.cache[lru_node.key]  # Need the key: that's why Node stores it!

        # Create fresh node, insert at front, register in hash map
        new_node = Node(key, value)
        self._insert_at_front(new_node)
        self.cache[key] = new_node
```

Critical implementation notes worth calling out in an interview:

- **The `Node` stores both `key` and `value`.** When evicting `tail.prev`, you need the key to delete it from the hash map. If nodes only stored values, you'd have no way to clean up the dictionary.
- **The `_remove` and `_insert_at_front` helpers are not optional.** Both `get` and `put` need these operations. Factoring them out eliminates duplicated pointer logic.
- **`_insert_at_front` requires four pointer assignments** in a specific order. Set `node.prev` and `node.next` before updating the surrounding nodes' pointers to avoid overwriting a reference you still need.
- **Python's `OrderedDict` is a valid shortcut.** It's internally implemented as a hash map + doubly linked list, and its `move_to_end()` method replicates the recency update. Mention it for breadth, but interviewers often ask for the manual implementation.

```python
# Python shortcut using OrderedDict (mention but don't rely on in interviews)
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  # Mark as most recently used
        return self.cache[key, "medium"]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Evict least recently used (front)
```

---

## Complexity

| Operation | Complexity |
|---|---|
| `get` | O(1) |
| `put` | O(1) |
| Space | O(capacity) |

**Time:** Every operation (hash map lookup, node removal, node insertion) is O(1). The `_remove` and `_insert_at_front` helpers each perform a fixed number of pointer assignments regardless of cache size.

**Space:** The hash map and doubly linked list each hold at most `capacity` entries (plus two sentinel nodes). Space scales linearly with capacity: O(capacity).

A common follow-up: *"How would you make this thread-safe?"* Wrap each `get` and `put` with a mutex lock. Both operations become atomic critical sections. Under heavy concurrent access, the lock becomes a bottleneck, which leads to discussing sharded caches or lock-free data structures.

---

## Common Interview Mistakes

1. **Using a list instead of a doubly linked list for ordering.** A Python list's `remove()` is O(n). This is the single most common mistake. Candidates implement a logically correct LRU cache that violates the O(1) requirement. Always justify why a doubly linked list is necessary.

2. **Forgetting to store the key inside the Node.** When evicting `tail.prev`, you need its key to delete it from the hash map. Nodes that only store values force a reverse lookup, which is O(n). Storing the key in the node is the clean solution.

3. **Getting the four pointer assignments in `_insert_at_front` in the wrong order.** The new node's `prev` and `next` must be set before updating `head.next` and the old first node's `prev`. Updating `head.next` first loses the reference to the node that needs its `prev` updated.

4. **Not handling the `put` update case.** When `put` is called with an existing key, you must remove the old node *before* checking capacity and creating a new one. Failing to do so causes a ghost node in the list and a stale reference in the hash map.

5. **Skipping the sentinel node design.** Without dummy head and tail, every insertion and deletion requires `if node.prev is None` and `if node.next is None` guards. This doubles the code and introduces more places for bugs.

6. **Reaching for `OrderedDict` without being able to explain it.** Using Python's `OrderedDict` is acceptable and elegant, but interviewers frequently follow up with "can you implement this without that built-in?" If you can't, you've shown you know a library shortcut but not the underlying structure.

7. **Not drawing the data structure before coding.** LRU Cache has more moving parts than most problems. Candidates who sketch the linked list layout, head -> [A] <-> [B] <-> [C] -> tail, before writing code catch pointer errors before they happen.

---

## Resources

- **Full Walkthrough**: [LRU Cache: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/lru-cache-interview-walkthrough/)
- **Practice**: [Mock interview for LRU Cache](https://intervu.dev/setup2?problem=lru-cache)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Linked List Cycle](linked-list-cycle.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/linked-list-cycle-interview-walkthrough/)
- [Merge Two Sorted Lists](merge-two-sorted-lists.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/merge-two-sorted-lists-interview-walkthrough/)
- [Reverse Linked List](reverse-linked-list.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/reverse-linked-list-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
