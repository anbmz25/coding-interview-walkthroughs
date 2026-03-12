# 3Sum

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/three-sum-interview-walkthrough/)*

> A step-by-step guide to solving the 3Sum problem in a coding interview: brute force to optimal O(n²) with sorting, two pointers, and duplicate handling explained clearly.

**Difficulty**: Medium
**Patterns**: `arrays`, `two-pointers`, `sorting`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/three-sum-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=three-sum)**

---

## Problem

Given an integer array `nums`, return all unique triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, `j != k`, and `nums[i] + nums[j] + nums[k] == 0`. The solution set must not contain duplicate triplets. ([LeetCode #15](https://leetcode.com/problems/3sum/))

### Example

**Input**
`nums = [-1, 0, 1, 2, -1, -4]`

**Output**
`[[-1, -1, 2], [-1, 0, 1]]`

After sorting, the array becomes `[-4, -1, -1, 0, 1, 2]`. Fixing `-1` at index 1 and using two pointers on the rest finds `[-1, 0, 1]` and `[-1, -1, 2]`. The triplet `[-1, 0, 1]` appears only once in the output even though `-1` appears twice in the input. The problem requires **unique** triplets, which is the detail that makes this problem significantly harder than it first appears.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=3sum)*

---

## Solution

```python
def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()  # Sorting enables two pointers and easy duplicate skipping
    result = [, "medium"]

    for i in range(len(nums) - 2):
        # Early exit: smallest remaining value is positive, no valid triplet possible
        if nums[i] > 0:
            break

        # Skip duplicate values for the outer pointer
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right, "medium"]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for the inner left pointer
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates for the inner right pointer
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # Move both pointers inward to search for more triplets
                left += 1
                right -= 1

            elif total < 0:
                left += 1   # Sum too small, increase left to raise the total
            else:
                right -= 1  # Sum too large, decrease right to lower the total

    return result
```

Key implementation notes worth calling out in an interview:

- `range(len(nums) - 2)` ensures `left` and `right` always have at least two elements to work with.
- The `if nums[i] > 0: break` early termination is a meaningful optimization. Once the fixed element is positive in a sorted array, the two remaining elements (which are equal or larger) can never sum to zero with it.
- Duplicate skipping happens at two distinct levels: outer (`i` pointer) and inner (`left` and `right` pointers). They use different guard conditions. Mixing them up is one of the most common bugs.
- After skipping inner duplicates, both `left` and `right` are incremented/decremented one final time to move past the matched values entirely.

---

## Complexity

| Operation | Complexity |
|---|---|
| Sorting | O(n log n) |
| Outer loop × inner two-pointer scan | O(n²) |
| Overall time | O(n²) |
| Space (excluding output) | O(1) or O(n) depending on sort |

**Time:** The outer loop runs O(n) times. For each iteration, the two-pointer inner scan runs in O(n). Combined: O(n²), which dominates the O(n log n) sort.

**Space:** Python's `sort()` uses Timsort, which is O(n) auxiliary space. The output list itself can hold up to O(n²) triplets in the worst case, but that's output space, not algorithmic space. The working space beyond sorting is O(1).

**Is O(n²) optimal?** Yes. It can be proven that any comparison-based algorithm for 3Sum requires Ω(n²) time in the worst case. Mentioning this shows you've thought about the lower bound, not just the upper bound.

---

## Common Interview Mistakes

1. **Forgetting to sort first.** The entire two-pointer approach depends on sorted order. Without sorting, you can't use directional pointer movement, and duplicate skipping becomes far more complex. Always sort before anything else.

2. **Skipping outer duplicates with the wrong condition.** The guard `if i > 0 and nums[i] == nums[i - 1]` is correct. Using `nums[i] == nums[i + 1]` instead would skip a value *before* processing it, potentially missing valid triplets that start with that value.

3. **Forgetting to skip inner duplicates after a match.** After appending a valid triplet, if you just do `left += 1; right -= 1` without skipping duplicates, you'll append the same triplet multiple times. The inner while loops are not optional.

4. **Moving only one pointer after a match.** After finding a triplet, both `left` and `right` must move. Moving only one leaves the other pointer in a state that causes an infinite loop or missed results.

5. **Not handling the early termination.** Omitting `if nums[i] > 0: break` produces a correct but slower solution. The two-pointer scan runs uselessly for all-positive suffixes. Interviewers may ask about optimizations; having this ready is a good signal.

6. **Confusing the output requirement.** The problem asks for the actual triplet values `[a, b, c]`, not indices. Returning indices (like Two Sum) is a common slip when candidates are moving quickly.

7. **Not narrating the duplicate-handling logic.** The deduplication is the hardest part of this problem to reason about. Candidates who code it silently, even if correctly, miss an opportunity to demonstrate they actually understand *why* it works.

---

## Resources

- **Full Walkthrough**: [3Sum: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/three-sum-interview-walkthrough/)
- **Practice**: [Mock interview for 3Sum](https://intervu.dev/setup2?problem=three-sum)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
