# Binary Tree Right Side View

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/binary-tree-right-side-view-interview-walkthrough/)*

> How to solve Binary Tree Right Side View (LeetCode #199) in a coding interview using BFS level-order traversal. Includes both BFS and DFS approaches, complexity analysis, common mistakes, and interview dialogue.

**Difficulty**: Medium
**Patterns**: `binary-tree`, `bfs`, `dfs`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/binary-tree-right-side-view-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=binary-tree-right-side-view)**

---

## Problem

Given the `root` of a binary tree, imagine yourself standing on the right side of it. Return the values of the nodes you can see, ordered from top to bottom.

([LeetCode #199](https://leetcode.com/problems/binary-tree-right-side-view/))

### Example 1

**Input**
`root = [1,2,3,null,5,null,4]`

**Output**
`[1, 3, 4]`

### Example 2

**Input**
`root = [1,null,3]`

**Output**
`[1, 3]`

### Example 3

**Input**
`root = []`

**Output**
`[]`

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=binary-tree-right-side-view)*

---

## Solution

**BFS:**
```python
from collections import deque

def rightSideView(root) -> list[int]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == level_size - 1:
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result
```

**DFS (right subtree first):**
```python
def rightSideView_dfs(root) -> list[int]:
    result = []

    def dfs(node, depth: int) -> None:
        if not node:
            return
        if depth == len(result):
            result.append(node.val)  # first node seen at this depth = rightmost
        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)

    dfs(root, 0)
    return result
```

---

## Complexity

| | Time | Space |
|---|---|---|
| BFS | O(n) | O(n), queue holds one full level |
| DFS | O(n) | O(H), recursion stack |

---

## Common Interview Mistakes

1. **Only considering the right child.** A left subtree node is visible if it exists at a depth where the right subtree has no node. The BFS approach handles this automatically, whatever is last in the level queue is visible.

2. **Not grouping by level in BFS.** Enqueuing all nodes without level markers means you can't tell when a level ends. Capture `len(queue)` at the start of each iteration to know how many nodes belong to the current level.

3. **Null root.** Return `[]` immediately, don't proceed to BFS.

---

## Resources

- **Full Walkthrough**: [Binary Tree Right Side View: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/binary-tree-right-side-view-interview-walkthrough/)
- **Practice**: [Mock interview for Binary Tree Right Side View](https://intervu.dev/setup2?problem=binary-tree-right-side-view)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Balanced Binary Tree](balanced-binary-tree.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/balanced-binary-tree-interview-walkthrough/)
- [Binary Tree Level Order Traversal](binary-tree-level-order-traversal.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/binary-tree-level-order-traversal-interview-walkthrough/)
- [Construct Binary Tree from Preorder and Inorder Traversal](construct-binary-tree-from-preorder-and-inorder-traversal.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/construct-binary-tree-from-preorder-and-inorder-traversal-interview-walkthrough/)
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
