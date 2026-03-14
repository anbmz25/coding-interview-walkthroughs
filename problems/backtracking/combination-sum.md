# Combination Sum

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/combination-sum-interview-walkthrough/)*

> A step-by-step walkthrough of LeetCode #39 as it plays out in a real coding interview. Learn the backtracking decision tree, the choose/explore/unchoose pattern, and the pruning techniques that separate clean solutions from broken ones.

**Difficulty**: Medium
**Patterns**: `backtracking`, `recursion`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/combination-sum-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=combination-sum)**

---

## Problem

Given an array of **distinct** positive integers `candidates` and a target integer `target`, return a list of all **unique combinations** of candidates that sum to `target`. The same number may be chosen from `candidates` an **unlimited number of times**. The solution set must not contain duplicate combinations.

([LeetCode #39](https://leetcode.com/problems/combination-sum/))

### Example 1

**Input**
`candidates = [2, 3, 6, 7], target = 7`

**Output**
`[[2, 2, 3], [7]]`

### Example 2

**Input**
`candidates = [2, 3, 5], target = 8`

**Output**
`[[2, 2, 2, 2], [2, 3, 3], [3, 5]]`

In Example 1, there are exactly two ways to sum to `7` using elements from the array: picking `2` twice and `3` once, or picking `7` once. In Example 2, `2` can be reused four times, or combined with two `3`s, or paired with `5`. The order within each combination doesn't matter: `[2, 3, 3]` and `[3, 2, 3]` are the same combination and should only appear once in the output.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=combination-sum)*

---

## Solution

```python
def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    results = []
    candidates.sort()  # Sorting enables early break pruning

    def backtrack(start: int, current_combo: list[int], remaining: int):
        # Base case: exact match found
        if remaining == 0:
            results.append(list(current_combo))  # Append a copy, not the reference
            return

        for i in range(start, len(candidates)):
            # Since candidates are sorted, all further values will also exceed remaining
            if candidates[i] > remaining:
                break

            # Choose: add this candidate to the current combination
            current_combo.append(candidates[i])

            # Explore: recurse with same index i (allows reuse of candidates[i])
            backtrack(i, current_combo, remaining - candidates[i])

            # Unchoose: remove the candidate to restore state for the next iteration
            current_combo.pop()

    backtrack(0, [], target)
    return results
```

The three-step structure inside the loop, **choose, explore, unchoose**, is the canonical backtracking pattern. Naming it explicitly to an interviewer signals you understand the pattern, not just this specific problem.

Let's trace `candidates = [2, 3, 6, 7], target = 7`:

- `backtrack(0, [], 7)` → pick `2` → `backtrack(0, [2], 5)`
  - pick `2` → `backtrack(0, [2,2], 3)`
    - pick `2` → `backtrack(0, [2,2,2], 1)`
      - pick `2` → 2 > 1 → break
    - pick `3` → `backtrack(1, [2,2,3], 0)` → **result: [2,2,3]** ✓
    - pick `6` → 6 > 3 → break
  - pick `3` → `backtrack(1, [2,3], 2)`
    - pick `3` → 3 > 2 → break
  - pick `6` → 6 > 5 → break
- pick `3` → `backtrack(1, [3], 4)`
  - pick `3` → `backtrack(1, [3,3], 1)`
    - pick `3` → 3 > 1 → break
  - pick `6` → 6 > 4 → break
- pick `6` → `backtrack(2, [6], 1)`
  - pick `6` → 6 > 1 → break
- pick `7` → `backtrack(3, [7], 0)` → **result: [7]** ✓

Final output: `[[2, 2, 3], [7]]` ✓

---

## Complexity

| Aspect | Complexity | Explanation |
|---|---|---|
| Time | O(n^(T/M)) | n = candidates length, T = target, M = smallest candidate |
| Space (call stack) | O(T/M) | Maximum recursion depth is target divided by the smallest candidate |
| Space (output) | O(k × T/M) | k = number of valid combinations, each up to length T/M |

**Time:** The bound O(n^(T/M)) captures the worst-case branching factor (n choices at each level) and maximum depth (T/M levels). In practice, pruning makes the actual runtime significantly faster than this bound.

**Space:** The recursion depth is bounded by T/M. Each level of recursion uses O(1) additional space beyond the combination being built.

---

## Common Interview Mistakes

1. **Passing `i + 1` instead of `i` in the recursive call.** This is the single most common bug. Using `i + 1` means each candidate can only be used once, producing wrong results for cases like `[2, 2, 2, 2]`. The whole point of this problem is unlimited reuse: you stay at index `i` when recursing.

2. **Appending `current_combo` directly instead of a copy.** Writing `results.append(current_combo)` appends a reference to the list, not a snapshot. As backtracking unwinds and modifies `current_combo`, every entry in `results` gets mutated. Always append `list(current_combo)` or `current_combo[:]`.

3. **Forgetting the undo step.** Backtracking requires explicitly undoing each choice before the next iteration. Forgetting `current_combo.pop()` means the list grows monotonically across recursive calls and produces completely wrong combinations.

4. **Starting the inner loop from `0` instead of `start`.** Starting from `0` each time means you'll generate both `[2, 3]` and `[3, 2]`, duplicate combinations that differ only in order. The `start` parameter exists specifically to prevent this.

5. **Not sorting before pruning with `break`.** The `break` optimization relies on the candidates being in ascending order. If you skip the sort, a smaller candidate appearing after a larger one would be incorrectly skipped.

6. **Trying to code before sketching the decision tree.** Backtracking problems have many moving parts. Candidates who jump straight to code almost always get the index management or undo step wrong. Drawing even a two-level decision tree takes 90 seconds and prevents most bugs.

7. **Checking `remaining < 0` instead of using `> remaining` in the loop guard.** Separating the success case (`== 0`) from the pruning (`candidates[i] > remaining` with break) is cleaner and less error-prone.

---

## Resources

- **Full Walkthrough**: [Combination Sum: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/combination-sum-interview-walkthrough/)
- **Practice**: [Mock interview for Combination Sum](https://intervu.dev/setup2?problem=combination-sum)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Permutations](permutations.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/permutations-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
