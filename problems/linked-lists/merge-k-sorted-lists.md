# Merge K Sorted Lists

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/merge-k-sorted-lists-interview-walkthrough/)*

> A step-by-step walkthrough of LeetCode #23 as it plays out in a real coding interview. Learn the min-heap K-way merge pattern, the Python tiebreaker trick, and the divide-and-conquer alternative that uses O(1) extra space.

**Difficulty**: Hard
**Patterns**: `heaps`, `linked-lists`, `divide-and-conquer`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/merge-k-sorted-lists-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=merge-k-sorted-lists)**

---

## Problem

You are given an array of `k` linked lists, where each list is sorted in ascending order. Merge all of them into a single sorted linked list and return it.

([LeetCode #23](https://leetcode.com/problems/merge-k-sorted-lists/))

### Example

**Input**
```
lists = [
  1 -> 4 -> 5,
  1 -> 3 -> 4,
  2 -> 6
]
```

**Output**
`1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6`

Pick the smallest node from the heads of all lists at each step, producing a single sorted list.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=merge-k-sorted-lists)*

---

## Solution

```python
import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # (value, index, node): index breaks ties, avoiding ListNode comparison
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
```

**Why include `i` in the tuple?** Python's `heapq` compares tuples element by element. If two nodes share the same value, it tries comparing the `ListNode` objects, which raises a `TypeError`. The list index acts as a tiebreaker.

### Bonus: Divide & Conquer

```python
def mergeKLists_dc(lists):
    if not lists:
        return None

    def merge_two(l1, l2):
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next

    interval = 1
    while interval < len(lists):
        for i in range(0, len(lists) - interval, interval * 2):
            lists[i] = merge_two(lists[i], lists[i + interval])
        interval *= 2

    return lists[0]
```

Same O(N log k) time, but O(1) extra space.

---

## Complexity

| Approach | Time | Space |
|---|---|---|
| Brute force (collect & sort) | O(N log N) | O(N) |
| Min-heap | O(N log k) | O(k) |
| Divide & conquer | O(N log k) | O(1) extra |

**Why O(N log k) beats O(N log N):** The heap holds at most k elements, so operations cost O(log k), not O(log N). When k is much smaller than N, this is dramatically faster.

---

## Common Interview Mistakes

1. **Not handling the tuple tiebreaker in Python.** Forgetting the list index `i` causes a `TypeError` when two nodes share the same value.

2. **Pushing null nodes into the heap.** Always check `if node` before pushing.

3. **Using naive O(N*k) approach.** Scanning all k heads linearly for each node gives O(N*k).

4. **Confusing N and k in complexity analysis.** N is total nodes, k is number of lists. Be precise.

5. **Not mentioning the divide & conquer alternative.** Noting it shows algorithmic maturity.

6. **Forgetting the dummy head pattern.** It eliminates messy conditional logic.

---

## Resources

- **Full Walkthrough**: [Merge K Sorted Lists: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/merge-k-sorted-lists-interview-walkthrough/)
- **Practice**: [Mock interview for Merge K Sorted Lists](https://intervu.dev/setup2?problem=merge-k-sorted-lists)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Linked List Cycle](linked-list-cycle.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/linked-list-cycle-interview-walkthrough/)
- [LRU Cache](lru-cache.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/lru-cache-interview-walkthrough/)
- [Merge Two Sorted Lists](merge-two-sorted-lists.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/merge-two-sorted-lists-interview-walkthrough/)
- [Middle of the Linked List](middle-of-the-linked-list.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/middle-of-the-linked-list-interview-walkthrough/)
- [Reverse Linked List](reverse-linked-list.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/reverse-linked-list-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
