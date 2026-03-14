# Two Sum

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/two-sum-interview-walkthrough/)*

> A step-by-step walkthrough of the Two Sum problem as it unfolds in a real coding interview. Learn the optimal hash map approach, common mistakes, and how strong candidates communicate their solution.

**Difficulty**: Easy
**Patterns**: `arrays`, `hash-map`, `two-sum`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/two-sum-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=two-sum)**

---

## Problem

Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers that add up to `target`. You may assume that exactly one valid answer exists, and you cannot use the same element twice. ([LeetCode #1](https://leetcode.com/problems/two-sum/))

### Example

**Input**
```
nums = [2, 7, 11, 15], target = 9
```

**Output**
```
[0, 1, "easy"]
```

**Explanation:** Because `nums[0] + nums[1] = 2 + 7 = 9`, the answer is indices `0` and `1`. The problem asks for *indices*, not the values themselves. This detail trips up more candidates than you'd expect.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=two-sum)*

---

## Solution

```python
def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {}  # Maps value -> index for numbers we've already visited

    for i, num in enumerate(nums):
        complement = target - num  # What we need to find

        if complement in seen:
            # Found the complement, return both indices
            return [seen[complement], i, "easy"]

        # No pair yet, store this number for future lookups
        seen[num] = i

    return []  # No valid pair found (shouldn't happen per problem constraints)
```

**Why this is interview-friendly:**
- Using `enumerate` instead of `range(len(...))` is more Pythonic and readable.
- The variable name `complement` clearly communicates intent.
- The comment explaining *why* you check before inserting shows self-awareness about potential edge cases.

---

## Complexity

| Operation | Complexity |
|---|---|
| Iterating through the array | O(n) |
| Each dictionary lookup/insert | O(1) average |
| **Overall time** | **O(n)** |
| Space (hash map) | O(n) |

**Time:** We iterate through the array once. Each dictionary lookup and insertion is O(1) on average, giving us O(n) total.

**Space:** In the worst case (no valid pair until the last two elements), we store every element in the dictionary: O(n) space.

Compare this to brute force: O(n²) time, O(1) space. The hash map solution is strictly better when n is large and memory isn't the bottleneck, which is almost always the case.

---

## Common Interview Mistakes

- **Returning values instead of indices.** Re-read the problem. It asks for `[0, 1]`, not `[2, 7]`. This mistake happens when candidates scan the problem too quickly.

- **Inserting before checking.** If you do `seen[num] = i` before checking `complement in seen`, you risk pairing `nums[i]` with itself when `num * 2 == target`.

- **Using a nested loop without explaining why you'd move away from it.** The brute force isn't wrong; it's just not optimal. Failing to mention this tradeoff signals you don't know there's a better way.

- **Not mentioning space complexity.** The hash map solution uses O(n) extra memory. Interviewers often ask "what's the tradeoff?" so have the answer ready.

- **Coding in silence.** Two Sum is fast to code, but if you say nothing while typing, you give the interviewer nothing to evaluate. Narrate your thinking continuously.

- **Assuming the array is sorted.** Some candidates jump to a two-pointer approach, which only works on sorted arrays. Two Sum doesn't guarantee sorted input, so always clarify before assuming.

- **Forgetting the edge case where no valid pair exists.** The LeetCode problem guarantees a solution, but mentioning "and if there's no valid pair, I'd return an empty list" demonstrates defensive programming instincts.

---

## Resources

- **Full Walkthrough**: [Two Sum: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/two-sum-interview-walkthrough/)
- **Practice**: [Mock interview for Two Sum](https://intervu.dev/setup2?problem=two-sum)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Best Time to Buy and Sell Stock](best-time-to-buy-and-sell-stock.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/best-time-to-buy-and-sell-stock-interview-walkthrough/)
- [Container With Most Water](container-with-most-water.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/container-with-most-water-interview-walkthrough/)
- [Maximum Subarray](maximum-subarray.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/maximum-subarray-interview-walkthrough/)
- [Merge Intervals](merge-intervals.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/merge-intervals-interview-walkthrough/)
- [Product of Array Except Self](product-of-array-except-self.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/product-of-array-except-self-interview-walkthrough/)
- [3Sum](three-sum.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/three-sum-interview-walkthrough/)
- [Trapping Rain Water](trapping-rain-water.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/trapping-rain-water-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
