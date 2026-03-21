# Min Stack

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/min-stack-interview-walkthrough/)*

> Master Min Stack for your coding interview. Learn the auxiliary-state pattern for O(1) getMin, two implementation approaches, and what interviewers actually evaluate.

**Difficulty**: Easy
**Patterns**: `stack`, `design`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/min-stack-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=min-stack)**

---

## Problem

Design a stack that supports `push`, `pop`, `top`, and `getMin`, all in O(1) time. `getMin()` must return the minimum element in the stack at any time.

### Example

```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   // → -3
minStack.pop();
minStack.top();      // → 0
minStack.getMin();   // → -2
```

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=min-stack)*

---

## Solution

**Stack of tuples (cleaner):**
```python
class MinStack:
    def __init__(self):
        self.stack = []  # (value, current_min)

    def push(self, val: int) -> None:
        current_min = min(val, self.stack[-1][1]) if self.stack else val
        self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
```

**Two parallel stacks:**
```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = min(val, self.min_stack[-1]) if self.min_stack else val
        self.min_stack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
```

Both are O(1) per operation and O(n) space total.

---

## Complexity

| Operation | Time | Space |
|---|---|---|
| push | O(1) | O(1) per element |
| pop | O(1) |, |
| top | O(1) |, |
| getMin | O(1) |, |
| **Total space** |, | **O(n)** |

---

## Common Interview Mistakes

1. **Storing only the global minimum.** If you pop the minimum, your stored value is now wrong. You need the minimum *at every stack depth*.

2. **Not handling the empty stack edge case in push.** When the stack is empty, `current_min = val` (no previous min to compare against).

3. **Duplicates.** If `-3` is pushed twice and popped once, `getMin` should still return `-3`. Both approaches handle this correctly because they track min per push, not per unique value.

4. **Forgetting both stacks must pop together.** In the two-stack approach, forgetting to pop `min_stack` in `pop()` desyncs them.

---

## Resources

- **Full Walkthrough**: [Min Stack: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/min-stack-interview-walkthrough/)
- **Practice**: [Mock interview for Min Stack](https://intervu.dev/setup2?problem=min-stack)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Basic Calculator](basic-calculator.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/basic-calculator-interview-walkthrough/)
- [Evaluate Reverse Polish Notation](evaluate-reverse-polish-notation.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/evaluate-reverse-polish-notation-interview-walkthrough/)
- [Implement Queue using Stacks](implement-queue-using-stacks.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/implement-queue-using-stacks-interview-walkthrough/)
- [Largest Rectangle in Histogram](largest-rectangle-in-histogram.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/largest-rectangle-in-histogram-interview-walkthrough/)
- [Valid Parentheses](valid-parentheses.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/valid-parentheses-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
