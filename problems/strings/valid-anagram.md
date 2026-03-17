# Valid Anagram

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/valid-anagram-interview-walkthrough/)*

> How to solve Valid Anagram (LeetCode #242) in a coding interview. Covers frequency counting vs. sorting, the Unicode follow-up, edge cases, and what strong candidates say to stand out.

**Difficulty**: Easy
**Patterns**: `strings`, `hash-map`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/valid-anagram-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=valid-anagram)**

---

## Problem

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise. An anagram is a word or phrase formed by rearranging the letters of another, using all the original letters exactly once.

([LeetCode #242](https://leetcode.com/problems/valid-anagram/))

### Example 1

**Input**
`s = "anagram", t = "nagaram"`

**Output**
`true`

### Example 2

**Input**
`s = "rat", t = "car"`

**Output**
`false`

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=valid-anagram)*

---

## Solution

```python
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = [0] * 26  # One slot per lowercase letter

    for c in s:
        count[ord(c) - ord('a')] += 1
    for c in t:
        count[ord(c) - ord('a')] -= 1

    return all(x == 0 for x in count)
```

**Alternative using Counter (more Pythonic, same complexity):**

```python
from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
```

The `Counter` approach is cleaner and handles Unicode naturally. The array approach is slightly faster in practice due to lower overhead.

---

## Complexity

| Aspect | Complexity | Explanation |
|---|---|---|
| Time | O(n) | Single pass through each string |
| Space | O(1) | Fixed-size 26-element array (or O(k) for Unicode with k unique chars) |

---

## Common Interview Mistakes

1. **Not checking lengths first.** Skipping the early `len(s) != len(t)` check is a missed optimization and potential source of incorrect results.

2. **Using sort when frequency counting is available.** Sorting is O(n log n) and is a red flag if the interviewer expects optimal solutions.

3. **Forgetting the Unicode follow-up.** If asked "what if the strings contain Unicode?", the fix is switching from a 26-element array to a `Counter` (dictionary). Have this answer ready.

4. **Using a set instead of a counter.** A set only tracks presence, not frequency. `"aab"` and `"abb"` would incorrectly return `true`.

5. **Not explaining the approach before coding.** Anagram is fast to code, resist the urge to just type. One sentence of narration shows communication skills.

---

## Resources

- **Full Walkthrough**: [Valid Anagram: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/valid-anagram-interview-walkthrough/)
- **Practice**: [Mock interview for Valid Anagram](https://intervu.dev/setup2?problem=valid-anagram)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Add Binary](add-binary.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/add-binary-interview-walkthrough/)
- [Longest Palindromic Substring](longest-palindromic-substring.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/longest-palindromic-substring-interview-walkthrough/)
- [Longest Substring Without Repeating Characters](longest-substring-without-repeating-characters.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/longest-substring-without-repeating-characters-interview-walkthrough/)
- [Minimum Window Substring](minimum-window-substring.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/minimum-window-substring-interview-walkthrough/)
- [Valid Palindrome](valid-palindrome.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/valid-palindrome-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
