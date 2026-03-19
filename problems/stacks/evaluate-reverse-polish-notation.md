# Evaluate Reverse Polish Notation

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/evaluate-reverse-polish-notation-interview-walkthrough/)*

> Master Evaluate Reverse Polish Notation for your coding interview. Learn the stack-based evaluation pattern, Python division truncation, and what interviewers actually evaluate.

**Difficulty**: Medium
**Patterns**: `stack`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/evaluate-reverse-polish-notation-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=evaluate-reverse-polish-notation)**

---

## Problem

Evaluate an expression in Reverse Polish Notation (postfix notation). Valid operators are `+`, `-`, `*`, `/`. Integer division should truncate toward zero.

### Example

**Input:** `tokens = ["2","1","+","3","*"]`
**Output:** `9`, `((2 + 1) * 3) = 9`

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=evaluate-reverse-polish-notation)*

---

## Solution

```python
def evalRPN(tokens: list[str]) -> int:
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in tokens:
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  # truncate toward zero
        else:
            stack.append(int(token))

    return stack[0]
```

**Division note:** `int(a / b)` truncates toward zero. Python's `//` floors toward negative infinity, which differs for negative results: `int(7 / -2) = -3` (correct), but `7 // -2 = -4` (wrong).

---

## Complexity

| Aspect | Complexity |
|---|---|
| Time | O(n), single pass through tokens |
| Space | O(n), stack holds at most n elements |

---

## Common Interview Mistakes

1. **Wrong operand order.** Pop `b` first (right), then `a` (left). `a - b`, not `b - a`.

2. **Using `//` instead of `int(a / b)`.** Python's `//` floors; the problem wants truncation toward zero.

3. **Not converting tokens to integers.** Tokens are strings, push `int(token)`.

---

## Resources

- **Full Walkthrough**: [Evaluate Reverse Polish Notation: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/evaluate-reverse-polish-notation-interview-walkthrough/)
- **Practice**: [Mock interview for Evaluate Reverse Polish Notation](https://intervu.dev/setup2?problem=evaluate-reverse-polish-notation)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Basic Calculator](basic-calculator.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/basic-calculator-interview-walkthrough/)
- [Implement Queue using Stacks](implement-queue-using-stacks.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/implement-queue-using-stacks-interview-walkthrough/)
- [Min Stack](min-stack.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/min-stack-interview-walkthrough/)
- [Valid Parentheses](valid-parentheses.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/valid-parentheses-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
