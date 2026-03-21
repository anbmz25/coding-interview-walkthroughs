# Implement Queue using Stacks

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/implement-queue-using-stacks-interview-walkthrough/)*

> Master Implement Queue using Stacks for your coding interview. Learn the two-stack inbox/outbox pattern, amortized O(1) reasoning, and what interviewers actually evaluate.

**Difficulty**: Easy
**Patterns**: `stack`, `design`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/implement-queue-using-stacks-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=implement-queue-using-stacks)**

---

## Problem

Implement a first-in-first-out (FIFO) queue using only two stacks. The queue must support `push`, `pop`, `peek`, and `empty`, all with amortized O(1) time.

### Example

```
MyQueue q = new MyQueue();
q.push(1); q.push(2);
q.peek();  // → 1
q.pop();   // → 1
q.empty(); // → false
```

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=implement-queue-using-stacks)*

---

## Solution

```python
class MyQueue:
    def __init__(self):
        self.in_stack = []   # Receives new elements
        self.out_stack = []  # Serves old elements in FIFO order

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def _transfer(self) -> None:
        """Move all elements from in_stack to out_stack (reverses order)."""
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        self._transfer()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._transfer()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack
```

---

## Complexity

| Operation | Amortized | Worst Case |
|---|---|---|
| push | O(1) | O(1) |
| pop | O(1) | O(n) |
| peek | O(1) | O(n) |
| empty | O(1) | O(1) |

**Amortized argument:** Each element is pushed once → O(1). Each element is transferred at most once → O(1). Each element is popped once → O(1). Total work per element: O(1). Any single `pop` that triggers a transfer is O(n), but those n elements were each pushed once, so the amortized cost per element is still O(1).

---

## Common Interview Mistakes

1. **Transferring on every push.** This gives O(n) push instead of amortized O(1) pop, same total work, but worse distribution and missing the insight.

2. **Not explaining amortized complexity.** Just saying "O(1)" without the amortized argument suggests you don't understand why.

3. **Not implementing `_transfer` as a helper.** Duplicating the transfer logic in `pop` and `peek` leads to bugs.

4. **Wrong empty check.** The queue is empty only when *both* stacks are empty, not just one.

---

## Resources

- **Full Walkthrough**: [Implement Queue using Stacks: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/implement-queue-using-stacks-interview-walkthrough/)
- **Practice**: [Mock interview for Implement Queue using Stacks](https://intervu.dev/setup2?problem=implement-queue-using-stacks)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Basic Calculator](basic-calculator.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/basic-calculator-interview-walkthrough/)
- [Evaluate Reverse Polish Notation](evaluate-reverse-polish-notation.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/evaluate-reverse-polish-notation-interview-walkthrough/)
- [Largest Rectangle in Histogram](largest-rectangle-in-histogram.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/largest-rectangle-in-histogram-interview-walkthrough/)
- [Min Stack](min-stack.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/min-stack-interview-walkthrough/)
- [Valid Parentheses](valid-parentheses.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/valid-parentheses-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
