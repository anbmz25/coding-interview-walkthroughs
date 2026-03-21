# Minimum Height Trees

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/minimum-height-trees-interview-walkthrough/)*

> A step-by-step walkthrough of the Minimum Height Trees problem as it unfolds in a real coding interview. Learn the leaf-trimming algorithm, why MHT roots are always the tree's center nodes, and how to implement the solution in O(n).

**Difficulty**: Medium
**Patterns**: `graph`, `bfs`, `minimum-height-trees`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/minimum-height-trees-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=minimum-height-trees)**

---

## Problem

Given a tree of `n` nodes labeled `0` to `n-1` as an undirected graph (edges), find all nodes that form roots of Minimum Height Trees (MHTs). Trees with those roots have the minimum possible height. There are at most 2 such roots. ([LeetCode #310](https://leetcode.com/problems/minimum-height-trees/))

### Example 1

**Input**
`n = 4`, `edges = [[1,0],[1,2],[1,3]]`

**Output**
`[1]`

Node 1 is the center. Rooting the tree at node 1 gives height 1. Rooting at any leaf (0, 2, or 3) gives height 2.

### Example 2

**Input**
`n = 6`, `edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]`

**Output**
`[3, 4]`

Both nodes 3 and 4 are centers. They're adjacent, each giving a tree of height 2.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=minimum-height-trees)*

---

## Solution

```python
from collections import defaultdict, deque

def findMinHeightTrees(n: int, edges: list[list[int]]) -> list[int]:
    if n == 1:
        return [0]

    adj = defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)

    # Initialize leaves (degree 1)
    leaves = deque([node for node in range(n) if len(adj[node]) == 1])
    remaining = n

    while remaining > 2:
        remaining -= len(leaves)
        new_leaves = deque()
        for leaf in leaves:
            neighbor = adj[leaf].pop()
            adj[neighbor].discard(leaf)
            if len(adj[neighbor]) == 1:
                new_leaves.append(neighbor)
        leaves = new_leaves

    return list(leaves)
```

Why this is interview-friendly:

- **Set-based adjacency for O(1) removal.** Using `set` instead of `list` makes `discard` O(1). With a list, removal is O(degree).
- **`remaining > 2` as the loop condition.** This correctly handles both odd-diameter (1 center) and even-diameter (2 centers) cases.
- **Each node is processed exactly once as a leaf.** The algorithm never revisits nodes.

---

## Complexity

| | Time | Space |
|---|---|---|
| Minimum Height Trees | O(n) | O(n) |

Each node is removed as a leaf exactly once. Building the adjacency sets is O(n). Total work is linear.

---

## Common Interview Mistakes

1. **Not handling `n == 1`.** A single node has no edges. The leaf-finding loop produces an empty list. Return `[0]` explicitly.

2. **Brute-forcing BFS from every node.** Running BFS from each node to measure height is O(n^2). The leaf-trimming approach is O(n). Always mention the brute force first, then explain why it's too slow.

3. **Stopping at `remaining == 1` only.** Stop when `remaining <= 2`. Two nodes can both be MHT roots when they're equidistant from both ends of the diameter.

4. **Using a list instead of a set for adjacency.** Removal from a list is O(degree), making the overall algorithm O(n * max_degree). Use `set()` for O(1) removal.

5. **Not counting `remaining` correctly.** Decrement `remaining` by the number of leaves before processing them. If you decrement inside the leaf-processing loop, you'll stop one round too early or too late.

---

## Resources

- **Full Walkthrough**: [Minimum Height Trees: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/minimum-height-trees-interview-walkthrough/)
- **Practice**: [Mock interview for Minimum Height Trees](https://intervu.dev/setup2?problem=minimum-height-trees)
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
- [Number of Islands](number-of-islands.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/number-of-islands-interview-walkthrough/)
- [Rotting Oranges](rotting-oranges.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/rotting-oranges-interview-walkthrough/)
- [Word Ladder](word-ladder.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/word-ladder-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
