# Longest Palindrome

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/longest-palindrome-interview-walkthrough/)*

> Master Longest Palindrome for your coding interview. Learn the pairs-plus-center greedy pattern, frequency counting, and what interviewers actually evaluate.

**Difficulty**: Easy
**Patterns**: `hash-map`, `string`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/longest-palindrome-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=longest-palindrome)**

---

## Problem

Given a string `s`, return the length of the longest palindrome that can be built with its characters. Letters are case-sensitive.

### Example

**Input:** `s = "abccccdd"`
**Output:** `7`, one longest palindrome is `"dccaccd"` (2 d's, 4 c's, 1 a).

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=longest-palindrome)*

---

## Solution

```python
from collections import Counter

def longestPalindrome(s: str) -> int:
    freq = Counter(s)
    length = 0
    has_odd = False

    for count in freq.values():
        length += count // 2 * 2
        if count % 2 == 1:
            has_odd = True

    return length + (1 if has_odd else 0)
```

---

## Complexity

| Aspect | Complexity |
|---|---|
| Time | O(n) |
| Space | O(k), k unique characters |

---

## Common Interview Mistakes

1. **Confusing with Longest Palindromic Substring.** This builds a palindrome from characters; that finds one within a string.
2. **Forgetting case sensitivity.** `'A'` and `'a'` are separate entries.
3. **Not adding the center +1.** Forgetting the optional center gives `length - 1`.

---

## Resources

- **Full Walkthrough**: [Longest Palindrome: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/longest-palindrome-interview-walkthrough/)
- **Practice**: [Mock interview for Longest Palindrome](https://intervu.dev/setup2?problem=longest-palindrome)
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
- [Insert Interval](insert-interval.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/insert-interval-interview-walkthrough/)
- [K Closest Points to Origin](k-closest-points-to-origin.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/k-closest-points-to-origin-interview-walkthrough/)
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
