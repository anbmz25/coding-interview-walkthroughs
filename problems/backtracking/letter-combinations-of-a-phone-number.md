# Letter Combinations of a Phone Number

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/letter-combinations-of-a-phone-number-interview-walkthrough/)*

> Master Letter Combinations of a Phone Number for your coding interview. Learn the backtracking Cartesian product pattern, the BFS alternative, and what interviewers actually evaluate.

**Difficulty**: Medium
**Patterns**: `backtracking`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/letter-combinations-of-a-phone-number-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=letter-combinations-of-a-phone-number)**

---

## Problem

Given a string containing digits from `2-9`, return all possible letter combinations. Mapping: 2→abc, 3→def, 4→ghi, 5→jkl, 6→mno, 7→pqrs, 8→tuv, 9→wxyz.

### Example

**Input:** `digits = "23"`
**Output:** `["ad","ae","af","bd","be","bf","cd","ce","cf"]`

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=letter-combinations-of-a-phone-number)*

---

## Solution

```python
def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []

    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    results = []
    current = []

    def backtrack(index: int) -> None:
        if index == len(digits):
            results.append(''.join(current))
            return
        for letter in phone_map[digits[index]]:
            current.append(letter)
            backtrack(index + 1)
            current.pop()

    backtrack(0)
    return results
```

---

## Complexity

| Aspect | Complexity |
|---|---|
| Time | O(4ⁿ × n), some keys have 4 letters |
| Space | O(n), recursion stack |

---

## Common Interview Mistakes

1. **Not handling empty input.** Return `[]` for `digits = ""`.
2. **String concatenation instead of list.** Can't efficiently undo `+=`. Use list + `pop()`.
3. **Forgetting the undo step.** `current.pop()` after recursion is essential.

---

## Resources

- **Full Walkthrough**: [Letter Combinations of a Phone Number: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/letter-combinations-of-a-phone-number-interview-walkthrough/)
- **Practice**: [Mock interview for Letter Combinations of a Phone Number](https://intervu.dev/setup2?problem=letter-combinations-of-a-phone-number)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Combination Sum](combination-sum.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/combination-sum-interview-walkthrough/)
- [Permutations](permutations.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/permutations-interview-walkthrough/)
- [Subsets](subsets.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/subsets-interview-walkthrough/)
- [Word Search](word-search.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/word-search-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
