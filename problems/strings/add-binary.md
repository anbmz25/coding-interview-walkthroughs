# Add Binary

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/add-binary-interview-walkthrough/)*

> A step-by-step walkthrough of the Add Binary problem as it unfolds in a real coding interview. Learn the right-to-left pointer technique, carry propagation, and how strong candidates handle unequal-length strings.

**Difficulty**: Easy
**Patterns**: `string`, `math`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/add-binary-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=add-binary)**

---

## Problem

Given two binary strings `a` and `b`, return their sum as a binary string. ([LeetCode #67](https://leetcode.com/problems/add-binary/))

### Example 1

**Input:** `a = "11"`, `b = "1"`
**Output:** `"100"`

### Example 2

**Input:** `a = "1010"`, `b = "1011"`
**Output:** `"10101"`

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=add-binary)*

---

## Solution

**Simulation approach:**
```python
def addBinary(a: str, b: str) -> str:
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry:
        digit_sum = carry
        if i >= 0:
            digit_sum += int(a[i])
            i -= 1
        if j >= 0:
            digit_sum += int(b[j])
            j -= 1

        result.append(str(digit_sum % 2))  # Current bit
        carry = digit_sum // 2             # New carry

    return ''.join(reversed(result))
```

**Pythonic shortcut (acceptable, but discuss trade-offs):**
```python
def addBinary(a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]
```

`int(a, 2)` converts a binary string to an integer, `bin()` converts back, and `[2:]` strips the `"0b"` prefix. Clean but uses built-in conversion. Ask the interviewer if this is acceptable.

---

## Complexity


---

## Common Interview Mistakes

- **Using `+` to build a string in a loop.** String concatenation in a loop is O(n²) in Python. Use a list and join at the end.

- **Forgetting the final carry.** If both strings are exhausted but `carry == 1`, you must append it. The `or carry` condition in the while loop handles this.

- **Reversing the input strings.** You can traverse from the end using indices. No need to reverse.

- **Not mentioning the built-in approach.** Show both and let the interviewer decide. If they want the simulation, the built-in shows you know the language.

---

## Resources

- **Full Walkthrough**: [Add Binary: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/add-binary-interview-walkthrough/)
- **Practice**: [Mock interview for Add Binary](https://intervu.dev/setup2?problem=add-binary)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Longest Palindromic Substring](longest-palindromic-substring.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/longest-palindromic-substring-interview-walkthrough/)
- [Longest Substring Without Repeating Characters](longest-substring-without-repeating-characters.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/longest-substring-without-repeating-characters-interview-walkthrough/)
- [Minimum Window Substring](minimum-window-substring.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/minimum-window-substring-interview-walkthrough/)
- [String to Integer (atoi)](string-to-integer-atoi.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/string-to-integer-atoi-interview-walkthrough/)
- [Valid Anagram](valid-anagram.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/valid-anagram-interview-walkthrough/)
- [Valid Palindrome](valid-palindrome.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/valid-palindrome-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
