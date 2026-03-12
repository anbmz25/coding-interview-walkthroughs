# Merge Intervals

> A step-by-step walkthrough of the Merge Intervals problem as it unfolds in a real coding interview. Learn the optimal approach, common mistakes, and how strong candidates communicate their solution.

**Difficulty**: Medium
**Patterns**: `arrays`, `sorting`, `merge-intervals`

📖 **[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/merge-intervals-interview-walkthrough/)**
🎙️ **[Practice in a mock interview →](https://intervu.dev/setup2?problem=merge-intervals)**

---

## Problem

Given an array of intervals where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input. ([LeetCode #56](https://leetcode.com/problems/merge-intervals/))

### Example

**Input**
```
intervals = [[1,3],[2,6],[8,10],[15,18]]
```

**Output**
```
[[1,6],[8,10],[15,18]]
```

**Explanation:** Intervals `[1,3]` and `[2,6]` overlap because 2 falls within `[1,3]`. They merge into `[1,6]`. The remaining intervals don't overlap with each other or with `[1,6]`, so they stay as-is.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=merge-intervals)*

---

## Solution

```python
from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []

    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]

        # Intervals overlap if current start <= last end
        if current[0] <= last[1]:
            # Extend the last interval's end if needed
            last[1] = max(last[1], current[1])
        else:
            # No overlap: start a new interval
            merged.append(current)

    return merged
```

**Why this is interview-friendly:**
- Variable names (`last`, `current`, `merged`) are descriptive and self-documenting.
- The logic is a flat loop with no nested loops, making it easy to trace.
- The `max(last[1], current[1])` handles the fully-nested case (e.g., `[1,10]` containing `[2,5]`) cleanly without a separate branch.

---

## Complexity

| Operation | Complexity |
|---|---|
| Sorting the intervals | O(n log n) |
| Single pass through the array | O(n) |
| **Overall** | **O(n log n)** |
| Space (result array) | O(n) |

The dominant cost is sorting. The merge pass itself is linear. This is optimal because you can't do better than O(n log n) when you have to inspect all n intervals.

---

## Common Interview Mistakes

- **Coding too early.** Jumping straight to implementation without sorting or thinking through the approach leads to messy, hard-to-fix solutions mid-interview.
- **Forgetting to sort.** This is the most common mistake. Without sorting, the greedy pass doesn't work.
- **Missing the nested interval case.** Using `last[1] = current[1]` instead of `last[1] = max(last[1], current[1])` will fail on inputs like `[[1,10],[2,5]]`.
- **Modifying the input array without checking.** Some interviewers will ask whether it's acceptable to sort in place. Clarify first.
- **Not explaining the greedy reasoning.** Arriving at the right code without explaining *why* it works is a missed opportunity to demonstrate depth.
- **Skipping the empty input check.** Always handle the edge case where `intervals = []`.

---

## Resources

- 📖 **Full Walkthrough**: [Merge Intervals: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/merge-intervals-interview-walkthrough/)
- 🎙️ **Practice**: [Mock interview for Merge Intervals](https://intervu.dev/setup2?problem=merge-intervals)
- 📚 [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- 📚 [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- 📚 [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
