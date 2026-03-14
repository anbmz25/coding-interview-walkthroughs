# Balanced Binary Tree

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/balanced-binary-tree-interview-walkthrough/)*

> A step-by-step walkthrough of the Balanced Binary Tree problem as it unfolds in a real coding interview. Learn the O(n²) trap, the bottom-up sentinel technique, and how strong candidates avoid redundant work.

**Difficulty**: Easy
**Patterns**: `binary-tree`, `dfs`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/balanced-binary-tree-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=balanced-binary-tree)**

---

## Problem

Given a binary tree, determine if it is height-balanced. A binary tree is height-balanced if, for every node, the absolute difference between the heights of the left and right subtrees is at most 1. ([LeetCode #110](https://leetcode.com/problems/balanced-binary-tree/))

### Example 1

**Input:**
```
    3
   / \
  9  20
    /  \
   15   7
```
**Output:** `true`

### Example 2

**Input:**
```
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
```
**Output:** `false`

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=balanced-binary-tree)*

---

## Solution

```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            left = check(node.left)
            if left == -1:
                return -1  # Short-circuit: left subtree is unbalanced

            right = check(node.right)
            if right == -1:
                return -1  # Short-circuit: right subtree is unbalanced

            if abs(left - right) > 1:
                return -1  # This node is not balanced

            return 1 + max(left, right)  # Return height to parent

        return check(root) != -1
```

---

## Complexity


---

## Common Interview Mistakes

- **Writing the O(n²) solution without noticing.** Calling a separate `height()` function inside a recursive `isBalanced()` is the trap.

- **Checking only the root.** Balance must hold at *every* node, not just the root.

- **Using -1 without explaining why.** State clearly: -1 is a sentinel that means "unbalanced; propagate immediately."

- **Forgetting to short-circuit on -1.** If you compute both `left` and `right` before checking for -1, you've lost the early-exit benefit.

---

## Resources

- **Full Walkthrough**: [Balanced Binary Tree: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/balanced-binary-tree-interview-walkthrough/)
- **Practice**: [Mock interview for Balanced Binary Tree](https://intervu.dev/setup2?problem=balanced-binary-tree)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Binary Tree Level Order Traversal](binary-tree-level-order-traversal.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/binary-tree-level-order-traversal-interview-walkthrough/)
- [Invert Binary Tree](invert-binary-tree.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/invert-binary-tree-interview-walkthrough/)
- [Lowest Common Ancestor of a Binary Tree](lowest-common-ancestor.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/lowest-common-ancestor-interview-walkthrough/)
- [Validate Binary Search Tree](validate-binary-search-tree.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/validate-binary-search-tree-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
