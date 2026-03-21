# Insert Interval

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/insert-interval-interview-walkthrough/)*

> Master Insert Interval for your coding interview. Learn the three-case linear scan, merge boundary conditions, and what interviewers actually evaluate.

**Difficulty**: Medium
**Patterns**: `arrays`, `intervals`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/insert-interval-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=insert-interval)**

---

## Problem

You are given an array of non-overlapping intervals `intervals` sorted in ascending order by start time, and a new interval `newInterval`. Insert `newInterval` into `intervals`, merging any overlapping intervals.

### Example

**Input:** `intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]`, `newInterval = [4,8]`
**Output:** `[[1,2],[3,10],[12,16]]`

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=insert-interval)*

---

## Solution

```python
def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    result = []
    i = 0
    n = len(intervals)

    # Add intervals that end before newInterval starts
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Merge overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(intervals[i][0], newInterval[0])
        newInterval[1] = max(intervals[i][1], newInterval[1])
        i += 1

    result.append(newInterval)

    # Add remaining intervals
    result.extend(intervals[i:])
    return result
```

---

## Complexity

| Aspect | Complexity |
|---|---|
| Time | O(n), single scan |
| Space | O(n), output list |

---

## Common Interview Mistakes

1. **Wrong overlap condition.** Use `<=` not `<`, adjacent intervals like `[1,3]` and `[3,5]` should merge.
2. **Forgetting to append merged interval.** Many candidates exit the merge loop and skip appending `newInterval`.
3. **Unnecessary sort.** Input is already sorted, sorting costs O(n log n) for no reason.

---

## Resources

- **Full Walkthrough**: [Insert Interval: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/insert-interval-interview-walkthrough/)
- **Practice**: [Mock interview for Insert Interval](https://intervu.dev/setup2?problem=insert-interval)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Best Time to Buy and Sell Stock](best-time-to-buy-and-sell-stock.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/best-time-to-buy-and-sell-stock-interview-walkthrough/)
- [Container With Most Water](container-with-most-water.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/container-with-most-water-interview-walkthrough/)
- [Contains Duplicate](contains-duplicate.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/contains-duplicate-interview-walkthrough/)
- [Find All Anagrams in a String](find-all-anagrams-in-a-string.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/find-all-anagrams-in-a-string-interview-walkthrough/)
- [Find Median from Data Stream](find-median-from-data-stream.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/find-median-from-data-stream-interview-walkthrough/)
- [K Closest Points to Origin](k-closest-points-to-origin.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/k-closest-points-to-origin-interview-walkthrough/)
- [Longest Palindrome](longest-palindrome.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/longest-palindrome-interview-walkthrough/)
- [Majority Element](majority-element.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/majority-element-interview-walkthrough/)
- [Maximum Subarray](maximum-subarray.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/maximum-subarray-interview-walkthrough/)
- [Meeting Rooms](meeting-rooms.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/meeting-rooms-interview-walkthrough/)
- [Merge Intervals](merge-intervals.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/merge-intervals-interview-walkthrough/)
- [Product of Array Except Self](product-of-array-except-self.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/product-of-array-except-self-interview-walkthrough/)
- [Ransom Note](ransom-note.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/ransom-note-interview-walkthrough/)
- [Sort Colors](sort-colors.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/sort-colors-interview-walkthrough/)
- [Spiral Matrix](spiral-matrix.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/spiral-matrix-interview-walkthrough/)
- [Task Scheduler](task-scheduler.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/task-scheduler-interview-walkthrough/)
- [3Sum](three-sum.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/three-sum-interview-walkthrough/)
- [Trapping Rain Water](trapping-rain-water.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/trapping-rain-water-interview-walkthrough/)
- [Two Sum](two-sum.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/two-sum-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
