# Unique Paths

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/unique-paths-interview-walkthrough/)*

> Master Unique Paths for your coding interview. Learn the 2D DP recurrence, 1D space optimization, the combinatorics shortcut, and what interviewers actually evaluate.

**Difficulty**: Medium
**Patterns**: `dynamic-programming`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/unique-paths-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=unique-paths)**

---

## Problem

There is a robot on an `m x n` grid. It can only move right or down. Return the number of unique paths from the top-left to the bottom-right corner.

### Example

**Input:** `m = 3, n = 7`
**Output:** `28`

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=unique-paths)*

---

## Solution

**1D DP (space-optimized):**
```python
def uniquePaths(m: int, n: int) -> int:
    dp = [1] * n
    for _ in range(1, m):
        for c in range(1, n):
            dp[c] += dp[c-1]
    return dp[n-1]
```

**Combinatorics (O(1) space):**
```python
from math import comb

def uniquePaths(m: int, n: int) -> int:
    return comb(m + n - 2, m - 1)
```

---

## Complexity

| Approach | Time | Space |
|---|---|---|
| 1D DP | O(m × n) | O(n) |
| Combinatorics | O(min(m,n)) | O(1) |

---

## Common Interview Mistakes

1. **Forgetting base cases.** First row and column are all 1s, only one way to reach any edge cell.
2. **Not knowing the combinatorics formula.** Mentioning `C(m+n-2, m-1)` even if you implement DP is a strong signal.
3. **Confusing m and n.** Keep row/column indexing consistent.

---

## Resources

- **Full Walkthrough**: [Unique Paths: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/unique-paths-interview-walkthrough/)
- **Practice**: [Mock interview for Unique Paths](https://intervu.dev/setup2?problem=unique-paths)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Climbing Stairs](climbing-stairs.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/climbing-stairs-interview-walkthrough/)
- [Coin Change](coin-change.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/coin-change-interview-walkthrough/)
- [Partition Equal Subset Sum](partition-equal-subset-sum.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/partition-equal-subset-sum-interview-walkthrough/)
- [Word Break](word-break.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/word-break-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
