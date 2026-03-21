# Word Ladder

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/word-ladder-interview-walkthrough/)*

> A step-by-step walkthrough of the Word Ladder problem as it unfolds in a real coding interview. Learn why BFS is the right tool, the neighbor-generation trick, and how bidirectional BFS cuts the search space.

**Difficulty**: Hard
**Patterns**: `graph`, `bfs`, `word-ladder`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/word-ladder-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=word-ladder)**

---

## Problem

Given `beginWord`, `endWord`, and a `wordList`, return the number of words in the shortest transformation sequence from `beginWord` to `endWord`, where each step changes exactly one letter and the resulting word must be in `wordList`. Return `0` if no sequence exists. ([LeetCode #127](https://leetcode.com/problems/word-ladder/))

### Example 1

**Input**
`beginWord = "hit"`, `endWord = "cog"`, `wordList = ["hot","dot","dog","lot","log","cog"]`

**Output**
`5`

Transformation: `hit -> hot -> dot -> dog -> cog`

### Example 2

**Input**
`beginWord = "hit"`, `endWord = "cog"`, `wordList = ["hot","dot","dog","lot","log"]`

**Output**
`0` (`"cog"` is not in the word list)

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=word-ladder)*

---

## Solution

```python
from collections import deque

def ladderLength(beginWord: str, endWord: str, wordList: list[str]) -> int:
    word_set = set(wordList)
    if endWord not in word_set:
        return 0

    queue = deque([(beginWord, 1)])
    visited = {beginWord}

    while queue:
        word, length = queue.popleft()

        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                if next_word == endWord:
                    return length + 1
                if next_word in word_set and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, length + 1))

    return 0
```

Why this is interview-friendly:

- **Set-based lookup is O(1).** Converting the word list to a set is the key optimization.
- **Early return on `endWord`.** No need to process the entire level.
- **`visited` prevents revisiting.** Adding to `visited` on enqueue (not dequeue) prevents duplicates from entering the queue.

**Follow-up: Bidirectional BFS.** BFS from both `beginWord` and `endWord` simultaneously. When the two frontiers meet, return the combined length. This reduces the search space from O(b^d) to O(b^(d/2)), a significant speedup for large dictionaries.

---

## Complexity

| | Time | Space |
|---|---|---|
| BFS | O(M^2 * N) | O(M * N) |

`M` = word length, `N` = number of words. For each word, we generate `M * 26` candidates. Each candidate construction is O(M) for string slicing.

---

## Common Interview Mistakes

1. **Using DFS instead of BFS.** DFS finds *a* path but not the *shortest* path. BFS guarantees shortest path in an unweighted graph.

2. **Not removing words from the set after visiting.** Without this, BFS can revisit words, creating cycles and infinite loops. Mark words as visited when they're enqueued, not when they're dequeued.

3. **Not checking `endWord in wordList` upfront.** If `endWord` isn't in the word list, no path exists. Return 0 immediately instead of running the full BFS.

4. **Comparing every word in the list to find neighbors.** O(n * L) per BFS node. Generating 26 * L candidates and checking the set is faster for large word lists.

---

## Resources

- **Full Walkthrough**: [Word Ladder: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/word-ladder-interview-walkthrough/)
- **Practice**: [Mock interview for Word Ladder](https://intervu.dev/setup2?problem=word-ladder)
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
- [Rotting Oranges](rotting-oranges.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/rotting-oranges-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
