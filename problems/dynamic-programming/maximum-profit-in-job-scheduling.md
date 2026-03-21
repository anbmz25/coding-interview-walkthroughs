# Maximum Profit in Job Scheduling

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/maximum-profit-in-job-scheduling-interview-walkthrough/)*

> A step-by-step walkthrough of the Maximum Profit in Job Scheduling problem as it unfolds in a real coding interview. Learn the DP + binary search approach, the sorting prerequisite, and how to implement the clean dp-array pattern.

**Difficulty**: Hard
**Patterns**: `dynamic-programming`, `binary-search`, `maximum-profit-in-job-scheduling`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/maximum-profit-in-job-scheduling-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=maximum-profit-in-job-scheduling)**

---

## Problem

You have `n` jobs. The `i`th job starts at `startTime[i]`, ends at `endTime[i]`, and pays `profit[i]`. Find the maximum profit you can achieve by scheduling non-overlapping jobs. ([LeetCode #1235](https://leetcode.com/problems/maximum-profit-in-job-scheduling/))

### Example 1

**Input**
`startTime = [1,2,3,3]`, `endTime = [3,4,5,6]`, `profit = [50,10,40,70]`

**Output**
`120`

Schedule jobs 1 and 4 (times [1,3] and [3,6], profits 50 + 70 = 120).

### Example 2

**Input**
`startTime = [1,2,3,4,6]`, `endTime = [3,5,10,6,9]`, `profit = [20,20,100,70,60]`

**Output**
`150`

Schedule jobs 1, 4, 5 (times [1,3], [4,6], [6,9], profits 20 + 70 + 60 = 150).

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=maximum-profit-in-job-scheduling)*

---

## Solution

```python
from bisect import bisect_right

def jobScheduling(startTime: list[int], endTime: list[int], profit: list[int]) -> int:
    jobs = sorted(zip(endTime, startTime, profit))
    # dp[i] = (end_time, max_profit): monotonically increasing in both dimensions
    dp = [(0, 0)]  # base case: 0 jobs, 0 profit

    for end, start, p in jobs:
        # Find latest job ending at or before `start`
        idx = bisect_right(dp, (start, float('inf'))) - 1
        best_with_job = dp[idx][1] + p

        if best_with_job > dp[-1][1]:
            dp.append((end, best_with_job))
        # else: skip (dp stays the same: only append if it improves)

    return dp[-1][1]
```

Why this is interview-friendly:

- **`bisect_right` with `(start, float('inf'))` finds the right insertion point.** Since `dp` stores `(end_time, profit)` tuples and `float('inf')` is larger than any profit, `bisect_right` returns the index after all entries with `end_time <= start`. Subtract 1 to get the latest compatible entry.
- **Monotonic dp array.** Only appending when profit improves keeps `dp` sorted in both dimensions, which is required for binary search to work.
- **No explicit skip tracking.** If the current job doesn't improve the best profit, we simply don't append. The last element of `dp` always holds the best achievable profit.

---

## Complexity

| | Time | Space |
|---|---|---|
| Maximum Profit in Job Scheduling | O(n log n) | O(n) |

Sorting is O(n log n). Each binary search is O(log n). The `dp` array has at most n entries.

---

## Common Interview Mistakes

1. **Not sorting by end time.** The DP recurrence requires jobs ordered by end time so "all previous jobs" means "all jobs with smaller end times." Sorting by start time doesn't give the right subproblem structure.

2. **Binary searching on the wrong field.** You need the latest job with `end_time <= start_time[current]`. The `dp` array stores `(end_time, profit)` tuples, and you search the `end_time` dimension.

3. **Forgetting the base case `(0, 0)`.** Without it, jobs with no compatible predecessors have no dp entry to fall back on. The base case represents "take no jobs, earn 0 profit."

4. **Appending every job to dp unconditionally.** Only append if the new profit exceeds the current maximum. `dp` must be monotonically increasing in profit for `bisect_right` to return correct results.

---

## Resources

- **Full Walkthrough**: [Maximum Profit in Job Scheduling: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/maximum-profit-in-job-scheduling-interview-walkthrough/)
- **Practice**: [Mock interview for Maximum Profit in Job Scheduling](https://intervu.dev/setup2?problem=maximum-profit-in-job-scheduling)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Climbing Stairs](climbing-stairs.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/climbing-stairs-interview-walkthrough/)
- [Coin Change](coin-change.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/coin-change-interview-walkthrough/)
- [Partition Equal Subset Sum](partition-equal-subset-sum.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/partition-equal-subset-sum-interview-walkthrough/)
- [Unique Paths](unique-paths.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/unique-paths-interview-walkthrough/)
- [Word Break](word-break.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/word-break-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
