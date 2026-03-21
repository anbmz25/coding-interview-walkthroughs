# Largest Rectangle in Histogram

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/largest-rectangle-in-histogram-interview-walkthrough/)*

> A step-by-step walkthrough of the Largest Rectangle in Histogram problem as it unfolds in a real coding interview. Learn the monotonic stack approach, the sentinel trick, and how to correctly compute rectangle widths.

**Difficulty**: Hard
**Patterns**: `stack`, `monotonic-stack`, `largest-rectangle-in-histogram`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/largest-rectangle-in-histogram-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=largest-rectangle-in-histogram)**

---

## Problem

Given an array of integers `heights` representing the heights of bars in a histogram (each bar has width 1), return the area of the largest rectangle that can be formed within the histogram. ([LeetCode #84](https://leetcode.com/problems/largest-rectangle-in-histogram/))

### Example 1

**Input**
`heights = [2,1,5,6,2,3]`

**Output**
`10`

The largest rectangle spans bars at indices 2 and 3 (heights 5 and 6), limited by height 5, giving area `5 * 2 = 10`.

### Example 2

**Input**
`heights = [2,4]`

**Output**
`4`

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=largest-rectangle-in-histogram)*

---

## Solution

```python
def largestRectangleArea(heights: list[int]) -> int:
    heights = heights + [0]  # sentinel to flush all bars
    stack = []  # monotonic increasing stack of indices
    max_area = 0

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            left = stack[-1] if stack else -1
            width = i - left - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area
```

Why this is interview-friendly:

- **Sentinel eliminates special-case handling.** The trailing `0` forces all remaining bars to be popped from the stack. Without it, you'd need a separate pass after the main loop.
- **Each bar pushed and popped exactly once.** Despite the nested `while`, the total work is O(n).
- **Width formula is compact.** `i - left - 1` where `left` is the new stack top (or -1 if empty). This covers all cases.

---

## Complexity

| | Time | Space |
|---|---|---|
| Largest Rectangle in Histogram | O(n) | O(n) |

Each bar is pushed onto and popped from the stack at most once. The stack holds at most n indices.

---

## Common Interview Mistakes

1. **Not appending the sentinel 0.** Without the trailing 0, bars that are never followed by a shorter bar never get popped. You'd miss rectangles involving the tallest bars. The sentinel forces all remaining bars to be processed.

2. **Wrong width formula.** When popping index `h_idx`, the left boundary is the new top of the stack (the last bar shorter than `heights[h_idx]`), and the right boundary is `i`. Width = `i - stack[-1] - 1` (or `i - (-1) - 1 = i` if the stack is empty).

3. **Confusing index vs. height on the stack.** Push indices onto the stack, not heights. You need both the index (for width calculation) and the height (from `heights[idx]`).

4. **Not mentioning brute force first.** Always state the brute-force (try every bar as the limiting height: O(n^2)) before the stack solution. This shows structured thinking and makes the O(n) solution more impressive.

---

## Resources

- **Full Walkthrough**: [Largest Rectangle in Histogram: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/largest-rectangle-in-histogram-interview-walkthrough/)
- **Practice**: [Mock interview for Largest Rectangle in Histogram](https://intervu.dev/setup2?problem=largest-rectangle-in-histogram)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Basic Calculator](basic-calculator.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/basic-calculator-interview-walkthrough/)
- [Evaluate Reverse Polish Notation](evaluate-reverse-polish-notation.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/evaluate-reverse-polish-notation-interview-walkthrough/)
- [Implement Queue using Stacks](implement-queue-using-stacks.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/implement-queue-using-stacks-interview-walkthrough/)
- [Min Stack](min-stack.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/min-stack-interview-walkthrough/)
- [Valid Parentheses](valid-parentheses.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/valid-parentheses-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
