# Construct Binary Tree from Preorder and Inorder Traversal

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/construct-binary-tree-from-preorder-and-inorder-traversal-interview-walkthrough/)*

> A step-by-step walkthrough of Construct Binary Tree from Preorder and Inorder Traversal as it unfolds in a real coding interview. Learn the recursive reconstruction algorithm, the hash map optimization, and how to avoid common index-tracking mistakes.

**Difficulty**: Medium
**Patterns**: `tree`, `recursion`, `construct-binary-tree-from-preorder-and-inorder-traversal`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/construct-binary-tree-from-preorder-and-inorder-traversal-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=construct-binary-tree-from-preorder-and-inorder-traversal)**

---

## Problem

Given two integer arrays `preorder` and `inorder` where `preorder` is the preorder traversal and `inorder` is the inorder traversal of the same binary tree, construct and return the binary tree. ([LeetCode #105](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/))

### Example

**Input**
`preorder = [3,9,20,15,7]`, `inorder = [9,3,15,20,7]`

**Output**
Tree with structure: root=3, left=9, right subtree rooted at 20 with children 15 (left) and 7 (right).

The preorder tells us 3 is the root. In the inorder array, 3 sits at index 1, so everything left of index 1 (`[9]`) is the left subtree and everything right (`[15,20,7]`) is the right subtree. Recurse on each half.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=construct-binary-tree-from-preorder-and-inorder-traversal)*

---

## Solution

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
    inorder_index = {val: idx for idx, val in enumerate(inorder)}
    pre_idx = [0]  # mutable reference to track position in preorder

    def build(in_left: int, in_right: int) -> Optional[TreeNode]:
        if in_left > in_right:
            return None

        root_val = preorder[pre_idx[0]]
        pre_idx[0] += 1
        root = TreeNode(root_val)

        mid = inorder_index[root_val]
        root.left = build(in_left, mid - 1)
        root.right = build(mid + 1, in_right)
        return root

    return build(0, len(inorder) - 1)
```

Why this is interview-friendly:

- **Hash map eliminates O(n) scan.** The `inorder_index` dict gives O(1) root lookups.
- **Mutable `pre_idx` avoids passing/returning indices.** Using `[0]` (a list) allows the nested function to modify it. An alternative is `nonlocal` in Python 3.
- **No array slicing.** Slicing creates copies per call, turning O(n) space into O(n^2). Index bounds `in_left` and `in_right` keep it at O(n).

---

## Complexity

| | Time | Space |
|---|---|---|
| Construct Binary Tree | O(n) | O(n) |

Hash map gives O(1) lookup. Each node is created exactly once. Recursion depth is O(h): O(log n) for balanced trees, O(n) for skewed trees. The hash map uses O(n) space.

---

## Common Interview Mistakes

1. **Slicing preorder and inorder arrays.** `preorder[1:mid+1]` creates a new copy per call, turning O(n) space into O(n^2) total. Use index bounds instead.

2. **Searching linearly for the root in inorder.** O(n) per call leads to O(n^2) total for skewed trees. The hash map makes it O(1).

3. **Wrong subtree size.** The left subtree has `mid - in_left` nodes. Use this count to correctly determine the preorder range if passing explicit bounds.

4. **Building right before left.** Preorder visits left subtree before right subtree. If you build the right subtree first, `pre_idx` will point to the wrong node. Order matters.

5. **Mutating preorder directly.** Using `preorder.pop(0)` is O(n) per pop (shifting all elements). Use a pointer instead.

---

## Resources

- **Full Walkthrough**: [Construct Binary Tree from Preorder and Inorder Traversal: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/construct-binary-tree-from-preorder-and-inorder-traversal-interview-walkthrough/)
- **Practice**: [Mock interview for Construct Binary Tree from Preorder and Inorder Traversal](https://intervu.dev/setup2?problem=construct-binary-tree-from-preorder-and-inorder-traversal)
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
- [Kth Smallest Element in a BST](kth-smallest-element-in-a-bst.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/kth-smallest-element-in-a-bst-interview-walkthrough/)
- [Lowest Common Ancestor of a Binary Tree](lowest-common-ancestor.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/lowest-common-ancestor-interview-walkthrough/)
- [Lowest Common Ancestor of a Binary Search Tree](lowest-common-ancestor-of-a-binary-search-tree.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/lowest-common-ancestor-of-a-binary-search-tree-interview-walkthrough/)
- [Maximum Depth of Binary Tree](maximum-depth-of-binary-tree.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/maximum-depth-of-binary-tree-interview-walkthrough/)
- [Serialize and Deserialize Binary Tree](serialize-and-deserialize-binary-tree.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/serialize-and-deserialize-binary-tree-interview-walkthrough/)
- [Validate Binary Search Tree](validate-binary-search-tree.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/validate-binary-search-tree-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
