# Clone Graph

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/clone-graph-interview-walkthrough/)*

> Master Clone Graph for your coding interview. Learn the DFS clone-map pattern, cycle handling, and what interviewers actually evaluate.

**Difficulty**: Medium
**Patterns**: `graph`, `dfs`, `bfs`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/clone-graph-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=clone-graph)**

---

## Problem

Given a reference to a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node contains a `val` (integer) and a `neighbors` list (list of adjacent nodes).

### Example

**Input:** `adjList = [[2,4],[1,3],[2,4],[1,3]]`
**Output:** A deep copy of the graph with the same adjacency structure.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=clone-graph)*

---

## Solution

**DFS (recursive):**
```python
def cloneGraph(node: Node) -> Node:
    if not node:
        return None

    cloned = {}

    def dfs(original: Node) -> Node:
        if original in cloned:
            return cloned[original]

        clone = Node(original.val)
        cloned[original] = clone  # Register BEFORE recursing

        for neighbor in original.neighbors:
            clone.neighbors.append(dfs(neighbor))

        return clone

    return dfs(node)
```

**BFS (iterative):**
```python
from collections import deque

def cloneGraph_bfs(node: Node) -> Node:
    if not node:
        return None

    cloned = {node: Node(node.val)}
    queue = deque([node])

    while queue:
        current = queue.popleft()
        for neighbor in current.neighbors:
            if neighbor not in cloned:
                cloned[neighbor] = Node(neighbor.val)
                queue.append(neighbor)
            cloned[current].neighbors.append(cloned[neighbor])

    return cloned[node]
```

---

## Complexity

| Aspect | Complexity |
|---|---|
| Time | O(V + E), each node and edge visited once |
| Space | O(V), clone map holds one entry per node |

---

## Common Interview Mistakes

1. **Registering the clone after recursion.** If you add the clone to `cloned` only after processing neighbors, any cycle recurses infinitely. Register immediately after creation.

2. **Shallow copying neighbors.** Appending the *original* neighbor objects gives you a shallow copy. You must append the *cloned* neighbor.

3. **Not handling `None`.** Return `None` before accessing any properties.

4. **Using `node.val` as key instead of the node object.** Works here because values are unique, but it's fragile for variants.

---

## Resources

- **Full Walkthrough**: [Clone Graph: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/clone-graph-interview-walkthrough/)
- **Practice**: [Mock interview for Clone Graph](https://intervu.dev/setup2?problem=clone-graph)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [01 Matrix](01-matrix.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/01-matrix-interview-walkthrough/)
- [Accounts Merge](accounts-merge.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/accounts-merge-interview-walkthrough/)
- [Course Schedule](course-schedule.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/course-schedule-interview-walkthrough/)
- [Flood Fill](flood-fill.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/flood-fill-interview-walkthrough/)
- [Number of Islands](number-of-islands.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/number-of-islands-interview-walkthrough/)
- [Rotting Oranges](rotting-oranges.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/rotting-oranges-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
