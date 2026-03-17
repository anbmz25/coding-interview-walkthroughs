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

- [Contains Duplicate](contains-duplicate.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/contains-duplicate-interview-walkthrough/)
- [Majority Element](majority-element.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/majority-element-interview-walkthrough/)
- [Partition Equal Subset Sum](partition-equal-subset-sum.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/partition-equal-subset-sum-interview-walkthrough/)
- [Valid Anagram](valid-anagram.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/valid-anagram-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
