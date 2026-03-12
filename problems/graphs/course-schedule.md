# Course Schedule

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/course-schedule-interview-walkthrough/)*

> A step-by-step guide to solving Course Schedule in a coding interview. Learn DFS three-state cycle detection on directed graphs, common mistakes, and what interviewers actually score you on.

**Difficulty**: Medium
**Patterns**: `graphs`, `dfs`, `topological-sort`, `grind-75`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/course-schedule-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=course-schedule)**

---

## Problem

You are given `numCourses` courses labeled `0` to `numCourses - 1`, and a list of prerequisite pairs. Each pair `[a, b]` means you must take course `b` before you can take course `a`. Return `true` if it's possible to finish all courses, or `false` if it's not.

A situation where it's *not* possible would be if two courses require each other, a circular dependency that makes it impossible to ever start.

### Example

**Input**
`numCourses = 2, prerequisites = [[1, 0]]`

**Output**
`true`

Here, course `1` requires course `0`. You can take `0` first, then `1`. There's no cycle, so it's possible to complete everything.

**Input**
`numCourses = 2, prerequisites = [[1, 0], [0, 1]]`

**Output**
`false`

Now course `1` requires `0` and course `0` requires `1`. They're mutually dependent, so you return `false`. ([LeetCode #207](https://leetcode.com/problems/course-schedule/))

*Already comfortable with the solution? [Practice it in a mock interview ->](https://intervu.dev/setup2?problem=course-schedule)*

---

## Solution

```python
from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list: course -> list of prerequisites
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        # 0 = unvisited, 1 = visiting (in current DFS path), 2 = visited (safe)
        state = [0] * numCourses

        def has_cycle(node: int) -> bool:
            if state[node] == 1:
                return True   # Back edge detected: cycle found
            if state[node] == 2:
                return False  # Already confirmed safe: skip

            state[node] = 1  # Mark as currently being explored

            for neighbor in graph[node]:
                if has_cycle(neighbor):
                    return True  # Propagate cycle detection upward

            state[node] = 2  # Mark as fully explored: no cycle from here
            return False

        # Check every node: graph may be disconnected
        for course in range(numCourses):
            if state[course] == 0:
                if has_cycle(course):
                    return False

        return True
```

The `defaultdict(list)` handles courses with no prerequisites cleanly. The explicit `state` array is cleaner than using a visited set because it distinguishes the three states needed for cycle detection.

---

## Complexity

| Operation | Complexity |
|---|---|
| Building the adjacency list | O(E), one pass over prerequisites |
| DFS traversal (each node visited once) | O(V) |
| Processing all edges across DFS | O(E) |
| **Overall Time** | **O(V + E)** |
| **Overall Space** | **O(V + E)**, graph storage + recursion stack |

Here, V = `numCourses` and E = `len(prerequisites)`. Each node is visited at most once (the `state == 2` check prevents re-processing), and each edge is traversed at most once.

---

## Common Interview Mistakes

1. **Using only two states instead of three** Many candidates use a simple `visited` boolean. This can't distinguish "currently on the DFS path" from "already fully processed," causing false cycle detections or missing real ones. You *need* the `visiting` state.

2. **Getting the edge direction backwards** If the problem says `[a, b]` means "a requires b," some candidates add `b -> a` instead of `a -> b`. Draw the graph explicitly before coding.

3. **Only traversing from node 0** If you start DFS only from `course 0`, you'll miss disconnected components. Always iterate over all nodes.

4. **Forgetting courses with no prerequisites** Courses not in `prerequisites` still exist in the graph. They just have no outgoing edges. Your code must not crash when `graph[node]` is empty.

5. **Coding immediately without drawing the graph** On a whiteboard, sketch the graph for the examples before writing code. This catches edge-direction mistakes early.

6. **Not explaining the three-state logic verbally** If you write the `state` array without explaining why three values are needed, the interviewer may assume you memorized the solution.

7. **Confusing this with undirected graph cycle detection** Undirected cycle detection only needs two states. Directed graphs require three. If you conflate the two, you'll give an incorrect solution.

---

## Resources

- **Full Walkthrough**: [Course Schedule: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/course-schedule-interview-walkthrough/)
- **Practice**: [Mock interview for Course Schedule](https://intervu.dev/setup2?problem=course-schedule)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
