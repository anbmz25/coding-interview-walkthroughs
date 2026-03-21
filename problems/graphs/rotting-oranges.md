# Rotting Oranges

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/rotting-oranges-interview-walkthrough/)*

> Master Rotting Oranges for your coding interview. Learn multi-source BFS, layer-by-layer traversal, and what interviewers actually evaluate.

**Difficulty**: Medium
**Patterns**: `graph`, `bfs`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/rotting-oranges-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=rotting-oranges)**

---

## Problem

You are given an `m x n` integer grid where each cell is:
- `0`, empty
- `1`, fresh orange
- `2`, rotten orange

Every minute, any fresh orange adjacent (4-directionally) to a rotten orange becomes rotten. Return the minimum number of minutes for all fresh oranges to rot, or `-1` if it is impossible.

### Example

**Input:** `[[2,1,1],[1,1,0],[0,1,1]]`
**Output:** `4`

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=rotting-oranges)*

---

## Solution

```python
from collections import deque

def orangesRotting(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh_count += 1

    if fresh_count == 0:
        return 0

    max_minutes = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        r, c, minute = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh_count -= 1
                max_minutes = max(max_minutes, minute + 1)
                queue.append((nr, nc, minute + 1))

    return max_minutes if fresh_count == 0 else -1
```

---

## Complexity

| Aspect | Complexity |
|---|---|
| Time | O(m × n), each cell enqueued at most once |
| Space | O(m × n), queue can hold all cells |

---

## Common Interview Mistakes

1. **Single-source BFS.** Running BFS from each rotten orange separately models sequential spread, not simultaneous. Results are wrong for grids with multiple rotten oranges.

2. **Off-by-one on minutes.** Tracking minutes with a level counter can produce ±1 bugs. Storing the time in the queue entry itself is cleanest.

3. **Not checking for remaining fresh oranges.** BFS completing doesn't mean all oranges are rotten. Check `fresh_count == 0`.

---

## Resources

- **Full Walkthrough**: [Rotting Oranges: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/rotting-oranges-interview-walkthrough/)
- **Practice**: [Mock interview for Rotting Oranges](https://intervu.dev/setup2?problem=rotting-oranges)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [01 Matrix](01-matrix.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/01-matrix-interview-walkthrough/)
- [Accounts Merge](accounts-merge.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/accounts-merge-interview-walkthrough/)
- [Clone Graph](clone-graph.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/clone-graph-interview-walkthrough/)
- [Course Schedule](course-schedule.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/course-schedule-interview-walkthrough/)
- [Flood Fill](flood-fill.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/flood-fill-interview-walkthrough/)
- [Minimum Height Trees](minimum-height-trees.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/minimum-height-trees-interview-walkthrough/)
- [Number of Islands](number-of-islands.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/number-of-islands-interview-walkthrough/)
- [Word Ladder](word-ladder.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/word-ladder-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
