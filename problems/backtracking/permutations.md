# Permutations

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/permutations-interview-walkthrough/)*

> A step-by-step walkthrough of LeetCode #46 as it plays out in a real coding interview. Learn the used-array backtracking pattern, why it differs from combination problems, and the swap-based alternative that saves space.

**Difficulty**: Medium
**Patterns**: `backtracking`, `recursion`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/permutations-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=permutations)**

---

## Problem

Given an array `nums` of **distinct** integers, return all possible permutations. You may return the answer in **any order**.

([LeetCode #46](https://leetcode.com/problems/permutations/))

### Example 1

**Input**
`nums = [1, 2, 3]`

**Output**
`[[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]`

### Example 2

**Input**
`nums = [0, 1]`

**Output**
`[[0,1], [1,0]]`

In Example 1, there are 3! = 6 permutations of three distinct elements: every possible ordering appears exactly once. Unlike combinations, **order matters** here: `[1, 2, 3]` and `[2, 1, 3]` are different permutations. Every element must appear in every permutation exactly once.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=permutations)*

---

## Solution

```python
def permute(nums: list[int]) -> list[list[int]]:
    results = []
    used = [False] * len(nums)  # Tracks which elements are in the current permutation

    def backtrack(current_perm: list[int]):
        # Base case: current permutation is complete
        if len(current_perm) == len(nums):
            results.append(list(current_perm))  # Append a copy, not the reference
            return

        for i in range(len(nums)):
            if used[i]:
                continue  # Skip elements already in this permutation

            # Choose
            used[i] = True
            current_perm.append(nums[i])

            # Explore
            backtrack(current_perm)

            # Unchoose
            current_perm.pop()
            used[i] = False

    backtrack([])
    return results
```

Let's trace `nums = [1, 2, 3]`:

```
backtrack([])
├── pick 1 → backtrack([1])
│   ├── pick 2 → backtrack([1,2])
│   │   └── pick 3 → backtrack([1,2,3]) → ✓ append [1,2,3]
│   └── pick 3 → backtrack([1,3])
│       └── pick 2 → backtrack([1,3,2]) → ✓ append [1,3,2]
├── pick 2 → backtrack([2])
│   ├── pick 1 → backtrack([2,1])
│   │   └── pick 3 → backtrack([2,1,3]) → ✓ append [2,1,3]
│   └── pick 3 → backtrack([2,3])
│       └── pick 1 → backtrack([2,3,1]) → ✓ append [2,3,1]
└── pick 3 → backtrack([3])
    ├── pick 1 → backtrack([3,1])
    │   └── pick 2 → backtrack([3,1,2]) → ✓ append [3,1,2]
    └── pick 2 → backtrack([3,2])
        └── pick 1 → backtrack([3,2,1]) → ✓ append [3,2,1]
```

All 3! = 6 permutations collected. The `used` flags ensure no element appears twice in any path from root to leaf.

### Bonus: In-Place Swap Approach

```python
def permute_swap(nums: list[int]) -> list[list[int]]:
    results = []

    def backtrack(start: int):
        if start == len(nums):
            results.append(list(nums))
            return

        for i in range(start, len(nums)):
            # Swap nums[i] into the current position
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            # Swap back to restore original order
            nums[start], nums[i] = nums[i], nums[start]

    backtrack(0)
    return results
```

This approach treats `nums` itself as the "current permutation" by swapping elements into place. It uses O(1) extra space beyond the output and call stack. The tradeoff: it's slightly harder to explain verbally and easier to get the swap indices wrong.

---

## Complexity

| Aspect | Complexity | Explanation |
|---|---|---|
| Time | O(n! x n) | n! permutations, copying each takes O(n) |
| Space (call stack) | O(n) | Recursion depth is exactly n |
| Space (`used` array) | O(n) | One boolean per element |
| Space (output) | O(n! x n) | Storing all permutations |

**Time:** O(n! x n) is unavoidable. You can't enumerate n! permutations faster than O(n!), and each copy costs O(n). The backtracking itself does no redundant work; every leaf in the decision tree corresponds to exactly one permutation.

**Space:** The recursion depth is exactly n (one level per element placed).

---

## Common Interview Mistakes

1. **Using a start index instead of a `used` array.** This is the combination-problem habit bleeding into a permutation problem. A start index prevents you from placing `1` after `2`: you'd miss `[2, 1, 3]` entirely. Permutations require every unused element to be available at every position.

2. **Appending `current_perm` directly instead of a copy.** `results.append(current_perm)` stores a reference. As backtracking modifies the list, every stored result changes with it. You'll end up with a list of identical empty lists. Always append `list(current_perm)`.

3. **Forgetting to reset `used[i]` after the recursive call.** The undo step must reset both the list (`pop`) and the flag (`used[i] = False`). Forgetting the flag reset means once an element is used in one branch, it stays marked used for all subsequent branches.

4. **Checking `len(current_perm) == n` with the wrong `n`.** If you shadow `n` somewhere or use `len(nums)` inconsistently, the base case can silently trigger too early or too late.

5. **Getting the swap indices wrong in the swap approach.** You swap `nums[start]` with `nums[i]`, not `nums[i]` with `nums[i+1]`. Confusing the "current position" (`start`) with the "candidate" (`i`) produces wrong or duplicate permutations.

6. **Not drawing the decision tree before coding.** Permutations have a clean, symmetric decision tree that's easy to sketch. Spending 60 seconds drawing the first two levels for `[1, 2, 3]` prevents most bugs.

7. **Treating this problem like Combination Sum.** The two problems look structurally similar but differ in a key way: combinations avoid revisiting earlier candidates using a start index; permutations need to revisit all elements using a used-tracking mechanism.

---

## Resources

- **Full Walkthrough**: [Permutations: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/permutations-interview-walkthrough/)
- **Practice**: [Mock interview for Permutations](https://intervu.dev/setup2?problem=permutations)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Combination Sum](combination-sum.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/combination-sum-interview-walkthrough/)
- [Subsets](subsets.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/subsets-interview-walkthrough/)
- [Word Search](word-search.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/word-search-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
