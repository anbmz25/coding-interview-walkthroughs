# Find Median from Data Stream

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/find-median-from-data-stream-interview-walkthrough/)*

> A step-by-step walkthrough of the Find Median from Data Stream problem as it unfolds in a real coding interview. Learn the two-heap approach, the rebalancing invariant, and how to simulate a max-heap in Python.

**Difficulty**: Hard
**Patterns**: `heap`, `design`, `find-median-from-data-stream`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/find-median-from-data-stream-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=find-median-from-data-stream)**

---

## Problem

Implement a `MedianFinder` class:
- `addNum(num: int)` adds a number from the data stream.
- `findMedian() -> float` returns the median of all added numbers.

If the count of numbers is even, the median is the average of the two middle values. ([LeetCode #295](https://leetcode.com/problems/find-median-from-data-stream/))

### Example

```
medianFinder.addNum(1)    # stream: [1]
medianFinder.addNum(2)    # stream: [1, 2]
medianFinder.findMedian() # returns 1.5
medianFinder.addNum(3)    # stream: [1, 2, 3]
medianFinder.findMedian() # returns 2.0
```

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=find-median-from-data-stream)*

---

## Solution

```python
import heapq

class MedianFinder:
    def __init__(self):
        self.lo = []  # max-heap (negate values)
        self.hi = []  # min-heap

    def addNum(self, num: int) -> None:
        # Push to lo (max-heap via negation)
        heapq.heappush(self.lo, -num)
        # Balance: lo's max must be <= hi's min
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        # Keep lo size >= hi size
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        return (-self.lo[0] + self.hi[0]) / 2.0
```

Why this is interview-friendly:

- **Three heap operations per `addNum`.** Push to lo, pop-push to hi, conditional pop-push back. Each is O(log n). Clean and deterministic.
- **Negation handles max-heap.** Python's `heapq` is min-heap only. Storing `-num` in `lo` simulates a max-heap. Access the max via `-lo[0]`.
- **No size tracking variables.** `len(lo)` and `len(hi)` give sizes directly. No separate counter to maintain.

---

## Complexity

| | Time | Space |
|---|---|---|
| `addNum` | O(log n) | O(n) total |
| `findMedian` | O(1) | O(1) |

Each insertion does at most 3 heap operations (push, pop, push). Median is a constant-time peek at heap tops.

A common follow-up: "Can you do better?" For arbitrary streaming data, O(log n) insertion with O(1) median is optimal. With bounded integer ranges, a Fenwick tree or bucket sort could achieve O(log range) for both operations.

---

## Common Interview Mistakes

1. **Forgetting to negate for max-heap.** Python's `heapq` is a min-heap. Push `-num` to `lo` and use `-lo[0]` to read the max. Forgetting one negation produces wrong results silently.

2. **Not rebalancing after insertion.** Without rebalancing, sizes can drift and the median formula breaks. Always ensure `len(lo) >= len(hi)` and `len(lo) - len(hi) <= 1`.

3. **Sorting on each `findMedian` call.** O(n log n) per query defeats the purpose. The two-heap approach reduces `findMedian` to O(1).

4. **Off-by-one in the median formula.** When sizes are equal (even count): average the two tops. When `lo` has one more (odd count): return `lo`'s top. Getting this backwards returns the wrong value.

5. **Routing directly to `hi` first.** The pattern must route through `lo` first to maintain the ordering invariant. Routing to `hi` first can violate the property that all elements in `lo` are less than or equal to all elements in `hi`.

---

## Resources

- **Full Walkthrough**: [Find Median from Data Stream: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/find-median-from-data-stream-interview-walkthrough/)
- **Practice**: [Mock interview for Find Median from Data Stream](https://intervu.dev/setup2?problem=find-median-from-data-stream)
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
