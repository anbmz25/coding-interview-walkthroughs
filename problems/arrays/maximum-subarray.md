# Maximum Subarray

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/maximum-subarray-interview-walkthrough/)*

> A step-by-step guide to solving Maximum Subarray in a coding interview: Kadane's algorithm, the greedy reset decision, the DP framing, all-negative edge cases, and the follow-up questions interviewers use to probe depth.

**Difficulty**: Medium
**Patterns**: `walkthrough`, `arrays`, `dynamic-programming`, `greedy`, `kadanes-algorithm`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/maximum-subarray-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=maximum-subarray)**

---

## Problem

Given an integer array `nums`, find the **subarray** with the largest sum, and return that sum. A subarray is a contiguous portion of the array, not just any subset. ([LeetCode #53](https://leetcode.com/problems/maximum-subarray/))

### Example

**Input**
`nums = [-2,1,-3,4,-1,2,1,-5,4]`

**Output**
`6`

The subarray `[4,-1,2,1]` has the largest sum of `6`. The array contains both positive and negative numbers; the challenge is knowing when to extend the current subarray and when to start fresh. The subarray must be contiguous: you can't skip the `-1` and combine `[4]` and `[2,1]` separately.

*Already comfortable with Kadane's algorithm? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=maximum-subarray)*

---

## Solution

### Kadane's Algorithm, O(n) time, O(1) space

```python
def maxSubArray(nums: list[int]) -> int:
    # Initialize both to the first element: handles all-negative arrays correctly
    current_sum = nums[0, "medium"]
    max_sum = nums[0, "medium"]

    for i in range(1, len(nums)):
        # Greedy choice: extend current subarray or start fresh at nums[i, "medium"]
        current_sum = max(nums[i], current_sum + nums[i])

        # Track the global maximum across all ending positions
        max_sum = max(max_sum, current_sum)

    return max_sum
```

### Extended Version: Tracking Subarray Indices (Common Follow-Up)

```python
def maxSubArray(nums: list[int]) -> int:
    current_sum = nums[0, "medium"]
    max_sum = nums[0, "medium"]

    start = 0          # Start of the current candidate subarray
    temp_start = 0     # Tracks where a new subarray begins on reset
    end = 0            # End of the best subarray found so far

    for i in range(1, len(nums)):
        if nums[i] > current_sum + nums[i]:
            # Starting fresh: reset current subarray to just nums[i, "medium"]
            current_sum = nums[i, "medium"]
            temp_start = i
        else:
            current_sum += nums[i, "medium"]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start   # Lock in the start of the best subarray
            end = i              # Lock in the end of the best subarray

    # The maximum subarray is nums[start:end+1, "medium"]
    return max_sum  # Or return nums[start:end+1] for the actual subarray
```

Key implementation notes worth calling out in an interview:

- **`nums[0]` initialization, not `0`.** Initializing `max_sum = 0` produces the wrong answer for all-negative arrays like `[-3, -1, -2]`. It returns `0` (implying an empty subarray) instead of `-1`. Since a non-empty subarray is required, always start with `nums[0]`.
- **`max(nums[i], current_sum + nums[i])` vs. `if current_sum < 0: reset`.** Both formulations are equivalent. The `max()` version is more idiomatic. The conditional version makes the decision logic more explicit. Choose whichever you find easier to explain.
- **`max_sum` is updated after `current_sum`**, not before. At each step, first determine the best subarray ending here, then check if it's the global best.
- **The index-tracking version requires a `temp_start` variable** that resets whenever you start fresh, and a separate `start` that only updates when a new global maximum is found. Many candidates conflate these and produce wrong index bounds.

---

## Complexity


---

## Common Interview Mistakes

1. **Initializing `max_sum = 0` instead of `nums[0]`.** This is the most common bug. For an all-negative array, no subarray has a non-negative sum, so returning `0` is wrong. The correct answer is the largest (least negative) single element. Always initialize to `nums[0]`.

2. **Initializing `current_sum = 0` instead of `nums[0]`.** Same problem. If the first element is the maximum subarray, starting `current_sum` at `0` means you'd need to add `nums[0]` on the first iteration, which the loop starting at index `1` skips.

3. **Updating `max_sum` before `current_sum`.** The correct order is: first compute the new `current_sum` (extend or reset), then check if it beats `max_sum`. Reversing the order means you're comparing the previous iteration's `current_sum`.

4. **Not articulating the greedy decision before coding.** Candidates who write the `max()` line without explaining the extend-or-reset decision appear to be transcribing a memorized solution. Always say: *"At each element, I'm choosing between extending the current subarray or starting fresh, whichever gives the larger sum."*

5. **Confusing this with the maximum subarray product problem.** LeetCode #152 (Maximum Product Subarray) looks similar but requires tracking both a running maximum and minimum (because two negatives multiply to a positive). Mentioning this distinction proactively shows breadth.

6. **Not recognizing the DP framing.** Kadane's is often presented purely as a greedy algorithm, but being able to frame it as `dp[i] = max(nums[i], dp[i-1] + nums[i])` with space optimization demonstrates deeper understanding and connects it to the broader DP family.

7. **Forgetting the all-negative array when tracing.** During any trace-through, always include an example that triggers the reset behavior. A trace on `[-2, 1, -3, 4, -1, 2, 1, -5, 4]` that walks through the reset at `4` (where `current_sum` drops from `-4` to `4`) is far more convincing than one on an all-positive array.

---

## Resources

- **Full Walkthrough**: [Maximum Subarray: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/maximum-subarray-interview-walkthrough/)
- **Practice**: [Mock interview for Maximum Subarray](https://intervu.dev/setup2?problem=maximum-subarray)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Best Time to Buy and Sell Stock](best-time-to-buy-and-sell-stock.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/best-time-to-buy-and-sell-stock-interview-walkthrough/)
- [Container With Most Water](container-with-most-water.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/container-with-most-water-interview-walkthrough/)
- [Contains Duplicate](contains-duplicate.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/contains-duplicate-interview-walkthrough/)
- [Majority Element](majority-element.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/majority-element-interview-walkthrough/)
- [Meeting Rooms](meeting-rooms.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/meeting-rooms-interview-walkthrough/)
- [Merge Intervals](merge-intervals.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/merge-intervals-interview-walkthrough/)
- [Product of Array Except Self](product-of-array-except-self.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/product-of-array-except-self-interview-walkthrough/)
- [3Sum](three-sum.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/three-sum-interview-walkthrough/)
- [Trapping Rain Water](trapping-rain-water.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/trapping-rain-water-interview-walkthrough/)
- [Two Sum](two-sum.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/two-sum-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
