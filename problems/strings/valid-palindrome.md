# Valid Palindrome

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/valid-palindrome-interview-walkthrough/)*

> Master Valid Palindrome for your coding interview. Learn the two-pointer approach, O(1) space optimization, common mistakes, and what interviewers actually evaluate.

**Difficulty**: Easy
**Patterns**: `string`, `two-pointers`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/valid-palindrome-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=valid-palindrome)**

---

## Problem

A phrase is a palindrome if, after converting all uppercase letters to lowercase and removing all non-alphanumeric characters, it reads the same forward and backward.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

### Example

**Input**
`s = "A man, a plan, a canal: Panama"`

**Output**
`true`

After cleaning: `"amanaplanacanalpanama"` reads the same forwards and backwards.

**Input**
`s = "race a car"`

**Output**
`false`

After cleaning: `"raceacar"` does not read the same in reverse.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=valid-palindrome)*

---

## Solution

```python
def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        # Skip non-alphanumeric characters from the left
        while left < right and not s[left].isalnum():
            left += 1

        # Skip non-alphanumeric characters from the right
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare the characters at both pointers (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
```

The guard `left < right` in both inner while loops prevents the pointers from crossing while skipping characters, an easy-to-miss edge case.

---

## Complexity

| Operation | Complexity |
|---|---|
| Scanning the string with two pointers | O(n) |
| `.isalnum()` and `.lower()` per character | O(1) |
| **Overall time** | **O(n)** |
| **Overall space** | **O(1)** |

Each character is visited at most once by either pointer. No extra data structures are created.

---

## Common Interview Mistakes

1. **Forgetting the `left < right` guard inside the inner while loops.** Without it, the pointers can cross when all remaining characters are non-alphanumeric, causing incorrect comparisons.

2. **Not lowercasing before comparing.** `'A' != 'a'` in Python. Easy to forget under pressure.

3. **Using `s.isalpha()` instead of `s.isalnum()`.** `isalpha()` excludes digits. The problem explicitly includes digits as valid alphanumeric characters.

4. **Treating the cleaned-string approach as wrong.** It's O(n) space but perfectly valid. Don't apologize for it. Present it, state the tradeoff, then offer to optimize if asked.

5. **Starting to code before clarifying the empty-string case.** Interviewers notice when candidates code first and discover edge cases last.

6. **Off-by-one errors in the pointer movement.** Forgetting `left += 1` and `right -= 1` at the end of the loop body causes an infinite loop.

---

## Resources

- **Full Walkthrough**: [Valid Palindrome: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/valid-palindrome-interview-walkthrough/)
- **Practice**: [Mock interview for Valid Palindrome](https://intervu.dev/setup2?problem=valid-palindrome)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Add Binary](add-binary.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/add-binary-interview-walkthrough/)
- [Longest Palindromic Substring](longest-palindromic-substring.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/longest-palindromic-substring-interview-walkthrough/)
- [Longest Substring Without Repeating Characters](longest-substring-without-repeating-characters.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/longest-substring-without-repeating-characters-interview-walkthrough/)
- [Minimum Window Substring](minimum-window-substring.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/minimum-window-substring-interview-walkthrough/)
- [String to Integer (atoi)](string-to-integer-atoi.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/string-to-integer-atoi-interview-walkthrough/)
- [Valid Anagram](valid-anagram.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/valid-anagram-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
