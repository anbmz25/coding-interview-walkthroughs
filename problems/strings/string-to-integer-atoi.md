# String to Integer (atoi)

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/string-to-integer-atoi-interview-walkthrough/)*

> A step-by-step walkthrough of the String to Integer (atoi) problem as it unfolds in a real coding interview. Learn to enumerate edge cases upfront, handle overflow clamping, and write a clean single-pass parser.

**Difficulty**: Medium
**Patterns**: `string`, `string-to-integer-atoi`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/string-to-integer-atoi-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=string-to-integer-atoi)**

---

## Problem

Implement `myAtoi(s: str) -> int` which converts a string to a 32-bit signed integer. The rules:
1. Skip leading whitespace.
2. Read an optional `+` or `-` sign.
3. Read digits until a non-digit character or end of string.
4. Clamp the result to the 32-bit signed integer range: `[-2^31, 2^31 - 1]`.
5. Return 0 if no valid conversion was possible.

([LeetCode #8](https://leetcode.com/problems/string-to-integer-atoi/))

### Example 1

**Input**
`s = "42"`

**Output**
`42`

### Example 2

**Input**
`s = "   -42"`

**Output**
`-42`

### Example 3

**Input**
`s = "4193 with words"`

**Output**
`4193`

### Example 4

**Input**
`s = "words and 987"`

**Output**
`0`

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=string-to-integer-atoi)*

---

## Solution

```python
def myAtoi(s: str) -> int:
    INT_MIN = -(2**31)
    INT_MAX = 2**31 - 1

    i = 0
    n = len(s)

    # Step 1: Skip leading whitespace
    while i < n and s[i] == ' ':
        i += 1

    # Step 2: Read optional sign
    sign = 1
    if i < n and s[i] in ('+', '-'):
        sign = -1 if s[i] == '-' else 1
        i += 1

    # Step 3: Read digits
    result = 0
    while i < n and s[i].isdigit():
        digit = int(s[i])
        result = result * 10 + digit
        i += 1

    # Step 4: Apply sign and clamp
    result *= sign
    return max(INT_MIN, min(INT_MAX, result))
```

Why this is interview-friendly:

- **Single pass, no extra data structures.** The index `i` advances through each phase (whitespace, sign, digits) exactly once.
- **Bounds checking on every access.** Each `while` loop checks `i < n` before accessing `s[i]`, preventing index-out-of-bounds errors.
- **Clamping is one line.** `max(INT_MIN, min(INT_MAX, result))` is clean and correct. No branching needed.

---

## Complexity

| | Time | Space |
|---|---|---|
| myAtoi | O(n) | O(1) |

Single pass through the string. No additional data structures.

---

## Common Interview Mistakes

1. **Stripping all whitespace with `s.strip()`.** Only leading whitespace is skipped. `strip()` also removes trailing whitespace, which isn't part of the spec. More importantly, it hides the manual parsing the interviewer wants to see.

2. **Not clamping overflow.** In Python, integers have arbitrary precision, so overflow doesn't happen naturally. You must explicitly clamp to `[-2^31, 2^31 - 1]`. Missing this is a silent correctness bug.

3. **Handling `+` sign.** Many candidates skip the `+` sign case. The problem specifies both `+` and `-` as valid. A `+` sign followed by digits is valid input.

4. **Not bounds-checking `i` in every while loop.** Each `while` loop must check `i < n` before accessing `s[i]`. Missing this causes an `IndexError` on empty strings or strings with only whitespace.

5. **Forgetting the default result is 0.** If no digits are read, return 0. Initializing `result = 0` handles this naturally, but candidates sometimes return `None` or raise an exception instead.

---

## Resources

- **Full Walkthrough**: [String to Integer (atoi): Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/string-to-integer-atoi-interview-walkthrough/)
- **Practice**: [Mock interview for String to Integer (atoi)](https://intervu.dev/setup2?problem=string-to-integer-atoi)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Add Binary](add-binary.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/add-binary-interview-walkthrough/)
- [Longest Palindromic Substring](longest-palindromic-substring.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/longest-palindromic-substring-interview-walkthrough/)
- [Longest Substring Without Repeating Characters](longest-substring-without-repeating-characters.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/longest-substring-without-repeating-characters-interview-walkthrough/)
- [Minimum Window Substring](minimum-window-substring.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/minimum-window-substring-interview-walkthrough/)
- [Valid Anagram](valid-anagram.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/valid-anagram-interview-walkthrough/)
- [Valid Palindrome](valid-palindrome.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/valid-palindrome-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
