# Subsets

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/subsets-interview-walkthrough/)*

> Master Subsets for your coding interview. Learn the backtracking snapshot pattern, the recursion tree, and what interviewers actually evaluate.

**Difficulty**: Medium
**Patterns**: `backtracking`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/subsets-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=subsets)**

---

## Problem

Given an integer array `nums` of unique elements, return all possible subsets (the power set). The solution must not contain duplicate subsets.

### Example

**Input:** `nums = [1, 2, 3]`
**Output:** `[[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]`

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=subsets)*

---

## Solution

**Backtracking:**
```python
def subsets(nums: list[int]) -> list[list[int]]:
    results = []
    current = []

    def backtrack(start: int) -> None:
        results.append(list(current))
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1)
            current.pop()

    backtrack(0)
    return results
```

**Iterative:**
```python
def subsets_iterative(nums: list[int]) -> list[list[int]]:
    results = [[]]
    for num in nums:
        results += [subset + [num] for subset in results]
    return results
```

---

## Complexity

| Aspect | Complexity |
|---|---|
| Time | O(n × 2ⁿ), 2ⁿ subsets, each up to length n |
| Space | O(n), recursion stack (not counting output) |

---

## Common Interview Mistakes

1. **Forgetting to copy `current`.** `results.append(current)` appends a reference, all entries point to the same (eventually empty) list. Always `results.append(list(current))`.
2. **Looping from 0 instead of `start`.** Revisiting earlier elements produces duplicates.
3. **Confusing with Subsets II.** Subsets II has duplicate numbers, needs sorting + skip logic. This problem guarantees unique elements.

---

## Resources

- **Full Walkthrough**: [Subsets: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/subsets-interview-walkthrough/)
- **Practice**: [Mock interview for Subsets](https://intervu.dev/setup2?problem=subsets)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Combination Sum](combination-sum.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/combination-sum-interview-walkthrough/)
- [Permutations](permutations.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/permutations-interview-walkthrough/)
- [Word Search](word-search.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/word-search-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
