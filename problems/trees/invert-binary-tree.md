# Invert Binary Tree

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/invert-binary-tree-interview-walkthrough/)*

> A step-by-step guide to solving Invert Binary Tree in a coding interview: recursive and iterative approaches, tree traversal reasoning, edge cases, and what strong candidates sound like.

**Difficulty**: Easy
**Patterns**: `trees`, `recursion`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/invert-binary-tree-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=invert-binary-tree)**

---

## Problem

Given the root of a binary tree, invert the tree (mirror it around its vertical center) and return the root. For every node, swap its left and right children. This applies recursively at every level. ([LeetCode #226](https://leetcode.com/problems/invert-binary-tree/))

### Example

**Input**
`root = [4,2,7,1,3,6,9]`

**Output**
`[4,7,2,9,6,3,1]`

The tree rooted at `4` has left child `2` (with children `1`, `3`) and right child `7` (with children `6`, `9`). After inversion, `4`'s children become `7` (left) and `2` (right). Recursively, every parent-child relationship is mirrored. A `None` input returns `None`.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=invert-binary-tree)*

---

## Solution

### Recursive: Clean and Concise (Recommended)

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: TreeNode) -> TreeNode:
    # Base case: empty tree is already inverted
    if root is None:
        return None

    # Swap left and right children at the current node
    root.left, root.right = root.right, root.left

    # Recursively invert both subtrees
    invertTree(root.left)
    invertTree(root.right)

    return root  # Return the same root: tree is modified in place
```

### Iterative BFS: Stack-Safe for Deep Trees

```python
from collections import deque

def invertTree(root: TreeNode) -> TreeNode:
    if root is None:
        return None

    queue = deque([root])

    while queue:
        node = queue.popleft()

        # Swap this node's children
        node.left, node.right = node.right, node.left

        # Enqueue children for processing (if they exist)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return root
```

Key implementation notes:

- **Python's tuple swap is atomic.** `root.left, root.right = root.right, root.left` fully evaluates the right side before assignment. No temp variable needed.
- **The recursive calls don't need to capture the return value.** The tree is modified in place.
- **The iterative approach avoids Python's recursion depth limit** (~1000). For a balanced tree of 100 nodes the depth is ~7, but for pathologically skewed trees, recursion could overflow.
- **For a balanced tree, recursive space O(log n) beats BFS space O(n).** Recursive isn't always worse on space.

---

## Complexity

| Approach | Time | Space |
|---|---|---|
| Recursive | O(n) | O(h) |
| Iterative BFS/DFS | O(n) | O(n) |

**Time:** Every node is visited exactly once. The swap is O(1). Total: O(n).

**Space (recursive):** Call stack depth equals tree height `h`. Balanced: O(log n). Skewed: O(n).

**Space (iterative):** Queue holds at most O(n) nodes. For a perfect binary tree, the last level alone contains n/2 nodes.

---

## Common Interview Mistakes

1. **Forgetting to return `root`.** The tree is inverted in place, but the return contract is broken if you forget `return root`. The caller gets `None`.

2. **Trying to invert without a base case.** Without `if root is None: return None`, the function raises `AttributeError` on `root.left`.

3. **Capturing recursive returns incorrectly.** Writing `root.left = invertTree(root.right)` without first preserving `root.left` produces incorrect results. Always swap pointers first, then recurse.

4. **Not mentioning the iterative alternative.** Presenting only recursion without acknowledging BFS signals incomplete thinking.

5. **Not explaining why traversal order doesn't matter.** Being able to say "correctness only requires every node gets its children swapped, regardless of visit order" demonstrates genuine understanding.

6. **Treating this as too trivial to explain.** The recursive solution is three lines. The explanation *is* the interview. Narrate the base case, the swap, and the recursion.

---

## Resources

- **Full Walkthrough**: [Invert Binary Tree: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/invert-binary-tree-interview-walkthrough/)
- **Practice**: [Mock interview for Invert Binary Tree](https://intervu.dev/setup2?problem=invert-binary-tree)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
