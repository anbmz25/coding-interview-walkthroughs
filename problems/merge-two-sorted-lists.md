# Merge Two Sorted Lists

> A step-by-step guide to solving Merge Two Sorted Lists in a coding interview: the dummy node pattern, iterative and recursive approaches, pointer mistakes to avoid, and what strong candidates sound like.

**Difficulty**: Easy
**Patterns**: `linked-lists`, `two-pointers`

📖 **[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/merge-two-sorted-lists-interview-walkthrough/)**
🎙️ **[Practice in a mock interview →](https://intervu.dev/setup2?problem=merge-two-sorted-lists)**

---

## Problem

You are given the heads of two sorted linked lists, `list1` and `list2`. Merge them into a single sorted linked list by **splicing together the nodes** of the two input lists (not creating new nodes). Return the head of the merged list. ([LeetCode #21](https://leetcode.com/problems/merge-two-sorted-lists/))

### Example

**Input**
`list1 = [1,2,4], list2 = [1,3,4]`

**Output**
`[1,1,2,3,4,4]`

Both input lists are sorted in non-decreasing order. The merge compares front nodes, appends the smaller one, and advances that pointer. When one list is exhausted, the remaining nodes of the other are appended directly. No new nodes are created.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=merge-two-sorted-lists)*

---

## Solution

### Iterative: Dummy Node (Recommended for Interviews)

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    # Dummy sentinel node: avoids special-casing the first insertion
    dummy = ListNode(0)
    current = dummy  # Tracks the tail of the merged list

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1   # Attach the smaller node
            list1 = list1.next     # Advance list1's pointer
        else:
            current.next = list2
            list2 = list2.next
        current = current.next     # Advance the merged list's tail

    # One list is exhausted: attach the remainder of the other
    current.next = list1 if list1 else list2

    return dummy.next  # Skip the sentinel, return the real head
```

### Recursive: Elegant Alternative

```python
def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    # Base cases: if either list is exhausted, return the other
    if not list1:
        return list2
    if not list2:
        return list1

    # The smaller head becomes the next node in the merged list
    if list1.val <= list2.val:
        list1.next = mergeTwoLists(list1.next, list2)  # Recurse on list1's tail
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)  # Recurse on list2's tail
        return list2
```

Key implementation notes:

- **The dummy node's value doesn't matter.** It's a structural anchor, never part of the output.
- **`current.next = list1 if list1 else list2`** is the tail-attachment step. This single line handles both the case where `list1` has remaining nodes and the case where `list2` does.
- **In the recursive version, `list1.next = mergeTwoLists(...)`** modifies the chosen node's `next` pointer in place, splicing the lists without creating new nodes.
- **The recursive version uses O(n + m) stack space**, one frame per node. For very long lists, this risks stack overflow. The iterative version uses O(1) space.

---

## Complexity

| Approach | Time | Space |
|---|---|---|
| Iterative (dummy node) | O(n + m) | O(1) |
| Recursive | O(n + m) | O(n + m) |

**Time:** Both approaches visit every node exactly once. Each visit does constant work. Total: O(n + m).

**Space:** Iterative uses only a fixed number of pointers, O(1). Recursive places one stack frame per call, O(n + m) total depth.

For interviews, the iterative approach is generally preferred for production-grade thinking. The recursive approach is elegant and worth presenting as an alternative, with its stack space tradeoff named explicitly.

---

## Common Interview Mistakes

1. **Forgetting the tail-attachment step.** When the loop exits, one list still has remaining nodes. Forgetting `current.next = list1 if list1 else list2` truncates the output. The single most common bug.

2. **Not using a dummy node and struggling with head insertion.** Without a sentinel, the first node requires special handling. The dummy node collapses initialization and loop logic into one path.

3. **Advancing the wrong pointer.** After choosing `list1.val`, you must advance `list1 = list1.next`, not `list2`. Mixing these up corrupts the merged list.

4. **Creating a cycle by not advancing `current`.** If you forget `current = current.next`, the tail never moves forward. The next iteration overwrites `current.next`, creating a cycle.

5. **Not discussing the recursive stack depth tradeoff.** Presenting the recursive solution without mentioning O(n + m) stack space shows incomplete analysis.

6. **Skipping the trace-through.** A quick trace on `[1,3]` + `[2,4]` catches pointer bugs before the interviewer does.

---

## Resources

- 📖 **Full Walkthrough**: [Merge Two Sorted Lists: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/merge-two-sorted-lists-interview-walkthrough/)
- 🎙️ **Practice**: [Mock interview for Merge Two Sorted Lists](https://intervu.dev/setup2?problem=merge-two-sorted-lists)
- 📚 [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- 📚 [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- 📚 [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
