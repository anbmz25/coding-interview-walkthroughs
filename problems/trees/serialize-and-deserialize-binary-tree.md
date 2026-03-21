# Serialize and Deserialize Binary Tree

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/serialize-and-deserialize-binary-tree-interview-walkthrough/)*

> A step-by-step walkthrough of Serialize and Deserialize Binary Tree as it unfolds in a real coding interview. Learn both BFS and DFS approaches, how to encode null nodes, and why the DFS preorder solution is the cleanest interview implementation.

**Difficulty**: Hard
**Patterns**: `tree`, `design`, `serialize-and-deserialize-binary-tree`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/serialize-and-deserialize-binary-tree-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=serialize-and-deserialize-binary-tree)**

---

## Problem

Design a `Codec` class with:
- `serialize(root) -> str`: encodes a tree to a string.
- `deserialize(data: str) -> TreeNode`: decodes a string back to the original tree.

The encoding format is your choice. There's no right answer as long as serialization and deserialization are inverses of each other. ([LeetCode #297](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/))

### Example

**Input**
`root = [1,2,3,null,null,4,5]`

**Serialized**
`"1,2,null,null,3,4,null,null,5,null,null"` (DFS preorder with null markers)

**Deserialized**
Original tree reconstructed correctly.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=serialize-and-deserialize-binary-tree)*

---

## Solution


---

## Complexity

| | Time | Space |
|---|---|---|
| serialize | O(n) | O(n) |
| deserialize | O(n) | O(n) |

Every node is visited once. The serialized string and recursion stack (or queue) are both O(n).

---

## Common Interview Mistakes

1. **Not encoding nulls.** Without null markers, the tree can't be uniquely reconstructed. This is the single most important design decision.

2. **Choosing a delimiter that appears in values.** Node values can be negative, so `-` is a bad delimiter. Use `,` consistently.

3. **BFS deserialize index tracking.** Off-by-one in the token index is a common bug. Each dequeued node consumes exactly two tokens (left child, right child). Tracking `i` carefully is essential.

4. **Not handling the empty tree.** `serialize(None)` should return `"null"`, and `deserialize("null")` should return `None`. Missing this edge case is a silent bug.

5. **Using `split()` without considering empty tokens.** `"1,,2".split(",")` produces `["1", "", "2"]`. Ensure your serialization never produces consecutive delimiters.

---

## Resources

- **Full Walkthrough**: [Serialize and Deserialize Binary Tree: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/serialize-and-deserialize-binary-tree-interview-walkthrough/)
- **Practice**: [Mock interview for Serialize and Deserialize Binary Tree](https://intervu.dev/setup2?problem=serialize-and-deserialize-binary-tree)
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
- [Maximum Depth of Binary Tree](maximum-depth-of-binary-tree.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/maximum-depth-of-binary-tree-interview-walkthrough/)
- [Validate Binary Search Tree](validate-binary-search-tree.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/validate-binary-search-tree-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
