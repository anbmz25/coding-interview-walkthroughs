# Trapping Rain Water

> A step-by-step guide to solving Trapping Rain Water in a coding interview: the geometric insight, prefix/suffix arrays, and the two-pointer O(1) space technique explained clearly.

**Difficulty**: Hard
**Patterns**: `two-pointers`, `arrays`

📖 **[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/trapping-rain-water-interview-walkthrough/)**
🎙️ **[Practice in a mock interview →](https://intervu.dev/setup2?problem=trapping-rain-water)**

---

## Problem

Given an array `height` of non-negative integers representing an elevation map where each bar has width 1, compute how much water can be trapped after it rains. ([LeetCode #42](https://leetcode.com/problems/trapping-rain-water/))

### Example

**Input**
`height = [0,1,0,2,1,0,1,3,1,0,1,2]`

**Output**
`6`

Visualize the height array as vertical bars. Water pools between taller bars: a low bar is covered by water up to the height of the shorter of the two tallest bars on its left and right sides. For the bar at index 5 (height `0`), the tallest bar to its left is `2` and to its right is `3`, so it holds `min(2, 3) - 0 = 2` units of water. Summing across all positions gives `6` total units. The first and last bars never hold water because there's nothing to contain it on their outer sides.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=trapping-rain-water)*

---

## Solution

### Approach 1: Prefix/Suffix Arrays (O(n) time, O(n) space)

```python
def trap(height: list[int]) -> int:
    n = len(height)
    if n < 3:
        return 0

    # max_left[i] = tallest bar from index 0 to i (inclusive)
    max_left = [0] * n
    max_left[0] = height[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], height[i])

    # max_right[i] = tallest bar from index i to n-1 (inclusive)
    max_right = [0] * n
    max_right[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], height[i])

    # Water above each bar = min of both maxima minus bar height
    total_water = 0
    for i in range(n):
        water_at_i = min(max_left[i], max_right[i]) - height[i]
        total_water += water_at_i  # Always >= 0 since max_left/right >= height[i]

    return total_water
```

### Approach 2: Two Pointers (O(n) time, O(1) space) — Optimal

```python
def trap(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_left, max_right = 0, 0
    total_water = 0

    while left < right:
        if height[left] <= height[right]:
            if height[left] >= max_left:
                max_left = height[left]   # New left peak — no water here
            else:
                total_water += max_left - height[left]  # Trapped water
            left += 1
        else:
            if height[right] >= max_right:
                max_right = height[right]  # New right peak — no water here
            else:
                total_water += max_right - height[right]  # Trapped water
            right -= 1

    return total_water
```

Implementation notes worth calling out in an interview:

- **The two-pointer approach never needs a `max(0, ...)` clamp.** Because `max_left` and `max_right` are always at least as large as the current bar height, the subtraction is always non-negative.
- **Process the pointer on the side with the smaller current height, not the smaller maximum.** The comparison is `height[left] <= height[right]`, not `max_left <= max_right`. This is the condition that guarantees the invariant.
- **Both pointers advance exactly once per iteration**, so the while loop runs exactly `n - 1` times total, confirming O(n) time.
- Present both approaches in an interview (prefix arrays first, then two pointers) to show the optimization journey.

---

## Complexity

| Approach | Time | Space |
|---|---|---|
| Brute Force | O(n^2) | O(1) |
| Prefix/Suffix Arrays | O(n) | O(n) |
| Two Pointers | O(n) | O(1) |

**Two-pointer time:** Both pointers traverse the array exactly once, each advancing one step per iteration until they meet. Every operation inside the loop is O(1). Total: O(n).

**Two-pointer space:** Only four scalar variables (`left`, `right`, `max_left`, `max_right`) regardless of input size. True O(1) auxiliary space.

The two-pointer solution achieves the theoretical optimum: you must examine every bar at least once (O(n) lower bound), and you need no more than constant extra storage. Stating this explicitly, "this is both time and space optimal," is a strong closing signal.

---

## Common Interview Mistakes

1. **Not explaining the water formula before coding.** The formula `min(max_left, max_right) - height[i]` is the entire geometric insight. Candidates who skip straight to implementation leave the interviewer unsure whether they understand the problem or are transcribing a memorized solution.

2. **Presenting only the two-pointer solution without showing the progression.** The two-pointer approach looks like magic if you haven't first established the precomputation approach. Always walk through: brute force, prefix arrays, two pointers. The journey is the point.

3. **Misidentifying which pointer to advance.** The rule: advance the pointer on the side where `height[left] <= height[right]`. Advancing the wrong pointer breaks the invariant and produces wrong results.

4. **Forgetting to update the running maximum before computing water.** For a bar that is a local peak, you update `max_left` or `max_right` and add zero water. Forgetting the update causes future bars to compute water against a stale maximum.

5. **Confusing the two-pointer comparison.** The comparison is on current bar heights (`height[left]` vs `height[right]`), not on running maxima. Using `max_left <= max_right` as the condition produces subtly wrong results.

6. **Not handling arrays of length less than 3.** An array with fewer than 3 bars can't trap water. While the two-pointer loop handles this correctly by terminating immediately, stating this edge case signals thoroughness.

7. **Declaring the solution correct without tracing through an example.** The two-pointer invariant is non-obvious. Trace through `[0,1,0,2,1,0,1,3,1,0,1,2]` step by step out loud to catch bugs.

---

## Resources

- 📖 **Full Walkthrough**: [Trapping Rain Water — Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/trapping-rain-water-interview-walkthrough/)
- 🎙️ **Practice**: [Mock interview for Trapping Rain Water](https://intervu.dev/setup2?problem=trapping-rain-water)
- 📚 [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- 📚 [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- 📚 [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anthropics/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev) — AI-powered mock interviews with instant feedback.*
