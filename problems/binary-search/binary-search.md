# Binary Search

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/binary-search-interview-walkthrough/)*

> A step-by-step walkthrough of the Binary Search problem as it unfolds in a real coding interview. Learn the precise boundary logic, off-by-one traps, and how strong candidates communicate this deceptively simple algorithm.

**Difficulty**: Easy
**Patterns**: `binary-search`, `arrays`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/binary-search-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=binary-search)**

---

## Problem

Given a sorted array of distinct integers `nums` and a target integer `target`, return the index of `target` in the array. If `target` is not present, return `-1`. Your solution must run in **O(log n)** time. ([LeetCode #704](https://leetcode.com/problems/binary-search/))

### Example

**Input**
```
nums = [-1, 0, 3, 5, 9, 12], target = 9
```

**Output**
```
4
```

The value `9` appears at index `4` in the sorted array. The O(log n) constraint rules out a simple linear scan, and the interviewer is explicitly asking for the binary search approach. A second example: if `target = 2`, the output is `-1` because `2` does not exist in the array.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=binary-search)*

---

## Solution

```python
def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1  # Inclusive boundaries

    while left <= right:  # Continue while search space is non-empty
        # Compute mid this way to avoid integer overflow (matters in lower-level languages)
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid                  # Found the target
        elif nums[mid] < target:
            left = mid + 1              # Target is in the right half
        else:
            right = mid - 1             # Target is in the left half

    return -1  # Target not in array
```

Style notes worth mentioning in an interview:

- The `mid` computation using `left + (right - left) // 2` instead of `(left + right) // 2` prevents integer overflow. In Python this doesn't matter, but in Java or C++ it does, and mentioning it signals real-world awareness.
- The `left <= right` loop condition is deliberately inclusive. It handles the case where one element remains.
- Each branch updates `left` or `right` past `mid`, not to `mid`, ensuring the search space strictly shrinks every iteration.

---

## Complexity

| Operation | Complexity |
|---|---|
| Time | O(log n) |
| Space | O(1) |

**Time:** Each iteration halves the search space. Starting from `n` elements, after `k` iterations you have `n / 2^k` elements remaining. The loop ends when `n / 2^k < 1`, so `k = log₂(n)` iterations maximum.

**Space:** The iterative implementation uses only three variables (`left`, `right`, `mid`) regardless of input size, constant space. Note: a *recursive* implementation uses O(log n) space due to the call stack. This is worth mentioning as a comparison point.

---

## Common Interview Mistakes

1. **Using `left < right` instead of `left <= right`.** This causes the loop to exit one iteration early, missing the case where exactly one element remains in the search space. If that single element is your target, you'll incorrectly return `-1`.

2. **Setting `left = mid` or `right = mid` instead of `mid ± 1`.** If `nums[mid] != target`, you need to exclude `mid` from the next search range. Failing to do so can create an infinite loop when `left` and `right` are adjacent.

3. **Computing `mid = (left + right) // 2`.** Correct in Python, but a classic integer overflow bug in Java and C++. Getting in the habit of writing `left + (right - left) // 2` is worth the extra keystrokes, and mentioning it earns points.

4. **Not handling an empty array.** If `nums = []`, the loop never executes and `-1` is returned correctly, but only if your initialization doesn't cause an index error. Confirm this with your interviewer or add a guard clause.

5. **Forgetting to test boundary targets.** The most common off-by-one bugs manifest when the target is the first or last element. Mentally trace `nums = [1, 3, 5]`, `target = 1` and `target = 5` through your code before declaring it done.

6. **Jumping to code without explaining the loop invariant.** Binary search is fundamentally about maintaining a contract: *"the target, if it exists, is always within [left, right]."* Candidates who explain this invariant demonstrate true understanding, not just memorization.

7. **Coding silently.** With a 5-line implementation, your verbal explanation *is* the interview. Saying nothing while you type gives the interviewer nothing to evaluate. Narrate every decision, especially the boundary choices.

---

## Resources

- **Full Walkthrough**: [Binary Search: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/binary-search-interview-walkthrough/)
- **Practice**: [Mock interview for Binary Search](https://intervu.dev/setup2?problem=binary-search)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [First Bad Version](first-bad-version.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/first-bad-version-interview-walkthrough/)
- [Search in Rotated Sorted Array](search-in-rotated-sorted-array.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/search-in-rotated-sorted-array-interview-walkthrough/)
- [Time Based Key-Value Store](time-based-key-value-store.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/time-based-key-value-store-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
