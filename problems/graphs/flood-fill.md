# Flood Fill

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/flood-fill-interview-walkthrough/)*

> Master Flood Fill for your coding interview. Learn the grid DFS/BFS pattern, boundary handling, infinite loop prevention, and what interviewers actually evaluate.

**Difficulty**: Easy
**Patterns**: `graph`, `dfs`, `bfs`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/flood-fill-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=flood-fill)**

---

## Problem

Given a 2D grid `image`, a starting pixel `(sr, sc)`, and a new color, perform a flood fill starting from `(sr, sc)`. A flood fill changes the color of the starting pixel and all connected pixels of the same original color (4-directional: up, down, left, right).

### Example

**Input:** `image = [[1,1,1],[1,1,0],[1,0,1]]`, sr=1, sc=1, color=2
**Output:** `[[2,2,2],[2,2,0],[2,0,1]]`

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=flood-fill)*

---

## Solution

```python
def floodFill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    original = image[sr][sc]
    if original == color:
        return image  # Avoid infinite loop

    rows, cols = len(image), len(image[0])

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if image[r][c] != original:
            return
        image[r][c] = color  # Paint
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    dfs(sr, sc)
    return image
```

**BFS alternative:**
```python
from collections import deque

def floodFill(image, sr, sc, color):
    original = image[sr][sc]
    if original == color:
        return image

    rows, cols = len(image), len(image[0])
    queue = deque([(sr, sc)])
    image[sr][sc] = color

    while queue:
        r, c = queue.popleft()
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original:
                image[nr][nc] = color
                queue.append((nr, nc))

    return image
```

---

## Complexity

| Aspect | Complexity |
|---|---|
| Time | O(m × n), each cell visited at most once |
| Space | O(m × n), recursion stack or queue |

---

## Common Interview Mistakes

1. **Not handling `original == color`.** This causes infinite recursion in DFS or an infinite loop in BFS. It's the most common bug.

2. **Checking bounds after accessing `image[r][c]`.** Always check bounds first to avoid index errors.

3. **Using 8-directional when 4 is correct.** Ask explicitly: the problem says 4-directional.

4. **Separate visited set.** You don't need one: the color change itself prevents revisiting. Adding one wastes space.

---

## Resources

- **Full Walkthrough**: [Flood Fill: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/flood-fill-interview-walkthrough/)
- **Practice**: [Mock interview for Flood Fill](https://intervu.dev/setup2?problem=flood-fill)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [01 Matrix](01-matrix.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/01-matrix-interview-walkthrough/)
- [Accounts Merge](accounts-merge.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/accounts-merge-interview-walkthrough/)
- [Course Schedule](course-schedule.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/course-schedule-interview-walkthrough/)
- [Number of Islands](number-of-islands.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/number-of-islands-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
