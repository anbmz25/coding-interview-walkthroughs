# Middle of the Linked List

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/middle-of-the-linked-list-interview-walkthrough/)*

> Master Middle of the Linked List for your coding interview. Learn the fast-slow pointer pattern, even-length list handling, and what interviewers actually evaluate.

**Difficulty**: Easy
**Patterns**: `linked-list`, `two-pointers`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/middle-of-the-linked-list-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=middle-of-the-linked-list)**

---

## Problem

Given the `head` of a singly linked list, return the middle node. If there are two middle nodes, return the second one.

### Example 1

**Input:** `[1,2,3,4,5]`
**Output:** Node 3 (the middle)

### Example 2

**Input:** `[1,2,3,4,5,6]`
**Output:** Node 4 (second of two middles)

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=middle-of-the-linked-list)*

---

## Solution

```python
def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
```

**Trace for [1,2,3,4,5,6]:**
- Start: slow=1, fast=1
- Step 1: slow=2, fast=3
- Step 2: slow=3, fast=5
- Step 3: slow=4, fast=None → exit
- Return node 4 ✓

---

## Complexity

| Aspect | Complexity |
|---|---|
| Time | O(n) |
| Space | O(1) |

---

## Common Interview Mistakes

1. **Wrong termination condition.** `while fast.next` returns the first middle for even lists; `while fast and fast.next` returns the second. Know which you need.

2. **Null pointer on `fast.next.next`.** The guard `fast and fast.next` ensures fast has both a value and a next node before advancing.

3. **Not knowing this is the foundation for harder problems.** Interviewers often follow up with "how would you use this to sort a linked list?" (merge sort) or "detect a palindrome?" (fast-slow + reverse second half).

---

## Resources

- **Full Walkthrough**: [Middle of the Linked List: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/middle-of-the-linked-list-interview-walkthrough/)
- **Practice**: [Mock interview for Middle of the Linked List](https://intervu.dev/setup2?problem=middle-of-the-linked-list)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Linked List Cycle](linked-list-cycle.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/linked-list-cycle-interview-walkthrough/)
- [LRU Cache](lru-cache.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/lru-cache-interview-walkthrough/)
- [Merge K Sorted Lists](merge-k-sorted-lists.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/merge-k-sorted-lists-interview-walkthrough/)
- [Merge Two Sorted Lists](merge-two-sorted-lists.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/merge-two-sorted-lists-interview-walkthrough/)
- [Reverse Linked List](reverse-linked-list.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/reverse-linked-list-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
