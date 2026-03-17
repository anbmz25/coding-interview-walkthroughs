# Longest Palindromic Substring

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/longest-palindromic-substring-interview-walkthrough/)*

> A step-by-step walkthrough of LeetCode #5 as it plays out in a real coding interview. Learn the expand-around-center technique, why brute force fails at scale, and the odd-vs-even center distinction that trips up most candidates.

**Difficulty**: Medium
**Patterns**: `strings`, `two-pointers`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/longest-palindromic-substring-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=longest-palindromic-substring)**

---

## Problem

Given a string `s`, return the longest substring of `s` that is a palindrome. A palindrome reads the same forwards and backwards. If there are multiple answers of the same maximum length, return any one of them.

([LeetCode #5](https://leetcode.com/problems/longest-palindromic-substring/))

### Example

**Input**
`s = "babad"`

**Output**
`"bab"` (or `"aba"`, both are valid)

**Explanation:** Both `"bab"` and `"aba"` are palindromic substrings of length 3. No substring of length 4 or 5 is a palindrome. Another example: for `s = "cbbd"`, the output is `"bb"`.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=longest-palindromic-substring)*

---

## Solution

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        best_start = 0
        best_len = 1

        def expand(left: int, right: int) -> None:
            nonlocal best_start, best_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # After loop, valid palindrome is s[left+1 : right]
            current_len = right - left - 1
            if current_len > best_len:
                best_len = current_len
                best_start = left + 1

        for i in range(len(s)):
            expand(i, i)       # Odd-length palindrome centered at i
            expand(i, i + 1)   # Even-length palindrome centered between i and i+1

        return s[best_start : best_start + best_len]
```

**Why `left + 1` and `right - left - 1`?** When the while loop exits, `s[left] != s[right]` (or we hit a boundary). The actual palindrome starts at `left + 1` and has length `right - left - 1`.

---

## Complexity

| Aspect | Complexity | Explanation |
|---|---|---|
| Time | O(n^2) | n centers, each expansion takes at most O(n) |
| Space | O(1) | Only a constant number of variables |

> **Bonus:** There's an O(n) algorithm called **Manacher's Algorithm**. Mentioning it shows algorithmic breadth, but implementing it under interview pressure is usually not expected.

---

## Common Interview Mistakes

1. **Forgetting even-length palindromes.** The single most common bug. Only expanding from single characters misses palindromes like `"abba"` or `"bb"`. Always handle both center types.

2. **Off-by-one errors in the expansion result.** When the loop exits, the pointers have gone one step too far. The palindrome is `s[left+1 : right]`, not `s[left : right+1]`.

3. **Coding O(n^3) brute force without acknowledging it.** Presenting brute force is fine as a starting point, but failing to recognize it won't scale is a red flag.

4. **Jumping into DP without knowing why.** Some candidates recall this is a "DP problem" and start drawing a 2D table without articulating the recurrence. The expand-around-center approach is simpler and just as optimal.

5. **Not explaining the two center types.** Saying "I expand from the center" without clarifying odd vs. even suggests shallow understanding.

6. **Mishandling empty string or single-character input.** A single character is always a palindrome of length 1. An empty string should return `""`.

---

## Resources

- **Full Walkthrough**: [Longest Palindromic Substring: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/longest-palindromic-substring-interview-walkthrough/)
- **Practice**: [Mock interview for Longest Palindromic Substring](https://intervu.dev/setup2?problem=longest-palindromic-substring)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Add Binary](add-binary.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/add-binary-interview-walkthrough/)
- [Longest Substring Without Repeating Characters](longest-substring-without-repeating-characters.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/longest-substring-without-repeating-characters-interview-walkthrough/)
- [Minimum Window Substring](minimum-window-substring.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/minimum-window-substring-interview-walkthrough/)
- [Valid Anagram](valid-anagram.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/valid-anagram-interview-walkthrough/)
- [Valid Palindrome](valid-palindrome.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/valid-palindrome-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
