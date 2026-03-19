# 01 Matrix

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/01-matrix-interview-walkthrough/)*

> A step-by-step walkthrough of the 01 Matrix problem as it unfolds in a real coding interview. Learn multi-source BFS, why seeding from zeros beats seeding from ones, and how strong candidates explain the approach.

**Difficulty**: Medium
**Patterns**: `bfs`, `matrix`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/01-matrix-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=01-matrix)**

---

## Problem

Given an `m x n` binary matrix `mat`, return a matrix where each cell contains the distance to the nearest `0`. Distance is measured in number of steps horizontally or vertically. ([LeetCode #542](https://leetcode.com/problems/01-matrix/))

### Example 1

**Input**
```
[[0,0,0],
 [0,1,0],
 [0,0,0]]
```

**Output**
```
[[0,0,0],
 [0,1,0],
 [0,0,0]]
```

### Example 2

**Input**
```
[[0,0,0],
 [0,1,0],
 [1,1,1]]
```

**Output**
```
[[0,0,0],
 [0,1,0],
 [1,2,1]]
```

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=01-matrix)*

---

## Solution

```python
from collections import deque

def updateMatrix(mat: list[list[int]]) -> list[list[int]]:
    rows, cols = len(mat), len(mat[0])
    dist = [[float('inf')] * cols for _ in range(rows)]
    queue = deque()

    # Seed all 0 cells with distance 0
    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 0:
                dist[r][c] = 0
                queue.append((r, c))

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if dist[nr][nc] > dist[r][c] + 1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))

    return dist
```

---

## Complexity


---

## Common Interview Mistakes

- **Seeding from 1s instead of 0s.** Multi-source BFS from all 1s searching for 0s requires O(n) BFS per 1-cell, totaling O((m*n)^2). Seed from 0s instead.

- **Not initializing 1-cells to infinity.** Without a sentinel, you can't tell which cells have been finalized. Initializing to `float('inf')` and updating only when an improvement is found is the clean approach.

- **Re-enqueueing cells unnecessarily.** The check `if dist[nr][nc] > dist[r][c] + 1` prevents redundant enqueuing. If the distance can't be improved, skip.

---

## Resources

- **Full Walkthrough**: [01 Matrix: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/01-matrix-interview-walkthrough/)
- **Practice**: [Mock interview for 01 Matrix](https://intervu.dev/setup2?problem=01-matrix)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Accounts Merge](accounts-merge.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/accounts-merge-interview-walkthrough/)
- [Clone Graph](clone-graph.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/clone-graph-interview-walkthrough/)
- [Course Schedule](course-schedule.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/course-schedule-interview-walkthrough/)
- [Flood Fill](flood-fill.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/flood-fill-interview-walkthrough/)
- [Number of Islands](number-of-islands.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/number-of-islands-interview-walkthrough/)
- [Rotting Oranges](rotting-oranges.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/rotting-oranges-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
