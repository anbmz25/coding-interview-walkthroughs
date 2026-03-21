# Partition Equal Subset Sum

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/partition-equal-subset-sum-interview-walkthrough/)*

> How to solve Partition Equal Subset Sum (LeetCode #416) in a coding interview using 0/1 knapsack DP. Covers the key reduction, space-optimized 1D DP, reverse iteration insight, and common mistakes.

**Difficulty**: Medium
**Patterns**: `dynamic-programming`, `knapsack`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/partition-equal-subset-sum-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=partition-equal-subset-sum)**

---

## Problem

Given an integer array `nums`, return `true` if you can partition the array into two subsets such that the sum of elements in both subsets is equal, and `false` otherwise.

([LeetCode #416](https://leetcode.com/problems/partition-equal-subset-sum/))

### Example 1

**Input**
`nums = [1, 5, 11, 5]`

**Output**
`true`, partition into `[1, 5, 5]` and `[11]`

### Example 2

**Input**
`nums = [1, 2, 3, 5]`

**Output**
`false`, no valid partition

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=partition-equal-subset-sum)*

---

## Solution

**2D DP (easier to derive, then optimize):**
```python
def canPartition_2d(nums: list[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    n = len(nums)

    # dp[i][j] = True if first i elements can sum to j
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True  # empty subset always sums to 0

    for i in range(1, n + 1):
        num = nums[i - 1]
        for j in range(target + 1):
            dp[i][j] = dp[i - 1][j]  # don't include nums[i-1]
            if j >= num:
                dp[i][j] = dp[i][j] or dp[i - 1][j - num]  # include it

    return dp[n][target]
```

**1D DP (space-optimized, what you should write in an interview):**
```python
def canPartition(nums: list[int]) -> bool:
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2

    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for j in range(target, num - 1, -1):  # iterate in reverse
            dp[j] = dp[j] or dp[j - num]
        if dp[target]:  # early exit
            return True

    return dp[target]
```

---

## Complexity

| | Time | Space |
|---|---|---|
| 2D DP | O(n * target) | O(n * target) |
| 1D DP | O(n * target) | O(target) |

`target` is at most `sum(nums) / 2`. With constraints, this is at most 10,000.

---

## Common Interview Mistakes

1. **Iterating forward in the 1D DP.** If you iterate `j` from `num` to `target` (increasing), you can use `num` multiple times in the same pass: that models the unbounded knapsack, not 0/1 knapsack. Reverse iteration enforces each element is used at most once.

2. **Forgetting `dp[0] = True`.** The base case is that the empty subset has sum 0. Without this, no subset can ever be "built up" in the DP.

3. **Not handling odd totals early.** Always check `total % 2 != 0` before building the DP table. Saves unnecessary work and is a clear correctness check interviewers notice.

4. **Confusing subset sum with partition.** The partition constraint means you don't need to find which elements are in each half, just whether one subset summing to `target` exists. The other elements automatically form the complement.

---

## Resources

- **Full Walkthrough**: [Partition Equal Subset Sum: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/partition-equal-subset-sum-interview-walkthrough/)
- **Practice**: [Mock interview for Partition Equal Subset Sum](https://intervu.dev/setup2?problem=partition-equal-subset-sum)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Climbing Stairs](climbing-stairs.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/climbing-stairs-interview-walkthrough/)
- [Coin Change](coin-change.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/coin-change-interview-walkthrough/)
- [Maximum Profit in Job Scheduling](maximum-profit-in-job-scheduling.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/maximum-profit-in-job-scheduling-interview-walkthrough/)
- [Unique Paths](unique-paths.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/unique-paths-interview-walkthrough/)
- [Word Break](word-break.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/word-break-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
