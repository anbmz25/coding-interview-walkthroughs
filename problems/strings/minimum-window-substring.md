# Minimum Window Substring

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/minimum-window-substring-interview-walkthrough/)*

> A step-by-step walkthrough of LeetCode #76 as it plays out in a real coding interview. Learn the two-phase sliding window, the formed counter that makes validity O(1), and the frequency map design that handles duplicate characters correctly.

**Difficulty**: Hard
**Patterns**: `sliding-window`, `strings`, `hash-map`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/minimum-window-substring-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=minimum-window-substring)**

---

## Problem

Given two strings `s` and `t`, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If no such window exists, return `""`.

([LeetCode #76](https://leetcode.com/problems/minimum-window-substring/))

### Example 1

**Input**
`s = "ADOBECODEBANC", t = "ABC"`

**Output**
`"BANC"`

### Example 2

**Input**
`s = "a", t = "a"`

**Output**
`"a"`

### Example 3

**Input**
`s = "a", t = "b"`

**Output**
`""`

In Example 1, the shortest window containing A, B, and C is `"BANC"` (length 4). The key challenge: `t` can contain duplicate characters. `t = "AA"` requires the window to contain at least two `A`s.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=minimum-window-substring)*

---

## Solution

```python
from collections import Counter

def min_window(s: str, t: str) -> str:
    if not s or not t:
        return ""

    need = Counter(t)
    required = len(need)

    window_counts = {}
    formed = 0

    left = 0
    best = float("inf"), 0, 0

    for right in range(len(s)):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1

        if char in need and window_counts[char] == need[char]:
            formed += 1

        while formed == required and left <= right:
            if right - left + 1 < best[0]:
                best = (right - left + 1, left, right)

            left_char = s[left]
            window_counts[left_char] -= 1

            if left_char in need and window_counts[left_char] < need[left_char]:
                formed -= 1

            left += 1

    return "" if best[0] == float("inf") else s[best[1]: best[2] + 1]
```

For `s = "ADOBECODEBANC"`, `t = "ABC"`:

1. Expand right to index 5 (`C`): window = `"ADOBEC"`, formed = 3
2. Shrink: remove `A`, formed = 2. Best so far = `"ADOBEC"` (len 6)
3. Expand to index 10 (`A`): formed = 3 again
4. Shrink through D, O, B: formed drops when removing B. Best = `"CODEBA"` (len 6) 
5. Expand to index 12 (`C`): formed = 3
6. Shrink through E, C, O, D, E: window = `"BANC"` (len 4). Best updated.

Result: `"BANC"` ✓

---

## Complexity

| Aspect | Complexity | Explanation |
|---|---|---|
| Time | O(n + m) | Each character added and removed at most once; building `need` costs O(m) |
| Space | O(m + k) | `need` stores m characters; `window_counts` stores at most k unique chars |

---

## Common Interview Mistakes

1. **Not tracking `formed`, re-checking validity from scratch.** Re-computing `all(window_counts[c] >= need[c] for c in need)` each step makes it O(n x m).

2. **Using a set instead of a counter for `t`.** Fails on duplicates. `t = "AA"` requires two `A`s.

3. **Decrementing `formed` too eagerly.** Only decrement when count drops *below* required, not on every decrease.

4. **Incrementing `formed` for characters not in `need`.** Track only characters in `t`.

5. **Off-by-one in the return slice.** `s[left:right + 1]` because Python slicing is exclusive on the right.

6. **Using `if` instead of `while` for the shrink phase.** The window must shrink as far as possible.

---

## Resources

- **Full Walkthrough**: [Minimum Window Substring: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/minimum-window-substring-interview-walkthrough/)
- **Practice**: [Mock interview for Minimum Window Substring](https://intervu.dev/setup2?problem=minimum-window-substring)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Add Binary](add-binary.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/add-binary-interview-walkthrough/)
- [Longest Palindromic Substring](longest-palindromic-substring.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/longest-palindromic-substring-interview-walkthrough/)
- [Longest Substring Without Repeating Characters](longest-substring-without-repeating-characters.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/longest-substring-without-repeating-characters-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
