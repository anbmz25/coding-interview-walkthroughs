# Maximum Depth of Binary Tree

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/maximum-depth-of-binary-tree-interview-walkthrough/)*

> Master Maximum Depth of Binary Tree for your coding interview. Learn recursive DFS, iterative BFS, common mistakes, and what interviewers actually evaluate.

**Difficulty**: Easy
**Patterns**: `tree`, `depth-first-search`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/maximum-depth-of-binary-tree-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=maximum-depth-of-binary-tree)**

---

## Problem

Given the root of a binary tree, return its maximum depth. The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

### Example

**Input**
```
    3
   / \
  9  20
    /  \
   15   7
```

**Output**
`3`

The longest path is `3 → 20 → 15` (or `3 → 20 → 7`), which has 3 nodes.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=maximum-depth-of-binary-tree)*

---

## Solution

**Recursive DFS:**

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

**Iterative BFS (level-order):**

```python
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        depth = 0
        queue = deque([root])

        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return depth
```

The BFS version is more code but avoids Python's recursion limit (~1000 frames by default) on deeply skewed trees.

---

## Complexity

| Approach | Time | Space |
|---|---|---|
| Recursive DFS | O(n) | O(h), call stack height |
| Iterative BFS | O(n) | O(w), max queue width (widest level) |

For a balanced tree, h = O(log n). For a skewed tree, h = O(n). BFS space is O(n/2) in the worst case (a complete binary tree's last level).

---

## Common Interview Mistakes

1. **Returning depth instead of 1 + depth.** Forgetting to count the current node is the most common off-by-one.

2. **Not handling `None` as the base case.** Some candidates check `if not root.left and not root.right: return 1`, which is correct but harder to reason about than `if root is None: return 0`.

3. **Confusing depth (nodes) with height (edges).** Confirm which definition applies. They differ by 1.

4. **Not mentioning iterative BFS as an alternative.** Even if you implement recursion, noting "this can hit Python's recursion limit on skewed trees, I'd use BFS in production" shows engineering judgment.

5. **Over-explaining the recursion.** Strong candidates say one sentence and write three lines of code. Weaker candidates describe every recursive call. Trust the recursion.

---

## Resources

- **Full Walkthrough**: [Maximum Depth of Binary Tree: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/maximum-depth-of-binary-tree-interview-walkthrough/)
- **Practice**: [Mock interview for Maximum Depth of Binary Tree](https://intervu.dev/setup2?problem=maximum-depth-of-binary-tree)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Balanced Binary Tree](balanced-binary-tree.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/balanced-binary-tree-interview-walkthrough/)
- [Binary Tree Level Order Traversal](binary-tree-level-order-traversal.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/binary-tree-level-order-traversal-interview-walkthrough/)
- [Binary Tree Right Side View](binary-tree-right-side-view.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/binary-tree-right-side-view-interview-walkthrough/)
- [Construct Binary Tree from Preorder and Inorder Traversal](construct-binary-tree-from-preorder-and-inorder-traversal.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/construct-binary-tree-from-preorder-and-inorder-traversal-interview-walkthrough/)
- [Diameter of Binary Tree](diameter-of-binary-tree.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/diameter-of-binary-tree-interview-walkthrough/)
- [Invert Binary Tree](invert-binary-tree.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/invert-binary-tree-interview-walkthrough/)
- [Kth Smallest Element in a BST](kth-smallest-element-in-a-bst.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/kth-smallest-element-in-a-bst-interview-walkthrough/)
- [Lowest Common Ancestor of a Binary Tree](lowest-common-ancestor.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/lowest-common-ancestor-interview-walkthrough/)
- [Lowest Common Ancestor of a Binary Search Tree](lowest-common-ancestor-of-a-binary-search-tree.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/lowest-common-ancestor-of-a-binary-search-tree-interview-walkthrough/)
- [Serialize and Deserialize Binary Tree](serialize-and-deserialize-binary-tree.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/serialize-and-deserialize-binary-tree-interview-walkthrough/)
- [Validate Binary Search Tree](validate-binary-search-tree.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/validate-binary-search-tree-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
