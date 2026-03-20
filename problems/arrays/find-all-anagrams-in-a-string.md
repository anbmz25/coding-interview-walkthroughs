# Find All Anagrams in a String

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/find-all-anagrams-in-a-string-interview-walkthrough/)*

> Master Find All Anagrams in a String for your coding interview. Learn the fixed-size sliding window, the matches counter optimization, and what interviewers actually evaluate.

**Difficulty**: Medium
**Patterns**: `sliding-window`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/find-all-anagrams-in-a-string-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=find-all-anagrams-in-a-string)**

---

## Problem

Given two strings `s` and `p`, return a list of all start indices of `p`'s anagrams in `s`.

### Example

**Input:** `s = "cbaebabacd"`, `p = "abc"`
**Output:** `[0, 6]`

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=find-all-anagrams-in-a-string)*

---

## Solution

```python
def findAnagrams(s: str, p: str) -> list[int]:
    if len(p) > len(s):
        return []

    p_count = [0] * 26
    s_count = [0] * 26

    for c in p:
        p_count[ord(c) - ord('a')] += 1
    for c in s[:len(p)]:
        s_count[ord(c) - ord('a')] += 1

    matches = sum(1 for i in range(26) if p_count[i] == s_count[i])
    result = [0] if matches == 26 else []

    for i in range(len(p), len(s)):
        incoming = ord(s[i]) - ord('a')
        outgoing = ord(s[i - len(p)]) - ord('a')

        s_count[incoming] += 1
        if s_count[incoming] == p_count[incoming]:
            matches += 1
        elif s_count[incoming] == p_count[incoming] + 1:
            matches -= 1

        s_count[outgoing] -= 1
        if s_count[outgoing] == p_count[outgoing]:
            matches += 1
        elif s_count[outgoing] == p_count[outgoing] - 1:
            matches -= 1

        if matches == 26:
            result.append(i - len(p) + 1)

    return result
```

---

## Complexity

| Aspect | Complexity |
|---|---|
| Time | O(n): O(1) per step |
| Space | O(1), two 26-element arrays |

---

## Common Interview Mistakes

1. **Recomputing frequency counts from scratch each window**: O(n × L) instead of O(n).
2. **Not deleting zero-count entries** in `Counter` comparisons, breaks equality.
3. **Off-by-one in start index.** Window ending at `i` starts at `i - len(p) + 1`.

---

## Resources

- **Full Walkthrough**: [Find All Anagrams in a String: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/find-all-anagrams-in-a-string-interview-walkthrough/)
- **Practice**: [Mock interview for Find All Anagrams in a String](https://intervu.dev/setup2?problem=find-all-anagrams-in-a-string)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Best Time to Buy and Sell Stock](best-time-to-buy-and-sell-stock.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/best-time-to-buy-and-sell-stock-interview-walkthrough/)
- [Container With Most Water](container-with-most-water.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/container-with-most-water-interview-walkthrough/)
- [Contains Duplicate](contains-duplicate.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/contains-duplicate-interview-walkthrough/)
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
- [3Sum](three-sum.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/three-sum-interview-walkthrough/)
- [Trapping Rain Water](trapping-rain-water.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/trapping-rain-water-interview-walkthrough/)
- [Two Sum](two-sum.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/two-sum-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
