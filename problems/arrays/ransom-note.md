# Ransom Note

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/ransom-note-interview-walkthrough/)*

> Master Ransom Note for your coding interview. Learn character frequency counting, the 26-element array optimization, and what interviewers actually evaluate.

**Difficulty**: Easy
**Patterns**: `hash-map`, `string`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/ransom-note-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=ransom-note)**

---

## Problem

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine`, and `false` otherwise. Each letter in `magazine` can only be used once.

### Example

**Input:** `ransomNote = "aa"`, `magazine = "aab"`
**Output:** `true`

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=ransom-note)*

---

## Solution

```python
from collections import Counter

def canConstruct(ransomNote: str, magazine: str) -> bool:
    magazine_counts = Counter(magazine)

    for char in ransomNote:
        if magazine_counts[char] == 0:
            return False
        magazine_counts[char] -= 1

    return True
```

**26-element array variant** (avoids hash overhead):

```python
def canConstruct(ransomNote: str, magazine: str) -> bool:
    counts = [0] * 26

    for char in magazine:
        counts[ord(char) - ord('a')] += 1

    for char in ransomNote:
        idx = ord(char) - ord('a')
        counts[idx] -= 1
        if counts[idx] < 0:
            return False

    return True
```

---

## Complexity

| Aspect | Complexity |
|---|---|
| Time | O(n + m), one pass over each string |
| Space | O(1), at most 26 entries |

---

## Common Interview Mistakes

1. **Skipping the early-length check.** If `magazine` is shorter than `ransomNote`, return `false` immediately, don't build the map.

2. **Mutating the magazine string.** Removing matched characters from a string is O(n) per deletion, avoid.

3. **Not explaining the 26-element array optimization.** For lowercase-only inputs, a fixed-size array is O(1) space and avoids hashing overhead.

---

## Resources

- **Full Walkthrough**: [Ransom Note: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/ransom-note-interview-walkthrough/)
- **Practice**: [Mock interview for Ransom Note](https://intervu.dev/setup2?problem=ransom-note)
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
- [Sort Colors](sort-colors.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/sort-colors-interview-walkthrough/)
- [3Sum](three-sum.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/three-sum-interview-walkthrough/)
- [Trapping Rain Water](trapping-rain-water.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/trapping-rain-water-interview-walkthrough/)
- [Two Sum](two-sum.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/two-sum-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
