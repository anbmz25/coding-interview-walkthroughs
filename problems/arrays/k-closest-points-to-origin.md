# K Closest Points to Origin

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/k-closest-points-to-origin-interview-walkthrough/)*

> Master K Closest Points to Origin for your coding interview. Learn the max-heap approach, Quickselect, why sqrt is unnecessary, and what interviewers actually evaluate.

**Difficulty**: Medium
**Patterns**: `heap`, `sorting`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/k-closest-points-to-origin-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=k-closest-points-to-origin)**

---

## Problem

Given an array of `points` where `points[i] = [xi, yi]`, return the `k` closest to the origin `(0, 0)`. Return the answer in any order.

### Example

**Input:** `points = [[3,3],[5,-1],[-2,4]]`, `k = 2`
**Output:** `[[3,3],[-2,4]]`

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=k-closest-points-to-origin)*

---

## Solution

**Max-heap of size k:**
```python
import heapq

def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    max_heap = []
    for x, y in points:
        dist = x**2 + y**2
        heapq.heappush(max_heap, (-dist, x, y))
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    return [[x, y] for _, x, y in max_heap]
```

---

## Complexity

| Approach | Time | Space |
|---|---|---|
| Sort | O(n log n) | O(1) |
| Max-heap of k | O(n log k) | O(k) |
| Quickselect | O(n) expected | O(1) |

---

## Common Interview Mistakes

1. **Using `sqrt`.** Unnecessary, compare `x² + y²` directly.
2. **Not knowing `heapq` is min-heap.** Negate the key for max-heap behavior.
3. **Proposing Quickselect without O(n²) caveat.** Mention randomized pivoting mitigates worst case.

---

## Resources

- **Full Walkthrough**: [K Closest Points to Origin: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/k-closest-points-to-origin-interview-walkthrough/)
- **Practice**: [Mock interview for K Closest Points to Origin](https://intervu.dev/setup2?problem=k-closest-points-to-origin)
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
- [Longest Palindrome](longest-palindrome.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/longest-palindrome-interview-walkthrough/)
- [Majority Element](majority-element.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/majority-element-interview-walkthrough/)
- [Maximum Subarray](maximum-subarray.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/maximum-subarray-interview-walkthrough/)
- [Meeting Rooms](meeting-rooms.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/meeting-rooms-interview-walkthrough/)
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
