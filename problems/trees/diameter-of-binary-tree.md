# Diameter of Binary Tree

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/diameter-of-binary-tree-interview-walkthrough/)*

> Master Diameter of Binary Tree for your coding interview. Learn the DFS-with-side-effect pattern, why the path may not pass through root, common mistakes, and what interviewers evaluate.

**Difficulty**: Easy
**Patterns**: `tree`, `depth-first-search`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/diameter-of-binary-tree-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=diameter-of-binary-tree)**

---

## Problem

Given the root of a binary tree, return the length of the diameter of the tree. The diameter is the length of the longest path between any two nodes. This path may or may not pass through the root. The length of a path between two nodes is the number of edges between them.

### Example 1

**Input**
```
    1
   / \
  2   3
 / \
4   5
```

**Output**
`3`

The longest path is `4 → 2 → 1 → 3` or `5 → 2 → 1 → 3`, both with 3 edges.

### Example 2

**Input**
```
  1
 /
2
```

**Output**
`1`

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=diameter-of-binary-tree)*

---

## Solution

```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def height(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            left_h = height(node.left)
            right_h = height(node.right)

            # Update global diameter: path through this node
            self.max_diameter = max(self.max_diameter, left_h + right_h)

            # Return height to parent
            return 1 + max(left_h, right_h)

        height(root)
        return self.max_diameter
```

**Why `self.max_diameter`?** The diameter isn't always at the root, so we can't just return it up the stack. We need a side-channel to track the maximum across all nodes.

---

## Complexity

| Aspect | Complexity | Explanation |
|---|---|---|
| Time | O(n) | Every node visited exactly once |
| Space | O(h) | Call stack depth equals tree height |

---

## Common Interview Mistakes

1. **Only considering paths through the root.** This is the most common mistake, returning `maxDepth(left) + maxDepth(right)` from `diameterOfBinaryTree` without recursing into subtrees.

2. **Calling `maxDepth` separately inside the loop.** Computing height separately for each node makes the solution O(n²). Computing height and diameter together in one DFS is O(n).

3. **Confusing edges and nodes.** The problem asks for edges. A leaf has diameter 0, not 1. A two-node tree has diameter 1.

4. **Forgetting the `max_diameter = 0` initialization.** For a single-node tree, the diameter is 0. Initializing to -1 or 1 would give wrong results.

5. **Returning the diameter instead of height from the helper.** The helper must return height so the parent can use it: the diameter is tracked separately.

---

## Resources

- **Full Walkthrough**: [Diameter of Binary Tree: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/diameter-of-binary-tree-interview-walkthrough/)
- **Practice**: [Mock interview for Diameter of Binary Tree](https://intervu.dev/setup2?problem=diameter-of-binary-tree)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Balanced Binary Tree](balanced-binary-tree.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/balanced-binary-tree-interview-walkthrough/)
- [Binary Tree Level Order Traversal](binary-tree-level-order-traversal.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/binary-tree-level-order-traversal-interview-walkthrough/)
- [Binary Tree Right Side View](binary-tree-right-side-view.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/binary-tree-right-side-view-interview-walkthrough/)
- [Invert Binary Tree](invert-binary-tree.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/invert-binary-tree-interview-walkthrough/)
- [Kth Smallest Element in a BST](kth-smallest-element-in-a-bst.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/kth-smallest-element-in-a-bst-interview-walkthrough/)
- [Lowest Common Ancestor of a Binary Tree](lowest-common-ancestor.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/lowest-common-ancestor-interview-walkthrough/)
- [Lowest Common Ancestor of a Binary Search Tree](lowest-common-ancestor-of-a-binary-search-tree.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/lowest-common-ancestor-of-a-binary-search-tree-interview-walkthrough/)
- [Maximum Depth of Binary Tree](maximum-depth-of-binary-tree.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/maximum-depth-of-binary-tree-interview-walkthrough/)
- [Validate Binary Search Tree](validate-binary-search-tree.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/validate-binary-search-tree-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
