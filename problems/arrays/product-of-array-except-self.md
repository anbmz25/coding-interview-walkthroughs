# Product of Array Except Self

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/product-of-array-except-self-interview-walkthrough/)*

> A step-by-step walkthrough of LeetCode #238 as it unfolds in a real coding interview. Learn the prefix/suffix product technique, the O(1) space optimization, and the edge cases that catch even prepared candidates.

**Difficulty**: Medium
**Patterns**: `arrays`, `prefix-product`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/product-of-array-except-self-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=product-of-array-except-self)**

---

## Problem

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all elements in `nums` **except** `nums[i]`.

You must write an algorithm that runs in **O(n)** time and does **not use the division operation**.

([LeetCode #238](https://leetcode.com/problems/product-of-array-except-self/))

### Example

**Input**
`nums = [1, 2, 3, 4]`

**Output**
`[24, 12, 8, 6]`

For index `0`, the product of all other elements is `2 * 3 * 4 = 24`. For index `1`, it's `1 * 3 * 4 = 12`. For index `2`, it's `1 * 2 * 4 = 8`. And for index `3`, it's `1 * 2 * 3 = 6`. Every element in the output represents the product of the entire array with that one position excluded.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=product-of-array-except-self)*

---

## Solution

```python
def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    answer = [1] * n

    # Left pass: answer[i] = product of all elements to the left of i
    left_product = 1
    for i in range(n):
        answer[i] = left_product
        left_product *= nums[i]  # Update for the next position

    # Right pass: multiply in the product of all elements to the right of i
    right_product = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]  # Update for the next position (moving left)

    return answer
```

Let's trace through `nums = [1, 2, 3, 4]`:

**After left pass:** `answer = [1, 1, 2, 6]`
- Index 0: nothing to the left → 1
- Index 1: `1` to the left → 1
- Index 2: `1*2` to the left → 2
- Index 3: `1*2*3` to the left → 6

**After right pass:** `answer = [24, 12, 8, 6]`
- Index 3: multiply by 1 (nothing to the right)
- Index 2: multiply by 4
- Index 1: multiply by `4*3 = 12`
- Index 0: multiply by `4*3*2 = 24`

Clean, correct, and no division anywhere.

---

## Complexity

| Pass | Time Complexity | Extra Space |
|---|---|---|
| Left pass | O(n) | O(1), single running variable |
| Right pass | O(n) | O(1), single running variable |
| **Total** | **O(n)** | **O(1)** (output array excluded) |

**Time:** Two sequential passes over the array, each visiting every element exactly once. Total: O(n).

**Space:** The output array itself is O(n), but by convention (and as specified in the problem) it doesn't count toward the space complexity. The only auxiliary space used is two integer variables (`left_product` and `right_product`).

---

## Common Interview Mistakes

1. **Proposing the division approach without acknowledging the constraint.** Some candidates jump straight to "compute total product, divide each time," which is wrong here. Reading constraints carefully and ruling out forbidden approaches explicitly is a strong signal.

2. **Forgetting to initialize `left_product` and `right_product` to `1`.** It sounds trivial, but initializing the running product to `0` is a subtle bug that produces all-zero output. Always think about the identity element for your operation: for multiplication, it's `1`.

3. **Off-by-one in the right pass.** The right pass must start from `n - 1` and go down to `0`. Starting from `n` or stopping at `1` will silently skip an index and produce wrong output.

4. **Using two full prefix/suffix arrays instead of optimizing to O(1).** The two-array version is correct and acceptable in many interviews, but if an interviewer asks "can you do it with O(1) extra space?", you should be ready with the running-variable optimization. Practicing both versions pays off.

5. **Not tracing through the example by hand before declaring it done.** This problem has a subtle two-pass structure that's easy to convince yourself is correct when it isn't. Always do a quick dry run on `[1, 2, 3, 4]` before moving on.

6. **Coding before explaining the two-pass insight.** The key insight here is genuinely elegant. Interviewers want to hear you articulate it, "the answer at each index is just a left product times a right product," before you touch the keyboard.

7. **Forgetting the edge case where the array has exactly two elements.** `nums = [3, 4]` should return `[4, 3]`. It works with the algorithm above, but it's worth verifying mentally during the interview to show thoroughness.

---

## Resources

- **Full Walkthrough**: [Product of Array Except Self: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/product-of-array-except-self-interview-walkthrough/)
- **Practice**: [Mock interview for Product of Array Except Self](https://intervu.dev/setup2?problem=product-of-array-except-self)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Best Time to Buy and Sell Stock](best-time-to-buy-and-sell-stock.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/best-time-to-buy-and-sell-stock-interview-walkthrough/)
- [Container With Most Water](container-with-most-water.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/container-with-most-water-interview-walkthrough/)
- [Contains Duplicate](contains-duplicate.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/contains-duplicate-interview-walkthrough/)
- [Find All Anagrams in a String](find-all-anagrams-in-a-string.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/find-all-anagrams-in-a-string-interview-walkthrough/)
- [Find Median from Data Stream](find-median-from-data-stream.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/find-median-from-data-stream-interview-walkthrough/)
- [Insert Interval](insert-interval.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/insert-interval-interview-walkthrough/)
- [K Closest Points to Origin](k-closest-points-to-origin.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/k-closest-points-to-origin-interview-walkthrough/)
- [Longest Palindrome](longest-palindrome.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/longest-palindrome-interview-walkthrough/)
- [Majority Element](majority-element.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/majority-element-interview-walkthrough/)
- [Maximum Subarray](maximum-subarray.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/maximum-subarray-interview-walkthrough/)
- [Meeting Rooms](meeting-rooms.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/meeting-rooms-interview-walkthrough/)
- [Merge Intervals](merge-intervals.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/merge-intervals-interview-walkthrough/)
- [Ransom Note](ransom-note.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/ransom-note-interview-walkthrough/)
- [Sort Colors](sort-colors.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/sort-colors-interview-walkthrough/)
- [Spiral Matrix](spiral-matrix.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/spiral-matrix-interview-walkthrough/)
- [Task Scheduler](task-scheduler.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/task-scheduler-interview-walkthrough/)
- [3Sum](three-sum.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/three-sum-interview-walkthrough/)
- [Trapping Rain Water](trapping-rain-water.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/trapping-rain-water-interview-walkthrough/)
- [Two Sum](two-sum.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/two-sum-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
