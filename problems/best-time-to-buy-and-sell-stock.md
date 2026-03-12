# Best Time to Buy and Sell Stock

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/best-time-to-buy-and-sell-stock-interview-walkthrough/)*

> A step-by-step walkthrough of Best Time to Buy and Sell Stock as it unfolds in a real coding interview. Learn the greedy O(n) approach, common mistakes, and how strong candidates communicate the solution.

**Difficulty**: Easy
**Patterns**: `arrays`, `greedy`, `best-time-to-buy-and-sell-stock`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/best-time-to-buy-and-sell-stock-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=best-time-to-buy-and-sell-stock)**

---

## Problem

You're given an array `prices` where `prices[i]` represents the price of a stock on day `i`. You want to maximize your profit by choosing **one day to buy** and a **later day to sell**. If no profit is possible, return `0`. ([LeetCode #121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/))

### Example

**Input**
```
prices = [7, 1, 5, 3, 6, 4]
```

**Output**
```
5
```

**Explanation:** On day 2 the price is `1` (buy), and on day 5 the price is `6` (sell), yielding a profit of `6 - 1 = 5`. Note that buying on day 2 and selling on day 1 is not allowed. You must buy *before* you sell. The maximum single-transaction profit is `5`, not `7` (which would require selling before buying).

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=best-time-to-buy-and-sell-stock)*

---

## Solution

```python
def maxProfit(prices: list[int]) -> int:
    min_price = float('inf')  # Best buying price seen so far
    max_profit = 0            # Best profit achievable so far

    for price in prices:
        if price < min_price:
            # Found a cheaper day to buy, so update our reference point
            min_price = price
        else:
            # What's the profit if we sell today?
            current_profit = price - min_price
            max_profit = max(max_profit, current_profit)

    return max_profit
```

**Why this is interview-friendly:**
- Using `float('inf')` as the initial `min_price` is more robust than `prices[0]`, since it handles edge cases like an empty array without an index error.
- The variable names `min_price` and `max_profit` communicate intent without needing comments.
- The `else` branch makes the logic explicit: you're either updating your buy point *or* evaluating a potential sale, never both in the same step.

---

## Complexity

| Operation | Complexity |
|---|---|
| Iterating through the array | O(n) |
| Each comparison/assignment | O(1) |
| **Overall time** | **O(n)** |
| Space (two variables) | O(1) |

**Time:** We iterate through the array exactly once. Each step involves a constant number of comparisons and assignments.

**Space:** We use only two variables regardless of input size: this is optimal. Unlike the Two Sum hash map solution, there's no space tradeoff here. We get both O(n) time *and* O(1) space.

This is worth emphasizing in an interview: *"This is about as efficient as it gets: linear time and constant space."*

---

## Common Interview Mistakes

- **Selling before buying.** Iterating through all pairs without enforcing `j > i` is the most common brute-force bug. Always verify that your buy day precedes your sell day.

- **Initializing `min_price` to `0`.** Zero seems like a safe default, but if all prices are positive (which they are for stocks), this would cause `min_price` to never update. Use `float('inf')` or `prices[0]`.

- **Returning a negative profit.** If prices only decrease (e.g., `[7, 6, 4, 3, 1]`), the correct answer is `0`. You simply don't trade. Forgetting to initialize `max_profit = 0` and instead returning the least-negative difference is a subtle but wrong answer.

- **Confusing this with the "maximum subarray" problem.** Kadane's algorithm solves a related but different problem. While you *can* convert Buy and Sell Stock into a max subarray problem using price differences, jumping straight there without explanation confuses interviewers who want to see your greedy reasoning.

- **Not handling a single-element array.** If `prices = [5]`, you can't make any transaction. Your solution should return `0` naturally, so verify this with your initialization choices.

- **Coding without explaining the greedy insight.** The implementation is short, which means the verbal explanation carries more weight. Candidates who type the solution silently and then say "done" leave the interviewer with nothing to evaluate.

- **Not mentioning follow-up variants.** Proactively noting that this problem has harder siblings (unlimited transactions, at most k transactions, with cooldown) shows breadth and invites a richer interview conversation.

---

## Resources

- **Full Walkthrough**: [Best Time to Buy and Sell Stock: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/best-time-to-buy-and-sell-stock-interview-walkthrough/)
- **Practice**: [Mock interview for Best Time to Buy and Sell Stock](https://intervu.dev/setup2?problem=best-time-to-buy-and-sell-stock)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
