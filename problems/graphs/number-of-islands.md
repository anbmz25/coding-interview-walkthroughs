# Number of Islands

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/number-of-islands-interview-walkthrough/)*

> A step-by-step guide to solving Number of Islands in a coding interview: grid-as-graph modeling, DFS vs BFS tradeoffs, in-place marking, and complexity analysis explained clearly.

**Difficulty**: Medium
**Patterns**: `graphs`, `dfs`, `bfs`, `grid`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/number-of-islands-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=number-of-islands)**

---

## Problem

You are given an `m x n` grid of characters where `'1'` represents land and `'0'` represents water. An **island** is defined as a group of adjacent land cells connected horizontally or vertically (not diagonally). Return the total number of islands in the grid. ([LeetCode #200](https://leetcode.com/problems/number-of-islands/))

### Example

**Input**
```
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1", "medium"]
, "medium"]
```

**Output**
`3`

The first island is the 2x2 block of `'1'`s in the top-left. The second is the single `'1'` in the middle. The third is the two connected `'1'`s in the bottom-right. Cells are only considered connected if they share an edge, diagonal adjacency doesn't count. Counting islands correctly requires both finding unvisited land cells and fully exploring (and marking) each connected component before moving on.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=number-of-islands)*

---

## Solution

### DFS (Recursive): Clean and Concise

```python
def numIslands(grid: list[list[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    island_count = 0

    def dfs(r, c):
        # Base case: out of bounds or not land: stop exploring
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return

        grid[r][c] = '0'  # Sink the cell: mark as visited in-place

        # Explore all 4 neighbors
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                island_count += 1  # Found a new island
                dfs(r, c)          # Sink the entire island

    return island_count
```

### BFS (Iterative): Stack-Safe for Large Grids

```python
from collections import deque

def numIslands(grid: list[list[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    island_count = 0

    def bfs(r, c):
        queue = deque([(r, c)])
        grid[r][c] = '0'  # Mark as visited immediately upon enqueuing

        while queue:
            row, col = queue.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                    grid[nr][nc] = '0'  # Mark before enqueuing to avoid duplicates
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                island_count += 1
                bfs(r, c)

    return island_count
```

Key implementation notes worth calling out in an interview:

- **In the BFS version, mark cells as `'0'` when enqueuing, not when dequeuing.** Marking on dequeue allows the same cell to be enqueued multiple times from different neighbors, causing duplicate processing. Marking on enqueue prevents this.
- **The DFS approach modifies the input grid.** If the interviewer says the grid must be preserved, use a separate `visited = set()` instead and check `(r, c) not in visited` before exploring.
- **The `[(1,0),(-1,0),(0,1),(0,-1)]` direction list** is a reusable pattern across all grid traversal problems, worth memorizing as a convention.
- For very large grids, the recursive DFS may hit Python's default recursion limit. Mentioning this and offering BFS as the stack-safe alternative demonstrates production-level awareness.

---

## Complexity

| Operation | Complexity |
|---|---|
| Time | O(m x n) |
| Space | O(m x n) |

**Time:** Every cell in the grid is visited at most once, either during the outer scan or during a DFS/BFS traversal. Each visit does a constant amount of work. Total: O(m x n).

**Space:** In the worst case (a grid entirely of `'1'`s), the DFS recursion stack can reach O(m x n) depth, or the BFS queue can hold O(m x n) entries. If a separate `visited` set is used instead of in-place marking, space remains O(m x n).

A common interviewer follow-up: *"Can you reduce space?"* The in-place marking approach uses no extra memory beyond the call stack. The stack itself is bounded by O(m x n) in the worst case, and there's no general way to avoid this for graph traversal. Be honest about this rather than over-claiming.

---

## Common Interview Mistakes

1. **Checking bounds after the recursive call rather than before.** In recursive DFS, always validate `r`, `c`, and `grid[r][c]` at the top of the function, returning early if invalid. Checking after causes an `IndexError` before the guard ever fires.

2. **Marking cells as visited after exploring neighbors instead of immediately.** Whether using DFS or BFS, mark a cell the moment you decide to process it, not after. Delayed marking allows the same cell to be enqueued or recursed into multiple times, inflating the count.

3. **Including diagonal neighbors.** The problem specifies 4-directional connectivity. Including diagonals (8 directions) merges islands that should remain separate. Always confirm connectivity rules before coding.

4. **Forgetting the empty grid guard.** `if not grid or not grid[0]` handles both a completely empty list and a list of empty rows. Missing this causes an `IndexError` on `grid[0]` before the traversal even begins.

5. **Not mentioning the input mutation tradeoff.** Modifying the input grid is convenient but destructive. Always flag this explicitly: *"I'm modifying the grid in-place, is that acceptable?"* Proposing a `visited` set as an alternative shows you've thought about both approaches.

6. **Confusing rows and columns in bounds checks.** The condition is `0 <= r < rows and 0 <= c < cols`. Rows bound `r`, columns bound `c`. Swapping them produces subtle bugs that only surface on non-square grids.

7. **Not narrating the graph modeling step.** Candidates who jump straight to "I'll do DFS" without explaining that the grid is an implicit graph where adjacent `'1'`s are connected nodes miss the most important conceptual moment. Always articulate the abstraction before the code.

---

## Resources

- **Full Walkthrough**: [Number of Islands: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/number-of-islands-interview-walkthrough/)
- **Practice**: [Mock interview for Number of Islands](https://intervu.dev/setup2?problem=number-of-islands)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
