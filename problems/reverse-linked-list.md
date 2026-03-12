# Reverse Linked List

> A step-by-step guide to solving Reverse Linked List in a coding interview: the three-pointer iterative technique, the recursive approach, pointer mistakes to avoid, and what strong candidates sound like.

**Difficulty**: Easy
**Patterns**: `linked-lists`, `two-pointers`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/reverse-linked-list-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=reverse-linked-list)**

---

## Problem

Given the `head` of a singly linked list, reverse the list and return the new head. The reversal must be done in place by relinking the existing nodes. ([LeetCode #206](https://leetcode.com/problems/reverse-linked-list/))

### Example

**Input**
`head = [1,2,3,4,5]`

**Output**
`[5,4,3,2,1]`

The original list `1 → 2 → 3 → 4 → 5 → None` becomes `5 → 4 → 3 → 2 → 1 → None`. Each node's `next` pointer is redirected to point backward. Node `1` becomes the tail, node `5` becomes the new head. No new nodes are created.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=reverse-linked-list)*

---

## Solution

### Iterative: Three Pointers (Recommended)

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode) -> ListNode:
    prev = None       # Will become the new tail anchor
    current = head    # Start at the head

    while current is not None:
        next_node = current.next   # Step 1: Save next before breaking link
        current.next = prev        # Step 2: Flip pointer backward
        prev = current             # Step 3: Advance prev
        current = next_node        # Step 4: Advance current

    return prev  # prev is the new head (original tail)
```

### Recursive: Elegant but O(n) Stack Space

```python
def reverseList(head: ListNode) -> ListNode:
    # Base case: empty list or single node
    if head is None or head.next is None:
        return head

    # Recurse to the end: new_head is the original last node
    new_head = reverseList(head.next)

    # On the way back: make head.next point back to head
    head.next.next = head
    head.next = None        # Break the original forward link

    return new_head  # Propagate the new head all the way up
```

Key implementation notes:

- **`next_node` must be saved first.** Once `current.next = prev` executes, the forward reference is gone. Without saving it, the rest of the list becomes unreachable.
- **`prev` starts as `None`.** The original head becomes the new tail, pointing to `None`.
- **Return `prev`, not `current`.** When the loop exits, `current` is `None`. `prev` is the last processed node: the new head.
- **In the recursive version, `head.next.next = head` then `head.next = None` is the crux.** Without `head.next = None`, a cycle is created.
- **Recursive uses O(n) stack space**, one frame per node. Approaches Python's default recursion limit for lists over 1,000 nodes.

---

## Complexity

| Approach | Time | Space |
|---|---|---|
| Iterative (three pointers) | O(n) | O(1) |
| Recursive | O(n) | O(n) |

**Time:** Both visit every node once. O(n).

**Space (iterative):** Three pointer variables. True O(1).

**Space (recursive):** One stack frame per node. O(n), with stack overflow risk for long lists.

---

## Common Interview Mistakes

1. **Forgetting to save `next_node` before redirecting.** The most catastrophic bug. The rest of the list becomes unreachable.

2. **Returning `current` instead of `prev`.** `current` is `None` at loop exit. The reversed list is silently discarded.

3. **Using `while current.next` instead of `while current`.** Skips the last node entirely.

4. **In the recursive version, forgetting `head.next = None`.** Creates a cycle between the last two nodes.

5. **Initializing `prev = head` instead of `prev = None`.** The first node's `next` points to itself, creating a length-1 cycle.

6. **Not narrating the pointer state.** The four steps are mechanical. Coding silently gives the interviewer no way to verify understanding.

---

## Resources

- **Full Walkthrough**: [Reverse Linked List: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/reverse-linked-list-interview-walkthrough/)
- **Practice**: [Mock interview for Reverse Linked List](https://intervu.dev/setup2?problem=reverse-linked-list)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
