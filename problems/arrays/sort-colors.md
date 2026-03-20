# Sort Colors

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/sort-colors-interview-walkthrough/)*

> Master Sort Colors for your coding interview. Learn the Dutch National Flag algorithm, three-pointer invariants, and what interviewers actually evaluate.

**Difficulty**: Medium
**Patterns**: `arrays`, `two-pointers`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/sort-colors-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=sort-colors)**

---

## Problem

Given an array `nums` with objects colored red (0), white (1), or blue (2), sort them in place so same-colored objects are adjacent, in order 0, 1, 2.

### Example

**Input:** `nums = [2, 0, 2, 1, 1, 0]`
**Output:** `[0, 0, 1, 1, 2, 2]`

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=sort-colors)*

---

## Solution

```python
def sortColors(nums: list[int]) -> None:
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
            # Don't increment mid: swapped value needs examination
```

---

## Complexity

| Aspect | Complexity |
|---|---|
| Time | O(n), single pass |
| Space | O(1), in place |

---

## Common Interview Mistakes

1. **Incrementing `mid` after swapping with `high`.** The value from `high` is unseen, don't skip it.
2. **Using `mid < high` instead of `mid <= high`.** When equal, `nums[mid]` is still unsorted.
3. **Proposing a general sort.** Use the constrained value set, that's the point.

---

## Resources

- **Full Walkthrough**: [Sort Colors: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/sort-colors-interview-walkthrough/)
- **Practice**: [Mock interview for Sort Colors](https://intervu.dev/setup2?problem=sort-colors)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Best Time to Buy and Sell Stock](best-time-to-buy-and-sell-stock.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/best-time-to-buy-and-sell-stock-interview-walkthrough/)
- [Container With Most Water](container-with-most-water.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/container-with-most-water-interview-walkthrough/)
- [Contains Duplicate](contains-duplicate.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/contains-duplicate-interview-walkthrough/)
- [Insert Interval](insert-interval.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/insert-interval-interview-walkthrough/)
- [Longest Palindrome](longest-palindrome.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/longest-palindrome-interview-walkthrough/)
- [Majority Element](majority-element.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/majority-element-interview-walkthrough/)
- [Maximum Subarray](maximum-subarray.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/maximum-subarray-interview-walkthrough/)
- [Meeting Rooms](meeting-rooms.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/meeting-rooms-interview-walkthrough/)
- [Merge Intervals](merge-intervals.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/merge-intervals-interview-walkthrough/)
- [Product of Array Except Self](product-of-array-except-self.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/product-of-array-except-self-interview-walkthrough/)
- [Ransom Note](ransom-note.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/ransom-note-interview-walkthrough/)
- [3Sum](three-sum.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/three-sum-interview-walkthrough/)
- [Trapping Rain Water](trapping-rain-water.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/trapping-rain-water-interview-walkthrough/)
- [Two Sum](two-sum.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/two-sum-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
