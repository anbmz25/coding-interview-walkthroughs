# Lowest Common Ancestor of a Binary Search Tree

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/lowest-common-ancestor-of-a-binary-search-tree-interview-walkthrough/)*

> Master Lowest Common Ancestor of a BST for your coding interview. Learn the split-point insight, iterative O(1) solution, and what interviewers actually evaluate.

**Difficulty**: Easy
**Patterns**: `tree`, `depth-first-search`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/lowest-common-ancestor-of-a-binary-search-tree-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=lowest-common-ancestor-of-a-binary-search-tree)**

---

## Problem

Given a binary search tree and two nodes `p` and `q`, find their lowest common ancestor (LCA). The LCA is defined as the deepest node that has both `p` and `q` as descendants (a node can be a descendant of itself).

### Example

**Input:** root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
**Output:** 6

**Input:** root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
**Output:** 2

Node 2 is the ancestor of both itself and node 4.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=lowest-common-ancestor-of-a-binary-search-tree)*

---

## Solution

**Recursive:**
```python
def lowestCommonAncestor(root, p, q):
    if p.val < root.val and q.val < root.val:
        return lowestCommonAncestor(root.left, p, q)
    if p.val > root.val and q.val > root.val:
        return lowestCommonAncestor(root.right, p, q)
    return root  # Split point found
```

**Iterative (O(1) space):**
```python
def lowestCommonAncestor(root, p, q):
    node = root
    while node:
        if p.val < node.val and q.val < node.val:
            node = node.left
        elif p.val > node.val and q.val > node.val:
            node = node.right
        else:
            return node
```

---

## Complexity

| Approach | Time | Space |
|---|---|---|
| Recursive | O(h) | O(h) call stack |
| Iterative | O(h) | O(1) |

For a balanced BST, h = O(log n). For a skewed BST, h = O(n).

---

## Common Interview Mistakes

1. **Using the general binary tree LCA approach.** It works but ignores the BST structure. Interviewers view this as a missed optimization.

2. **Not handling the case where `p` or `q` equals the current node.** The `else` branch handles this correctly since if `p.val == root.val`, neither condition is true.

3. **Not knowing the difference between LCA of BST (#235) and LCA of binary tree (#236).** The BST version is O(h); the general version is O(n). Being able to state this distinction shows depth.

4. **Forgetting that the iterative version is O(1) space.** Always mention this as an advantage over the recursive version.

---

## Resources

- **Full Walkthrough**: [Lowest Common Ancestor of a Binary Search Tree: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/lowest-common-ancestor-of-a-binary-search-tree-interview-walkthrough/)
- **Practice**: [Mock interview for Lowest Common Ancestor of a Binary Search Tree](https://intervu.dev/setup2?problem=lowest-common-ancestor-of-a-binary-search-tree)
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
- [Maximum Depth of Binary Tree](maximum-depth-of-binary-tree.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/maximum-depth-of-binary-tree-interview-walkthrough/)
- [Validate Binary Search Tree](validate-binary-search-tree.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/validate-binary-search-tree-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
