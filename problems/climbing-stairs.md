# Climbing Stairs

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/climbing-stairs-interview-walkthrough/)*

> A step-by-step walkthrough of the Climbing Stairs problem as it unfolds in a real coding interview. Learn the full recursion-to-DP progression, the Fibonacci connection, and how strong candidates communicate their optimization steps.

**Difficulty**: Medium
**Patterns**: `dynamic-programming`, `climbing-stairs`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/climbing-stairs-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=climbing-stairs)**

---

## Problem

You are climbing a staircase with `n` steps. Each time you can either climb **1 step** or **2 steps**. Return the number of distinct ways you can reach the top. ([LeetCode #70](https://leetcode.com/problems/climbing-stairs/))

### Example

**Input**
```
n = 5
```

**Output**
```
8
```

For `n = 3`, there are 3 ways: `{1,1,1}`, `{1,2}`, `{2,1}`. For `n = 5`, there are 8 ways. The pattern here is not coincidental: the answers follow the Fibonacci sequence (1, 1, 2, 3, 5, 8, 13...), a connection worth recognizing and mentioning in your interview.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=climbing-stairs)*

---

## Solution

```python
def climbStairs(n: int) -> int:
    # Base cases: only one way to climb 1 step, two ways to climb 2 steps
    if n == 1:
        return 1
    if n == 2:
        return 2

    # prev2 = ways(i-2), prev1 = ways(i-1)
    prev2, prev1 = 1, 2

    for i in range(3, n + 1):
        # Ways to reach step i = ways from step i-1 + ways from step i-2
        current = prev1 + prev2

        # Slide the window forward
        prev2 = prev1
        prev1 = current

    return prev1  # Now holds ways(n)
```

Style notes worth calling out in an interview:

- Handling `n == 1` and `n == 2` explicitly as base cases keeps the loop logic clean and avoids subtle off-by-one errors.
- Variable names `prev1` and `prev2` communicate their roles clearly. They represent `ways(i-1)` and `ways(i-2)` relative to the current iteration.
- The sliding window pattern (`prev2 = prev1`, `prev1 = current`) is a reusable idiom across many Fibonacci-style DP problems, worth naming explicitly.

For completeness, here's also the memoized version, which some interviewers prefer to see first as a stepping stone:

```python
from functools import lru_cache

def climbStairs(n: int) -> int:
    @lru_cache(maxsize=None)
    def ways(k):
        if k <= 1:
            return 1
        if k == 2:
            return 2
        return ways(k - 1) + ways(k - 2)

    return ways(n)
```

---

## Complexity

| Operation | Complexity |
|---|---|
| Time (naive recursion) | O(2ⁿ) |
| Time (memoized / bottom-up) | O(n) |
| Space (memoized) | O(n) |
| Space (bottom-up optimized) | O(1) |

**Time:** In the optimized solution, we make a single pass from step 3 to step `n`, exactly `n - 2` iterations, so O(n) overall.

**Space:** We store only two variables at any point, regardless of `n`. This is the key win over the memoization approach, and worth highlighting: *"I've reduced space from O(n) to O(1) by observing that the recurrence only looks back two steps."*

---

## Common Interview Mistakes

1. **Returning the wrong base case for `n = 1`.** Some candidates write `if n == 0: return 1` and `if n == 1: return 1`, which works but requires careful reasoning. Being explicit with `n == 1 → 1` and `n == 2 → 2` is cleaner and less error-prone.

2. **Off-by-one in the loop range.** Using `range(2, n)` instead of `range(3, n + 1)` shifts the entire iteration, producing wrong results. Always trace through a small example (`n = 4`) to verify your loop bounds.

3. **Presenting only the recursive solution without optimizing.** The naive recursion is the *starting point*, not the answer. Stopping there signals you don't know DP. Always drive toward memoization and then bottom-up.

4. **Not naming the Fibonacci connection.** Recognizing that the answer is the (n+1)th Fibonacci number is a signal of mathematical maturity. Not mentioning it when you clearly see it is a missed opportunity.

5. **Confusing `prev1` and `prev2` after the slide.** The update order matters: you must set `prev2 = prev1` *before* setting `prev1 = current`. Doing it in the wrong order overwrites a value you still need. Trace through once to confirm.

6. **Not explaining the recurrence before coding.** Candidates who write the loop without first saying *"to reach step n, I either came from n-1 or n-2, so ways(n) = ways(n-1) + ways(n-2)"* leave the interviewer guessing whether they understand the problem or just memorized the solution.

7. **Ignoring the space optimization.** Getting to a working O(n) space bottom-up DP is good. Getting to O(1) by noting the recurrence only needs two prior values is great. Interviewers often prompt for this; have the answer ready.

---

## Resources

- **Full Walkthrough**: [Climbing Stairs: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/climbing-stairs-interview-walkthrough/)
- **Practice**: [Mock interview for Climbing Stairs](https://intervu.dev/setup2?problem=climbing-stairs)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
