# Meeting Rooms

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/meeting-rooms-interview-walkthrough/)*

> Master Meeting Rooms for your coding interview. Learn the sort-then-scan interval pattern, overlap detection, and what interviewers actually evaluate.

**Difficulty**: Easy
**Patterns**: `array`, `sorting`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/meeting-rooms-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=meeting-rooms)**

---

## Problem

Given an array of meeting time intervals `intervals` where `intervals[i] = [start_i, end_i]`, determine if a person can attend all meetings (i.e., no two intervals overlap).

### Example 1

**Input:** `intervals = [[0,30],[5,10],[15,20]]`
**Output:** `false`, `[0,30]` overlaps with both `[5,10]` and `[15,20]`.

### Example 2

**Input:** `intervals = [[7,10],[2,4]]`
**Output:** `true`, `[2,4]` ends before `[7,10]` starts.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=meeting-rooms)*

---

## Solution

```python
def canAttendMeetings(intervals: list[list[int]]) -> bool:
    intervals.sort(key=lambda x: x[0])  # Sort by start time

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False  # Current meeting starts before previous ends

    return True
```

**Edge cases handled:**
- Empty array: `range(1, 0)` is empty, returns `True`.
- Single meeting: same, `range(1, 1)` is empty, returns `True`.
- Touching intervals `[1,3],[3,5]`: `3 < 3` is False → no overlap. Adjust to `<=` if touching counts as overlap.

---

## Complexity

| Aspect | Complexity |
|---|---|
| Time | O(n log n), dominated by sort |
| Space | O(1) extra (in-place sort) |

---

## Common Interview Mistakes

1. **Using `<=` vs `<` without clarifying touching intervals.** `[1,3]` and `[3,5]`, is this an overlap? Always clarify and be consistent.

2. **Not sorting first.** Without sorting, you'd need to check all pairs: O(n²).

3. **Comparing wrong fields.** Compare `intervals[i][0]` (start) with `intervals[i-1][1]` (end), not start with start.

4. **Not connecting to Meeting Rooms II.** Interviewers often follow up with "how many rooms do you need?", knowing this uses a min-heap on end times shows depth.

---

## Resources

- **Full Walkthrough**: [Meeting Rooms: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/meeting-rooms-interview-walkthrough/)
- **Practice**: [Mock interview for Meeting Rooms](https://intervu.dev/setup2?problem=meeting-rooms)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Best Time to Buy and Sell Stock](best-time-to-buy-and-sell-stock.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/best-time-to-buy-and-sell-stock-interview-walkthrough/)
- [Container With Most Water](container-with-most-water.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/container-with-most-water-interview-walkthrough/)
- [Contains Duplicate](contains-duplicate.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/contains-duplicate-interview-walkthrough/)
- [Find All Anagrams in a String](find-all-anagrams-in-a-string.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/find-all-anagrams-in-a-string-interview-walkthrough/)
- [Insert Interval](insert-interval.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/insert-interval-interview-walkthrough/)
- [K Closest Points to Origin](k-closest-points-to-origin.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/k-closest-points-to-origin-interview-walkthrough/)
- [Longest Palindrome](longest-palindrome.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/longest-palindrome-interview-walkthrough/)
- [Majority Element](majority-element.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/majority-element-interview-walkthrough/)
- [Maximum Subarray](maximum-subarray.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/maximum-subarray-interview-walkthrough/)
- [Merge Intervals](merge-intervals.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/merge-intervals-interview-walkthrough/)
- [Product of Array Except Self](product-of-array-except-self.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/product-of-array-except-self-interview-walkthrough/)
- [Ransom Note](ransom-note.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/ransom-note-interview-walkthrough/)
- [Sort Colors](sort-colors.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/sort-colors-interview-walkthrough/)
- [Spiral Matrix](spiral-matrix.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/spiral-matrix-interview-walkthrough/)
- [3Sum](three-sum.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/three-sum-interview-walkthrough/)
- [Trapping Rain Water](trapping-rain-water.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/trapping-rain-water-interview-walkthrough/)
- [Two Sum](two-sum.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/two-sum-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
