# Word Search

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/word-search-interview-walkthrough/)*

> Master Word Search for your coding interview. Learn the grid DFS + backtracking pattern, in-place visited marking, and what interviewers actually evaluate.

**Difficulty**: Medium
**Patterns**: `backtracking`, `dfs`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/word-search-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=word-search)**

---

## Problem

Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid. The word must be constructed from sequentially adjacent cells (horizontally or vertically). The same cell may not be used more than once.

### Example

**Input:** `board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]`, `word = "ABCCED"`
**Output:** `true`

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=word-search)*

---

## Solution

```python
def exist(board: list[list[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(r: int, c: int, index: int) -> bool:
        if index == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if board[r][c] != word[index]:
            return False

        temp = board[r][c]
        board[r][c] = '#'  # mark visited

        for dr, dc in directions:
            if dfs(r + dr, c + dc, index + 1):
                board[r][c] = temp
                return True

        board[r][c] = temp  # unmark: backtrack
        return False

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False
```

---

## Complexity

| Aspect | Complexity |
|---|---|
| Time | O(m × n × 4^L), L is word length |
| Space | O(L), recursion stack |

---

## Common Interview Mistakes

1. **Not unmarking visited cells.** Other paths can't reuse cells from dead-end branches. Always restore.
2. **Wrong early-exit order.** Check bounds and character match before accessing `board[r][c]`.
3. **Not trying all starting cells.** Must iterate every cell as a potential start.

---

## Resources

- **Full Walkthrough**: [Word Search: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/word-search-interview-walkthrough/)
- **Practice**: [Mock interview for Word Search](https://intervu.dev/setup2?problem=word-search)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Combination Sum](combination-sum.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/combination-sum-interview-walkthrough/)
- [Letter Combinations of a Phone Number](letter-combinations-of-a-phone-number.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/letter-combinations-of-a-phone-number-interview-walkthrough/)
- [Permutations](permutations.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/permutations-interview-walkthrough/)
- [Subsets](subsets.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/subsets-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
