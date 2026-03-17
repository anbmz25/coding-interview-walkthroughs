# Search in Rotated Sorted Array

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/search-in-rotated-sorted-array-interview-walkthrough/)*

> A step-by-step walkthrough of LeetCode #33 as it plays out in a real coding interview. Learn how to adapt binary search for rotated arrays, nail the boundary conditions, and handle the follow-ups interviewers use to test depth.

**Difficulty**: Medium
**Patterns**: `binary-search`, `arrays`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/search-in-rotated-sorted-array-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=search-in-rotated-sorted-array)**

---

## Problem

You are given an integer array `nums` sorted in ascending order, which has been **rotated** at some unknown pivot index. For example, `[0, 1, 2, 4, 5, 6, 7]` might become `[4, 5, 6, 7, 0, 1, 2]` after rotating at index 3.

Given `nums` and an integer `target`, return the index of `target` if it exists in the array, or `-1` if it does not. Your solution **must run in O(log n) time**.

([LeetCode #33](https://leetcode.com/problems/search-in-rotated-sorted-array/))

### Example 1

**Input**
`nums = [4, 5, 6, 7, 0, 1, 2], target = 0`

**Output**
`4`

### Example 2

**Input**
`nums = [4, 5, 6, 7, 0, 1, 2], target = 3`

**Output**
`-1`

In Example 1, the array was originally `[0, 1, 2, 4, 5, 6, 7]` and was rotated so that `4` is now at index `0`. Target `0` is found at index `4`. In Example 2, `3` simply doesn't exist in the array. The key structural observation is that even after rotation, at least one half of the array, when you pick a midpoint, is always guaranteed to be sorted. That guarantee is what makes O(log n) possible.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=search-in-rotated-sorted-array)*

---

## Solution

```python
def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Determine which half is guaranteed to be sorted
        if nums[left] <= nums[mid]:
            # Left half [left, mid] is sorted
            if nums[left] <= target < nums[mid]:
                # Target falls within the sorted left range
                right = mid - 1
            else:
                # Target must be in the right half
                left = mid + 1
        else:
            # Right half [mid, right] is sorted
            if nums[mid] < target <= nums[right]:
                # Target falls within the sorted right range
                left = mid + 1
            else:
                # Target must be in the left half
                right = mid - 1

    return -1  # Target not found
```

Let's trace through Example 1: `nums = [4, 5, 6, 7, 0, 1, 2], target = 0`

- `left=0, right=6` → `mid=3`, `nums[3]=7`, not target
  - `nums[0]=4 <= nums[3]=7` → left half `[4,5,6,7]` is sorted
  - Is `4 <= 0 < 7`? No → search right half → `left = 4`
- `left=4, right=6` → `mid=5`, `nums[5]=1`, not target
  - `nums[4]=0 <= nums[5]=1` → left half `[0,1]` is sorted
  - Is `0 <= 0 < 1`? Yes → search left half → `right = 4`
- `left=4, right=4` → `mid=4`, `nums[4]=0` → **found! return 4** ✓

---

## Complexity

| Aspect | Complexity | Explanation |
|---|---|---|
| Time | O(log n) | Each iteration eliminates half the remaining array |
| Space | O(1) | Only pointer variables, no auxiliary data structures |

**Time:** The rotation doesn't change the fundamental O(log n) guarantee because we still eliminate exactly half the search space at every step. We've simply added logic to determine *which* half to eliminate.

**Space:** Only three integer variables (`left`, `right`, `mid`). No recursion, no auxiliary data structures.

---

## Common Interview Mistakes

1. **Using `<` instead of `<=` when checking if the left half is sorted.** The condition `nums[left] <= nums[mid]` uses `<=`, not `<`. This matters when `left == mid` (single element remaining on the left). Using strict `<` would misclassify that case and send the search in the wrong direction.

2. **Getting the target range check wrong.** When checking if the target is in the sorted left half, the condition is `nums[left] <= target < nums[mid]`, strict less-than on the right because `mid` itself was already checked. Flipping any of these operators silently produces wrong answers on edge cases.

3. **Trying to find the pivot first.** Some candidates spend time writing a separate function to locate the rotation point, then run two binary searches. This works but is more complex and easier to get wrong. The one-pass approach is cleaner and directly demonstrates the core insight.

4. **Not handling the non-rotated case.** If the array was never rotated (e.g., `[1, 2, 3, 4, 5]`), `nums[left] <= nums[mid]` is always true and the algorithm correctly reduces to standard binary search. Candidates who hardcode assumptions about a pivot always existing will fail this case.

5. **Off-by-one on pointer updates.** When you've confirmed the target is NOT in the sorted half, you move to the other side using `left = mid + 1` or `right = mid - 1`, not `left = mid` or `right = mid`. Forgetting the `±1` creates an infinite loop when the target is adjacent to the midpoint.

6. **Coding before drawing an example.** The decision logic in this problem is dense. Candidates who code immediately, without first walking through a concrete rotated array, frequently write conditions they haven't verified. Spending 60 seconds tracing through `[4,5,6,7,0,1,2]` with `target=0` before writing a line of code prevents most bugs.

7. **Forgetting to handle `target == nums[mid]` before the half-determination logic.** This check must come first. If you defer it, you risk updating `left` or `right` past the answer before you check it.

---

## Resources

- **Full Walkthrough**: [Search in Rotated Sorted Array: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/search-in-rotated-sorted-array-interview-walkthrough/)
- **Practice**: [Mock interview for Search in Rotated Sorted Array](https://intervu.dev/setup2?problem=search-in-rotated-sorted-array)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Binary Search](binary-search.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/binary-search-interview-walkthrough/)
- [First Bad Version](first-bad-version.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/first-bad-version-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
