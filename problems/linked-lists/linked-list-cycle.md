# Linked List Cycle

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/linked-list-cycle-interview-walkthrough/)*

> A step-by-step guide to solving Linked List Cycle in a coding interview: Floyd's tortoise and hare algorithm, the hash set baseline, the mathematical proof of why pointers meet, and what strong candidates sound like.

**Difficulty**: Easy
**Patterns**: `linked-lists`, `two-pointers`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/linked-list-cycle-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=linked-list-cycle)**

---

## Problem

Given the `head` of a linked list, determine if the list contains a **cycle**. A cycle exists if some node can be reached again by continuously following the `next` pointer. Return `true` if there is a cycle, `false` otherwise. ([LeetCode #141](https://leetcode.com/problems/linked-list-cycle/))

### Example

**Input**
`head = [3,2,0,-4], pos = 1`

**Output**
`true`

The tail node (`-4`) points back to index `1` (value `2`), creating a cycle: `3 → 2 → 0 → -4 → 2 → ...`. Note that `pos` is not a parameter to your function. A second example: `head = [1,2], pos = -1` returns `false` because the list terminates at `None`.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=linked-list-cycle)*

---

## Solution

### Hash Set (O(n) space, intuitive)

```python
def hasCycle(head: ListNode) -> bool:
    visited = set()
    current = head

    while current is not None:
        if current in visited:
            return True       # Cycle confirmed
        visited.add(current)
        current = current.next

    return False  # Reached None: no cycle
```

### Floyd's Tortoise and Hare (O(1) space, optimal)

```python
def hasCycle(head: ListNode) -> bool:
    if not head or not head.next:
        return False  # Empty list or single node without self-loop

    slow = head        # Moves 1 step at a time
    fast = head        # Moves 2 steps at a time

    while fast is not None and fast.next is not None:
        slow = slow.next          # One step
        fast = fast.next.next     # Two steps

        if slow == fast:
            return True   # Pointers met: cycle detected

    return False  # fast hit None: list terminates
```

Key implementation notes:

- **`fast is not None and fast.next is not None` guards two-step advancement.** Check `fast` first (short-circuit), then `fast.next`. Reversing the order or omitting either check causes `AttributeError`.
- **Both pointers start at `head`.** They diverge on the first iteration. Starting `fast = head.next` also works but requires adjusting the loop.
- **Pointer equality compares references, not values.** Two nodes with the same `val` are distinct objects.
- **The hash set stores node objects, not values.** `visited.add(current)` adds the reference.

---

## Complexity

| Approach | Time | Space |
|---|---|---|
| Hash Set | O(n) | O(n) |
| Floyd's Two-Pointer | O(n) | O(1) |

**Time (Floyd's):** Without a cycle, `fast` reaches the end in O(n/2) steps. With a cycle, after both enter the loop, they meet within at most `c` iterations (cycle length). Since `c <= n`, total is O(n).

**Space (Floyd's):** Two pointer variables regardless of list size. True O(1).

---

## Common Interview Mistakes

1. **Forgetting to check `fast.next` before advancing.** If `fast` is the last node, `fast.next.next` raises `AttributeError`. The most common bug.

2. **Using node values instead of references in the hash set.** Storing `current.val` instead of `current` gives false positives when values repeat.

3. **Not explaining why pointers are guaranteed to meet.** Saying "fast catches slow" without justifying why is hand-waving. The real explanation: fast gains exactly one step per iteration, so the gap closes by one deterministically.

4. **Not presenting the hash set solution first.** Jumping to Floyd's without establishing the O(n) space baseline makes the optimization appear unjustified.

5. **Not mentioning the follow-up (finding cycle start).** Most interviewers will ask about LeetCode #142. Having a prepared answer ("reset one pointer to head, advance both one step, they meet at cycle entry") signals depth.

---

## Resources

- **Full Walkthrough**: [Linked List Cycle: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/linked-list-cycle-interview-walkthrough/)
- **Practice**: [Mock interview for Linked List Cycle](https://intervu.dev/setup2?problem=linked-list-cycle)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [LRU Cache](lru-cache.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/lru-cache-interview-walkthrough/)
- [Merge K Sorted Lists](merge-k-sorted-lists.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/merge-k-sorted-lists-interview-walkthrough/)
- [Merge Two Sorted Lists](merge-two-sorted-lists.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/merge-two-sorted-lists-interview-walkthrough/)
- [Reverse Linked List](reverse-linked-list.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/reverse-linked-list-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
