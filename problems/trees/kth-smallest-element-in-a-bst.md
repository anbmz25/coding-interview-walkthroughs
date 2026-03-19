# Kth Smallest Element in a BST

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/kth-smallest-element-in-a-bst-interview-walkthrough/)*

> Master Kth Smallest Element in a BST for your coding interview. Learn the in-order traversal shortcut, iterative early-exit, and the augmented-tree follow-up.

**Difficulty**: Medium
**Patterns**: `tree`, `binary-search-tree`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/kth-smallest-element-in-a-bst-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=kth-smallest-element-in-a-bst)**

---

## Problem

Given the `root` of a binary search tree and an integer `k`, return the `k`th smallest value (1-indexed) among all node values.

### Example

**Input:** `root = [5,3,6,2,4,null,null,1]`, `k = 3`
**Output:** `3`

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=kth-smallest-element-in-a-bst)*

---

## Solution

**Iterative (preferred, cleanest early exit):**
```python
def kthSmallest(root, k: int) -> int:
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        k -= 1
        if k == 0:
            return current.val

        current = current.right
```

---

## Complexity

| Aspect | Complexity |
|---|---|
| Time | O(H + k), H is tree height, stop after k nodes |
| Space | O(H), stack depth |

---

## Common Interview Mistakes

1. **Traversing the whole tree.** Stop as soon as k hits 0. No need to visit remaining nodes.

2. **Collecting all values then indexing.** `values[k-1]` works but is O(n) time and space. The iterative approach terminates early.

3. **Not knowing the follow-up.** If the BST is modified frequently and `kthSmallest` is called many times, augment each node with `left_count`. Query becomes O(log n).

---

## Resources

- **Full Walkthrough**: [Kth Smallest Element in a BST: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/kth-smallest-element-in-a-bst-interview-walkthrough/)
- **Practice**: [Mock interview for Kth Smallest Element in a BST](https://intervu.dev/setup2?problem=kth-smallest-element-in-a-bst)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Balanced Binary Tree](balanced-binary-tree.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/balanced-binary-tree-interview-walkthrough/)
- [Binary Tree Level Order Traversal](binary-tree-level-order-traversal.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/binary-tree-level-order-traversal-interview-walkthrough/)
- [Binary Tree Right Side View](binary-tree-right-side-view.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/binary-tree-right-side-view-interview-walkthrough/)
- [Diameter of Binary Tree](diameter-of-binary-tree.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/diameter-of-binary-tree-interview-walkthrough/)
- [Invert Binary Tree](invert-binary-tree.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/invert-binary-tree-interview-walkthrough/)
- [Lowest Common Ancestor of a Binary Tree](lowest-common-ancestor.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/lowest-common-ancestor-interview-walkthrough/)
- [Lowest Common Ancestor of a Binary Search Tree](lowest-common-ancestor-of-a-binary-search-tree.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/lowest-common-ancestor-of-a-binary-search-tree-interview-walkthrough/)
- [Maximum Depth of Binary Tree](maximum-depth-of-binary-tree.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/maximum-depth-of-binary-tree-interview-walkthrough/)
- [Validate Binary Search Tree](validate-binary-search-tree.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/validate-binary-search-tree-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
