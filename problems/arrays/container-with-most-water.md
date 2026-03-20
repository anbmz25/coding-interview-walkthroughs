# Container With Most Water

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/container-with-most-water-interview-walkthrough/)*

> A step-by-step walkthrough of LeetCode #11 as it plays out in a real coding interview. Learn the two-pointer technique, the greedy argument for why it's correct, and the proof that moving the shorter pointer never misses the optimal pair.

**Difficulty**: Medium
**Patterns**: `two-pointers`, `greedy`, `arrays`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/container-with-most-water-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=container-with-most-water)**

---

## Problem

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`th line are at `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container that holds the most water. Return the maximum amount of water the container can store. You may not slant the container.

([LeetCode #11](https://leetcode.com/problems/container-with-most-water/))

### Example 1

**Input**
`height = [1, 8, 6, 2, 5, 4, 8, 3, 7]`

**Output**
`49`

### Example 2

**Input**
`height = [1, 1]`

**Output**
`1`

In Example 1, the best pair is indices `1` and `8` (heights `8` and `7`). Width = 7, height = min(8, 7) = 7, area = 49. The water level is limited by the *shorter* wall.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=container-with-most-water)*

---

## Solution

```python
def max_area(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        current_area = min(height[left], height[right]) * width
        max_water = max(max_water, current_area)

        # Move the shorter pointer inward
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1

    return max_water
```

Trace for `height = [1, 8, 6, 2, 5, 4, 8, 3, 7]`:

| Step | left | right | h[l] | h[r] | width | area | max | move |
|---|---|---|---|---|---|---|---|---|
| 1 | 0 | 8 | 1 | 7 | 8 | 8 | 8 | left++ |
| 2 | 1 | 8 | 8 | 7 | 7 | 49 | 49 | right-- |
| 3 | 1 | 7 | 8 | 3 | 6 | 18 | 49 | right-- |
| 4 | 1 | 6 | 8 | 8 | 5 | 40 | 49 | left++ |
| 5 | 2 | 6 | 6 | 8 | 4 | 24 | 49 | left++ |
| 6 | 3 | 6 | 2 | 8 | 3 | 6 | 49 | left++ |
| 7 | 4 | 6 | 5 | 8 | 2 | 10 | 49 | left++ |
| 8 | 5 | 6 | 4 | 8 | 1 | 4 | 49 | left++ |

`max_water = 49` ✓

---

## Complexity

| Aspect | Complexity | Explanation |
|---|---|---|
| Time | O(n) | Each pointer moves inward at most n times total |
| Space | O(1) | Only three integer variables |

---

## Common Interview Mistakes

1. **Moving the taller pointer instead of the shorter one.** The height is still constrained by the shorter wall and the width has decreased. The area can only get worse.

2. **Using `+` instead of `min()` in the area formula.** Water fills up to the *shorter* wall. Using sum or average is physically wrong.

3. **Computing width as `right - left + 1`.** The width is the distance between walls: `right - left`, not `right - left + 1`.

4. **Stopping the loop with `left <= right`.** When `left == right`, the container has zero width. The loop should end when pointers meet.

5. **Not being able to justify the pointer movement.** Writing correct code without explaining *why* is a red flag. Prepare: "Moving the taller pointer can't help because the height is still capped by the shorter wall and the width decreases."

6. **Jumping to two pointers without mentioning brute force first.** Naming the brute force and explaining why it's insufficient shows reasoning, not memorization.

---

## Resources

- **Full Walkthrough**: [Container With Most Water: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/container-with-most-water-interview-walkthrough/)
- **Practice**: [Mock interview for Container With Most Water](https://intervu.dev/setup2?problem=container-with-most-water)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Best Time to Buy and Sell Stock](best-time-to-buy-and-sell-stock.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/best-time-to-buy-and-sell-stock-interview-walkthrough/)
- [Contains Duplicate](contains-duplicate.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/contains-duplicate-interview-walkthrough/)
- [Insert Interval](insert-interval.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/insert-interval-interview-walkthrough/)
- [Longest Palindrome](longest-palindrome.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/longest-palindrome-interview-walkthrough/)
- [Majority Element](majority-element.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/majority-element-interview-walkthrough/)
- [Maximum Subarray](maximum-subarray.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/maximum-subarray-interview-walkthrough/)
- [Meeting Rooms](meeting-rooms.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/meeting-rooms-interview-walkthrough/)
- [Merge Intervals](merge-intervals.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/merge-intervals-interview-walkthrough/)
- [Product of Array Except Self](product-of-array-except-self.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/product-of-array-except-self-interview-walkthrough/)
- [Ransom Note](ransom-note.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/ransom-note-interview-walkthrough/)
- [Sort Colors](sort-colors.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/sort-colors-interview-walkthrough/)
- [3Sum](three-sum.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/three-sum-interview-walkthrough/)
- [Trapping Rain Water](trapping-rain-water.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/trapping-rain-water-interview-walkthrough/)
- [Two Sum](two-sum.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/two-sum-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
