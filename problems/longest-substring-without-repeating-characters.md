# Longest Substring Without Repeating Characters

> A step-by-step walkthrough of LeetCode #3 as it unfolds in a real coding interview. Learn the sliding window approach, the critical index-tracking guard, and how strong candidates communicate their solution.

**Difficulty**: Medium
**Patterns**: `sliding-window`, `strings`

📖 **[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/longest-substring-without-repeating-characters-interview-walkthrough/)**
🎙️ **[Practice in a mock interview →](https://intervu.dev/setup2?problem=longest-substring-without-repeating-characters)**

---

## Problem

Given a string `s`, find the length of the **longest substring** that contains no repeating characters. A substring is a contiguous sequence of characters within the string, not to be confused with a subsequence, which can skip characters. ([LeetCode #3](https://leetcode.com/problems/longest-substring-without-repeating-characters/))

### Example

**Input**
```
s = "abcabcbb"
```

**Output**
```
3
```

The longest substring without repeating characters is `"abc"`, which has length `3`. Note that `"abcabc"` doesn't qualify because `'a'`, `'b'`, and `'c'` each repeat. A second example: for `s = "bbbbb"`, every character is a repeat, so the answer is `1` (any single character). For `s = "pwwkew"`, the answer is `3`, the substring `"wke"`.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=longest-substring-without-repeating-characters)*

---

## Solution

```python
def lengthOfLongestSubstring(s: str) -> int:
    char_index = {}  # Maps character -> its most recent index in s
    max_length = 0
    left = 0         # Left boundary of the current window

    for right in range(len(s)):
        char = s[right]

        # If char is in our window (not just in the map), shrink from the left
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1  # Jump past the previous occurrence

        # Always update to the latest index of this character
        char_index[char] = right

        # Update the longest valid window seen so far
        max_length = max(max_length, right - left + 1)

    return max_length
```

Style notes worth calling out in an interview:

- Storing the character's *index* (not just a boolean) is what enables the O(1) left-pointer jump. If you used a set, you'd need a while loop to shrink the window character by character. Still O(n) amortized, but less elegant and harder to explain.
- The guard `char_index[char] >= left` prevents moving the left pointer backward. This is the most commonly missed detail in implementations.
- `right - left + 1` is the current window size, a formula worth stating explicitly so the interviewer can follow your logic.
- Updating `char_index[char] = right` happens unconditionally, even when `char` isn't a duplicate. This ensures the map always reflects the freshest position.

---

## Complexity

| Operation | Complexity |
|---|---|
| Time | O(n) |
| Space | O(min(n, m)) |

**Time:** The `right` pointer traverses the string once from left to right, n steps total. The `left` pointer only ever moves forward and never exceeds `right`. Every character is "entered" into the window once and "exited" at most once. Each hash map operation is O(1). Total: O(n).

**Space:** The hash map stores at most one entry per unique character in the string. That's bounded by `min(n, m)` where `m` is the size of the character set (128 for ASCII, 26 for lowercase letters). In the worst case (all unique characters) the map grows to O(n).

This is a common interview follow-up: *"Can you reduce space further?"* For lowercase letters only, you could use a fixed-size array of 26 instead of a hash map, O(1) space relative to input size, though still O(m) in absolute terms.

---

## Common Interview Mistakes

1. **Using a set instead of a hash map.** A set tells you *if* a character is in the window but not *where* it last appeared. With a set, you'd need a while loop to shrink the window one character at a time. Correct, but slower to write and explain. The index-storing hash map is cleaner and more impressive.

2. **Forgetting the `char_index[char] >= left` guard.** Without this check, a character that appeared before the current window would incorrectly push `left` backward, breaking the window invariant. This is the single most common subtle bug in this problem.

3. **Not updating `char_index` after moving `left`.** The map must always reflect the most recent index of every character. Skipping the update causes stale indices and wrong left-pointer jumps on subsequent iterations.

4. **Computing window size as `right - left` instead of `right - left + 1`.** Off-by-one. A window where `left == right` contains one character, so its length is `1`, not `0`.

5. **Not handling the empty string.** If `s = ""`, the loop never executes and `max_length` stays `0`, which is correct. But it's worth verifying this edge case explicitly in your head (or out loud) before submitting.

6. **Coding the sliding window before explaining it.** The window contraction logic is non-obvious enough that writing it silently looks like guesswork. Always say *"when I hit a duplicate, I'll advance left past its previous occurrence"* before your fingers touch the keyboard.

7. **Confusing substring with subsequence.** A substring must be contiguous. Candidates who've been thinking about subsequence problems sometimes blur this line. Confirming "contiguous characters" early prevents building the wrong solution entirely.

---

## Resources

- 📖 **Full Walkthrough**: [Longest Substring Without Repeating Characters — Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/longest-substring-without-repeating-characters-interview-walkthrough/)
- 🎙️ **Practice**: [Mock interview for Longest Substring Without Repeating Characters](https://intervu.dev/setup2?problem=longest-substring-without-repeating-characters)
- 📚 [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- 📚 [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- 📚 [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev) — AI-powered mock interviews with instant feedback.*
