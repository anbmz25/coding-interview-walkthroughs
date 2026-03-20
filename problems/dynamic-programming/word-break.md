# Word Break

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/word-break-interview-walkthrough/)*

> A step-by-step walkthrough of LeetCode #139 as it plays out in a real coding interview. Learn the DP recurrence, why naive recursion explodes exponentially, and the base case that trips up most candidates.

**Difficulty**: Medium
**Patterns**: `dynamic-programming`, `strings`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/word-break-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=word-break)**

---

## Problem

Given a string `s` and a list of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words. The same word may be reused multiple times.

([LeetCode #139](https://leetcode.com/problems/word-break/))

### Example 1

**Input**
`s = "leetcode", wordDict = ["leet", "code"]`

**Output**
`true`

### Example 2

**Input**
`s = "applepenapple", wordDict = ["apple", "pen"]`

**Output**
`true`

### Example 3

**Input**
`s = "catsandog", wordDict = ["cats", "dog", "sand", "an", "cat"]`

**Output**
`false`

In Example 1, `"leetcode"` splits into `"leet"` + `"code"`. In Example 2, `"applepenapple"` splits into `"apple"` + `"pen"` + `"apple"`, reusing the same word. Example 3 is the instructive one: many partial matches lead deep into the string before hitting dead ends.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=word-break)*

---

## Solution

```python
def word_break(s: str, wordDict: list[str]) -> bool:
    word_set = set(wordDict)  # O(1) lookup instead of O(m) list scan
    n = len(s)

    # dp[i] = True means s[0:i] can be segmented using wordDict
    dp = [False] * (n + 1)
    dp[0] = True  # Empty prefix is always valid

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break  # No need to check other j values for this i

    return dp[n]
```

Let's trace `s = "leetcode"`, `wordDict = ["leet", "code"]`:

| i | substring checked | key check | dp[i] |
|---|---|---|---|
| 0 | `""` | base case | `True` |
| 1-3 | `"l"`, `"le"`, `"lee"` | no matches | `False` |
| 4 | `"leet"` | `dp[0]=True`, `"leet"` in set | `True` |
| 5-7 | `"leetc"`, `"leetco"`, `"leetcod"` | no word completes from `dp[4]` | `False` |
| 8 | `"leetcode"` | `dp[4]=True`, `"code"` in set | `True` |

`dp[8] = True`. Return `True`.

### Memoized Recursive Version

If you prefer top-down thinking:

```python
def word_break_memo(s: str, wordDict: list[str]) -> bool:
    word_set = set(wordDict)
    memo = {}

    def can_break(start: int) -> bool:
        if start == len(s):
            return True
        if start in memo:
            return memo[start]

        for end in range(start + 1, len(s) + 1):
            if s[start:end] in word_set and can_break(end):
                memo[start] = True
                return True

        memo[start] = False
        return False

    return can_break(0)
```

Both versions are O(n^2 x m) time and O(n) space.

---

## Complexity

| Aspect | Complexity | Explanation |
|---|---|---|
| Time | O(n^2 x m) | n^2 substrings checked, each hash comparison is O(m) for word length m |
| Space (DP array) | O(n) | One boolean per position in `s` |
| Space (word set) | O(W x m) | W words of average length m stored in the set |

In practice, you can tighten the inner loop: for each position `i`, only check substrings of length up to `max_word_len`. This reduces the constant factor meaningfully.

---

## Common Interview Mistakes

1. **Using a list for `wordDict` lookups instead of a set.** `s[j:i] in wordDict` where `wordDict` is a list costs O(W) per lookup. Converting to a set drops this to O(1) amortized.

2. **Initializing `dp[0] = False`.** `dp[0]` represents the empty prefix, which can always be segmented. Setting it to `False` means no position is ever reachable, and the entire table stays `False`.

3. **Off-by-one in the DP indices.** `dp` has length `n + 1`. `dp[i]` represents `s[0:i]`. The answer is `dp[n]`, not `dp[n-1]`.

4. **Forgetting the `break` after setting `dp[i] = True`.** Not breaking doesn't produce wrong answers, but it wastes work and signals you haven't thought about the inner loop's exit condition.

5. **Proposing pure recursion without flagging its time complexity.** The recursive approach is a natural starting point, but you should immediately explain why it's O(2^n) and pivot to DP. Presenting naive recursion as your final answer is a red flag.

6. **Not validating the recurrence on a small example.** The index arithmetic (`dp[j]`, `s[j:i]`, `dp[n]`) is easy to mess up. Tracing through `"leet" + "code"` takes 90 seconds and catches every off-by-one.

---

## Resources

- **Full Walkthrough**: [Word Break: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/word-break-interview-walkthrough/)
- **Practice**: [Mock interview for Word Break](https://intervu.dev/setup2?problem=word-break)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Climbing Stairs](climbing-stairs.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/climbing-stairs-interview-walkthrough/)
- [Coin Change](coin-change.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/coin-change-interview-walkthrough/)
- [Partition Equal Subset Sum](partition-equal-subset-sum.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/partition-equal-subset-sum-interview-walkthrough/)
- [Unique Paths](unique-paths.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/unique-paths-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
