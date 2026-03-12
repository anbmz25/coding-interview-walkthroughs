# Coin Change

> A step-by-step guide to solving the Coin Change problem in a coding interview: from recursive brute force to optimal bottom-up DP with recurrence derivation and greedy failure analysis.

**Difficulty**: Medium
**Patterns**: `dynamic-programming`, `dp`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/coin-change-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=coin-change)**

---

## Problem

You are given an integer array `coins` representing coin denominations and an integer `amount` representing a target total. Return the **fewest number of coins** needed to make up that amount. If the amount cannot be made up by any combination of the given coins, return `-1`. You may use each coin denomination an **unlimited** number of times. ([LeetCode #322](https://leetcode.com/problems/coin-change/))

### Example

**Input**
`coins = [1, 5, 11], amount = 15`

**Output**
`3`

The optimal combination is three coins of denomination `5` (5 + 5 + 5 = 15). Note that a greedy approach, always picking the largest coin that fits, would choose `11` first, then need four `1`s to reach 15, giving a total of five coins. Greedy fails here, which is exactly why this problem requires dynamic programming. A second example: `coins = [2]`, `amount = 3` returns `-1` because no combination of `2`s can sum to `3`.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=coin-change)*

---

## Solution

```python
def coinChange(coins: list[int], amount: int) -> int:
    # dp[i] = minimum coins needed to make exactly amount i
    # Initialize to infinity to represent "not yet reachable"
    dp = [float('inf')] * (amount + 1)

    # Base case: 0 coins needed to make amount 0
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] != float('inf'):
                # Using this coin gives us dp[i - coin] + 1 total coins
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[amount] is still infinity, no valid combination exists
    return dp[amount] if dp[amount] != float('inf') else -1
```

Style notes worth calling out in an interview:

- Initializing `dp` to `float('inf')` rather than `-1` or `0` is deliberate. It acts as a sentinel for "unreachable," and the `min()` operation naturally ignores unreachable states without special-casing.
- The guard `dp[i - coin] != float('inf')` prevents building on unreachable sub-amounts. Omitting it would leave `dp[i]` as `inf + 1`, which is still `inf` in Python but signals unclear thinking.
- The nested loop order (outer over amounts, inner over coins) is the standard unbounded knapsack pattern. Swapping them would still work here since coins are unbounded, but the current order is clearer and more conventional.
- Converting `float('inf')` to `-1` only at the final return keeps all internal logic clean and uniform.

For completeness, here's the top-down memoized version, useful to present as the stepping stone:

```python
from functools import lru_cache

def coinChange(coins: list[int], amount: int) -> int:
    @lru_cache(maxsize=None)
    def dp(remaining):
        if remaining == 0:
            return 0
        if remaining < 0:
            return float('inf')
        return min(dp(remaining - c) + 1 for c in coins)

    result = dp(amount)
    return result if result != float('inf') else -1
```

---

## Complexity

| Operation | Complexity |
|---|---|
| Time | O(amount × len(coins)) |
| Space | O(amount) |

**Time:** The outer loop runs `amount` times. For each sub-amount, the inner loop iterates over all `len(coins)` denominations. Every operation inside is O(1). Total: O(amount × len(coins)).

**Space:** The `dp` array has `amount + 1` entries. No other data structures scale with input size. Space is O(amount).

A common follow-up: *"Can you do better than O(amount × len(coins))?"* The honest answer is no. This is essentially optimal for the general case. You can prune with early termination in practice, but the asymptotic bound holds. Saying this confidently demonstrates genuine understanding of the algorithm's limits.

---

## Common Interview Mistakes

1. **Reaching for greedy first without questioning it.** Greedy (always use the largest coin that fits) works for standard coin systems like US currency, but fails for arbitrary denominations. Candidates who implement greedy without questioning it signal they haven't thought critically about the problem structure. Always justify *why* DP is needed.

2. **Initializing `dp` to `0` instead of `infinity`.** If `dp[i]` starts at `0`, the `min()` operation will always return `0`, never updating to the real answer. The infinity sentinel is essential, not a minor implementation detail.

3. **Forgetting the `dp[0] = 0` base case.** Without it, no amount greater than zero can ever be reached, because every path back to zero would find `dp[0] = inf` and halt. The base case is what seeds the entire table.

4. **Off-by-one in the loop range.** Using `range(1, amount)` instead of `range(1, amount + 1)` skips computing `dp[amount]`, the very value you need. Always double-check loop bounds with a small example.

5. **Not handling the impossible case.** Returning `dp[amount]` directly without checking for infinity yields a confusing large number instead of `-1`. The final conversion is not optional.

6. **Confusing unbounded vs. 0/1 knapsack.** In this problem, each coin can be used unlimited times. That's why `dp[i - coin]` is safe to use in a forward-filling loop. If each coin could only be used once, the loop order and state definition would change. Mentioning this distinction earns points.

7. **Not articulating the recurrence before coding.** The DP table means nothing without a clear state definition. Before writing a single line, say: *"`dp[i]` is the minimum coins to make amount `i`, and `dp[i] = min(dp[i - c] + 1)` for each valid coin `c`."* Candidates who skip this and go straight to code look like they're transcribing a memorized solution.

---

## Resources

- **Full Walkthrough**: [Coin Change: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/coin-change-interview-walkthrough/)
- **Practice**: [Mock interview for Coin Change](https://intervu.dev/setup2?problem=coin-change)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
