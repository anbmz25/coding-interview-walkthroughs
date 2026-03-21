# Task Scheduler

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/task-scheduler-interview-walkthrough/)*

> A step-by-step walkthrough of the Task Scheduler problem as it unfolds in a real coding interview. Learn the greedy formula approach, the heap-based simulation alternative, and how strong candidates derive the scheduling formula from first principles.

**Difficulty**: Medium
**Patterns**: `greedy`, `heap`, `task-scheduler`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/task-scheduler-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=task-scheduler)**

---

## Problem

You are given an array `tasks` of CPU tasks, each labeled `A` to `Z`. Between two tasks of the same type, there must be at least `n` intervals of cooldown (idle or other tasks). Return the minimum number of intervals needed to finish all tasks. ([LeetCode #621](https://leetcode.com/problems/task-scheduler/))

### Example 1

**Input**
`tasks = ["A","A","A","B","B","B"]`, `n = 2`

**Output**
`8`

Schedule: `A -> B -> idle -> A -> B -> idle -> A -> B`

### Example 2

**Input**
`tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]`, `n = 2`

**Output**
`16`

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=task-scheduler)*

---

## Solution

```python
from collections import Counter

def leastInterval(tasks: list[str], n: int) -> int:
    counts = Counter(tasks)
    max_count = max(counts.values())
    max_count_tasks = sum(1 for c in counts.values() if c == max_count)

    formula = (max_count - 1) * (n + 1) + max_count_tasks
    return max(formula, len(tasks))
```

Why this is interview-friendly:

- **Four lines of logic.** Count frequencies, find the max, count how many tasks share that max, apply the formula. Clean and auditable.
- **No simulation needed.** The formula captures the entire scheduling structure without stepping through time units.
- **The `max()` at the end handles the dense case.** When there are so many distinct tasks that all idle slots get filled, the answer is just `len(tasks)`.

---

## Complexity

| | Time | Space |
|---|---|---|
| Formula | O(n) | O(26) = O(1) |
| Heap simulation | O(total_intervals * log 26) = O(n) | O(26) = O(1) |

Both are effectively O(n) with O(1) space since the alphabet is fixed at 26 characters.

---

## Common Interview Mistakes

1. **Forgetting `max(formula, len(tasks))`.** When there are many diverse tasks, idle slots disappear entirely. The formula can undercount. Always cap it at `len(tasks)`.

2. **Not counting tasks with `max_count` correctly.** If both A and B appear 3 times and `n = 2`, the last frame has both A and B, not just one. `max_count_tasks` must count how many task types share the maximum frequency.

3. **Simulating per-step without a heap.** Greedy simulation without a priority queue runs in O(n * 26) per time unit, is harder to implement, and more error-prone.

4. **Confusing `n` with `n+1`.** The frame size is `n + 1` (the task itself plus `n` cooldown slots), not `n`. This off-by-one changes the entire formula.

---

## Resources

- **Full Walkthrough**: [Task Scheduler: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/task-scheduler-interview-walkthrough/)
- **Practice**: [Mock interview for Task Scheduler](https://intervu.dev/setup2?problem=task-scheduler)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Best Time to Buy and Sell Stock](best-time-to-buy-and-sell-stock.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/best-time-to-buy-and-sell-stock-interview-walkthrough/)
- [Container With Most Water](container-with-most-water.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/container-with-most-water-interview-walkthrough/)
- [Contains Duplicate](contains-duplicate.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/contains-duplicate-interview-walkthrough/)
- [Find All Anagrams in a String](find-all-anagrams-in-a-string.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/find-all-anagrams-in-a-string-interview-walkthrough/)
- [Find Median from Data Stream](find-median-from-data-stream.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/find-median-from-data-stream-interview-walkthrough/)
- [Insert Interval](insert-interval.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/insert-interval-interview-walkthrough/)
- [K Closest Points to Origin](k-closest-points-to-origin.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/k-closest-points-to-origin-interview-walkthrough/)
- [Longest Palindrome](longest-palindrome.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/longest-palindrome-interview-walkthrough/)
- [Majority Element](majority-element.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/majority-element-interview-walkthrough/)
- [Maximum Subarray](maximum-subarray.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/maximum-subarray-interview-walkthrough/)
- [Meeting Rooms](meeting-rooms.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/meeting-rooms-interview-walkthrough/)
- [Merge Intervals](merge-intervals.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/merge-intervals-interview-walkthrough/)
- [Product of Array Except Self](product-of-array-except-self.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/product-of-array-except-self-interview-walkthrough/)
- [Ransom Note](ransom-note.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/ransom-note-interview-walkthrough/)
- [Sort Colors](sort-colors.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/sort-colors-interview-walkthrough/)
- [Spiral Matrix](spiral-matrix.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/spiral-matrix-interview-walkthrough/)
- [3Sum](three-sum.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/three-sum-interview-walkthrough/)
- [Trapping Rain Water](trapping-rain-water.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/trapping-rain-water-interview-walkthrough/)
- [Two Sum](two-sum.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/two-sum-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
