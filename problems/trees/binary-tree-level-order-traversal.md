# Binary Tree Level Order Traversal

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/binary-tree-level-order-traversal-interview-walkthrough/)*

> A step-by-step guide to solving Binary Tree Level Order Traversal in a coding interview. Learn the BFS queue-snapshot pattern, common mistakes, and what interviewers actually score you on.

**Difficulty**: Medium
**Patterns**: `trees`, `bfs`, `grind-75`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/binary-tree-level-order-traversal-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=binary-tree-level-order-traversal)**

---

## Problem

Given the root of a binary tree, return the node values grouped by level, from top to bottom. Each level is its own list.

### Example

**Input**
```
      3
     / \
    9  20
   /  /  \
  4  15   7
```
`root = [3, 9, 20, 4, null, 15, 7]`

**Output**
`[[3], [9, 20], [4, 15, 7]]`

At depth 0, we have just `3`. At depth 1, `9` and `20`. At depth 2, `4`, `15`, and `7`. ([LeetCode #102](https://leetcode.com/problems/binary-tree-level-order-traversal/))

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=binary-tree-level-order-traversal)*

---

## Solution

```python
from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return [, "medium"]

        result = [, "medium"]
        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_level = [, "medium"]

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)

        return result
```

The use of `deque` is intentional. Python lists have O(n) `pop(0)` operations, making them unsuitable for queues. `deque.popleft()` is O(1) and keeps the overall complexity tight.

---

## Complexity

| Operation | Complexity |
|---|---|
| Visiting every node | O(n) |
| Enqueue / dequeue each node | O(1) per node, O(n) total |
| Building result lists | O(n) total across all levels |
| **Overall Time** | **O(n)** |
| **Overall Space** | **O(n)**, queue holds at most the widest level |

For a perfectly balanced binary tree, the last level contains n/2 nodes, all of which could be in the queue simultaneously. For a skewed tree (like a linked list), the queue never holds more than one node at a time.

---

## Common Interview Mistakes

1. **Using `list.pop(0)` instead of `deque.popleft()`** Python's `list.pop(0)` is O(n). On large inputs, this blows up your time complexity from O(n) to O(n²). Always use `collections.deque`.

2. **Forgetting to snapshot `len(queue)` before the inner loop** If you check `len(queue)` inside the loop, or don't capture it before enqueuing children, you'll accidentally process the next level's nodes in the current level's loop iteration.

3. **Not handling `root = None`** Accessing `root.val` on a null root crashes immediately. A single guard clause at the top fixes this.

4. **Coding before clarifying the output format** Some candidates build a flat list `[3, 9, 20, 4, 15, 7]` instead of `[[3], [9, 20], [4, 15, 7]]`. Confirm the output shape before you start.

5. **Using recursion and hitting stack limits** For a tree with 10^5 nodes in a skewed shape, DFS recursion will hit Python's default recursion depth limit. BFS with an explicit queue is safer.

6. **Starting to code immediately without explaining the approach** Interviewers want to follow your reasoning. Walk through your plan verbally before writing any code.

7. **Forgetting to check for `None` children before enqueuing** Always check `if node.left` before `queue.append(node.left)`. Enqueuing `None` into the queue will cause `NoneType` errors in the next iteration.

---

## Resources

- **Full Walkthrough**: [Binary Tree Level Order Traversal: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/binary-tree-level-order-traversal-interview-walkthrough/)
- **Practice**: [Mock interview for Binary Tree Level Order Traversal](https://intervu.dev/setup2?problem=binary-tree-level-order-traversal)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Balanced Binary Tree](balanced-binary-tree.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/balanced-binary-tree-interview-walkthrough/)
- [Binary Tree Right Side View](binary-tree-right-side-view.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/binary-tree-right-side-view-interview-walkthrough/)
- [Diameter of Binary Tree](diameter-of-binary-tree.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/diameter-of-binary-tree-interview-walkthrough/)
- [Invert Binary Tree](invert-binary-tree.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/invert-binary-tree-interview-walkthrough/)
- [Lowest Common Ancestor of a Binary Tree](lowest-common-ancestor.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/lowest-common-ancestor-interview-walkthrough/)
- [Lowest Common Ancestor of a Binary Search Tree](lowest-common-ancestor-of-a-binary-search-tree.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/lowest-common-ancestor-of-a-binary-search-tree-interview-walkthrough/)
- [Maximum Depth of Binary Tree](maximum-depth-of-binary-tree.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/maximum-depth-of-binary-tree-interview-walkthrough/)
- [Validate Binary Search Tree](validate-binary-search-tree.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/validate-binary-search-tree-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
