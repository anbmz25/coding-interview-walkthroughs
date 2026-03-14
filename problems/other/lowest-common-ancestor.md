# Lowest Common Ancestor of a Binary Tree

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/lowest-common-ancestor-interview-walkthrough/)*

> A step-by-step walkthrough of LeetCode #236 as it plays out in a real coding interview. Learn the single-pass postorder DFS approach, why BST solutions don't work here, and how to handle the self-ancestor edge case.

**Difficulty**: Medium
**Patterns**: `trees`, `recursion`, `dfs`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/lowest-common-ancestor-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=lowest-common-ancestor)**

---

## Problem

Given a binary tree and two nodes `p` and `q`, find their **lowest common ancestor (LCA)**.

The lowest common ancestor is defined as the deepest node in the tree that has both `p` and `q` as descendants (a node can be a descendant of itself).

([LeetCode #236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/))

### Example

**Input**
```
Tree:
        3
       / \
      5   1
     / \ / \
    6  2 0  8
      / \
     7   4

p = 5, q = 4
```

**Output**
`5`

**Explanation:** Node `5` is the LCA of nodes `5` and `4` because `5` is an ancestor of `4`, and `5` is a descendant of itself by definition. Another example: if `p = 5` and `q = 1`, the LCA would be `3` (the root).

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=lowest-common-ancestor-of-a-binary-tree)*

---

## Solution

```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Base case: fallen off the tree
        if root is None:
            return None

        # If the current node matches either target, it's a candidate for LCA
        if root == p or root == q:
            return root

        # Recursively search both subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both subtrees returned a match, current node is the LCA
        if left and right:
            return root

        # Otherwise, propagate whichever subtree found a match
        return left if left else right
```

**Why `root == p` and not `root.val == p.val`?** We compare node references (object identity), not values. The problem passes actual `TreeNode` objects.

---

## Complexity

| Aspect | Complexity | Explanation |
|---|---|---|
| Time | O(N) | Visit every node once in the worst case |
| Space (call stack) | O(H) | H = tree height. O(log N) balanced, O(N) skewed |

**Time:** Even if we find `p` early, we may still need to search the other subtree for `q`.

**Space:** No additional data structures. Space is purely from the recursion stack.

---

## Common Interview Mistakes

1. **Confusing BST LCA with general tree LCA.** BST LCA uses value comparisons (go left if both values are smaller). That approach does not work for a general binary tree. Always confirm the tree type.

2. **Returning early on the first match without considering the subtree.** Some candidates stop searching as soon as they find `p`. The algorithm handles this correctly because returning `p` naturally propagates the answer upward.

3. **Not handling the self-ancestor edge case.** "A node can be a descendant of itself" is explicitly stated. The solution handles this because we return the node as soon as we find it.

4. **Coding before clarifying.** Jumping into code without asking about BST vs. general tree is a common signal of poor interview habits.

5. **Not explaining the postorder nature of the traversal.** Interviewers love hearing "this is essentially a postorder DFS because we make decisions based on what our children return." Naming the pattern shows depth.

6. **Forgetting to return the result upward.** A common bug is finding the LCA but not propagating it correctly. Make sure `return root` in the "both sides non-null" case actually returns up the call stack.

7. **Using extra space unnecessarily.** Storing paths or using a hash map of ancestors works, but introducing O(N) extra space when O(H) is achievable costs points.

---

## Resources

- **Full Walkthrough**: [Lowest Common Ancestor of a Binary Tree: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/lowest-common-ancestor-interview-walkthrough/)
- **Practice**: [Mock interview for Lowest Common Ancestor of a Binary Tree](https://intervu.dev/setup2?problem=lowest-common-ancestor)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
