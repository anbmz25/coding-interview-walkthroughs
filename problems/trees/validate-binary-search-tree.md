# Validate Binary Search Tree

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/validate-binary-search-tree-interview-walkthrough/)*

> A step-by-step walkthrough of LeetCode #98 as it plays out in a real coding interview. Learn the bounds-propagation technique, why the naive local-check approach fails, and the edge cases that catch even experienced candidates.

**Difficulty**: Medium
**Patterns**: `trees`, `binary-search-tree`, `recursion`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/validate-binary-search-tree-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=validate-binary-search-tree)**

---

## Problem

Given the root of a binary tree, determine whether it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with values **strictly less than** the node's value.
- The right subtree of a node contains only nodes with values **strictly greater than** the node's value.
- Both the left and right subtrees must also be valid BSTs.

([LeetCode #98](https://leetcode.com/problems/validate-binary-search-tree/))

### Example 1

**Input**
```
    2
   / \
  1   3
```
`root = [2, 1, 3]`

**Output**
`true`

### Example 2

**Input**
```
        10
       /  \
      5    15
     / \   / \
    3   7  6  20
```
`root = [10, 5, 15, 3, 7, 6, 20]`

**Output**
`false`

In Example 1, node `1` is to the left of `2` (less than) and node `3` is to the right (greater than), valid. In Example 2, the tree looks perfectly healthy at first glance. Every parent-child relationship checks out. Yet the tree is invalid: node `6` sits in the right subtree of `10`, which means it must be greater than `10`, but `6 < 10`. This is exactly the violation that trips most candidates up.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=validate-binary-search-tree)*

---

## Solution

```python
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: TreeNode) -> bool:
    def validate(node, min_val, max_val):
        # An empty subtree is always valid
        if not node:
            return True

        # This node's value must fall strictly within the inherited bounds
        if node.val <= min_val or node.val >= max_val:
            return False

        # Recurse: tighten the upper bound going left, lower bound going right
        left_valid = validate(node.left, min_val, node.val)
        right_valid = validate(node.right, node.val, max_val)

        return left_valid and right_valid

    return validate(root, -math.inf, math.inf)
```

Let's trace through Example 2 (`[10, 5, 15, 3, 7, 6, 20]`):

- `validate(10, -inf, +inf)` → `10` is in bounds ✓
  - `validate(5, -inf, 10)` → `5` is in bounds ✓
    - `validate(3, -inf, 5)` → `3` is in bounds ✓ → both children `None` → `True`
    - `validate(7, 5, 10)` → `7` is in bounds ✓ → both children `None` → `True`
  - `validate(15, 10, +inf)` → `15` is in bounds ✓
    - `validate(6, 10, 15)` → `6 <= 10` → **`False`** ✗

Notice that the violation isn't caught until we reach node `6`, three levels deep, and only because it inherited the lower bound of `10` from the root. A local parent-child check at node `6` would have seen `6 < 15` and passed it. The bounds approach catches what the naive approach misses.

### Bonus: In-Order Traversal Approach

```python
def is_valid_bst_inorder(root: TreeNode) -> bool:
    prev = [-math.inf]  # Use a list to allow mutation inside the nested function

    def inorder(node):
        if not node:
            return True
        if not inorder(node.left):
            return False
        # Each node visited in-order must be strictly greater than the previous
        if node.val <= prev[0]:
            return False
        prev[0] = node.val
        return inorder(node.right)

    return inorder(root)
```

Both approaches are O(n) time and O(h) space where `h` is the tree height. The bounds-propagation approach is generally preferred in interviews because it's easier to reason about and explain verbally.

---

## Complexity

| Aspect | Complexity | Explanation |
|---|---|---|
| Time | O(n) | Each node is visited exactly once |
| Space (best case) | O(log n) | Balanced tree: recursion depth equals tree height |
| Space (worst case) | O(n) | Skewed tree: recursion depth equals number of nodes |

**Time:** Every node is visited exactly once in a single DFS traversal.

**Space:** The space complexity is determined by the call stack depth, which equals the height of the tree. For a balanced BST, that's O(log n). For a degenerate tree (essentially a linked list), it degrades to O(n).

---

## Common Interview Mistakes

1. **The local-check trap.** Checking only parent-child relationships is the most common wrong answer for this problem. If you catch yourself writing this, stop, explain why it's insufficient, and pivot to the bounds approach. Catching your own mistake and correcting it clearly is actually impressive.

2. **Using `INT_MIN` and `INT_MAX` as initial bounds in statically typed languages.** In Java or C++, using `Integer.MIN_VALUE` as the initial lower bound fails when a node has exactly that value. Use `-infinity` (or `Long.MIN_VALUE` as a workaround). In Python, `math.inf` is always safe.

3. **Using `<=` vs `<` incorrectly.** BSTs require *strictly* less than and *strictly* greater than. Using `<` instead of `<=` in your bounds check allows equal values through, which is wrong for the standard definition. Get the comparison operators right.

4. **Forgetting that `None` nodes are valid.** Some candidates add `if not node: return False`, which would make every leaf invalid. An absent child means there's nothing to violate constraints: always return `True` for null nodes.

5. **Not explaining the approach before coding.** The bounds-propagation insight is genuinely non-obvious. Interviewers want to hear you articulate *why* local checks aren't enough and *what* you're passing down in the recursive calls before you start writing.

6. **Hardcoding bounds as `0` or arbitrary values.** Some candidates initialize with `min_val = 0` or `min_val = -1000`, forgetting that valid BST values can be negative or very large. Always use actual infinity.

7. **Confusing the in-order approach and forgetting to track the previous node correctly.** If you use the in-order traversal approach, you need a way to persist the `previous` value across recursive calls, either through a mutable container (list), a class variable, or by threading it through the return value. Forgetting this makes the approach silently incorrect.

---

## Resources

- **Full Walkthrough**: [Validate Binary Search Tree: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/validate-binary-search-tree-interview-walkthrough/)
- **Practice**: [Mock interview for Validate Binary Search Tree](https://intervu.dev/setup2?problem=validate-binary-search-tree)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Binary Tree Level Order Traversal](binary-tree-level-order-traversal.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/binary-tree-level-order-traversal-interview-walkthrough/)
- [Invert Binary Tree](invert-binary-tree.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/invert-binary-tree-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
