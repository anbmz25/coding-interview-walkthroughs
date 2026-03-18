# Basic Calculator

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/basic-calculator-interview-walkthrough/)*

> A step-by-step walkthrough of the Basic Calculator problem as it unfolds in a real coding interview. Learn the stack-save pattern for nested parentheses, sign context management, and how strong candidates trace through expressions.

**Difficulty**: Hard
**Patterns**: `stack`, `string`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/basic-calculator-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=basic-calculator)**

---

## Problem

Given a string `s` representing a valid mathematical expression with integers, `+`, `-`, `(`, `)`, and spaces, evaluate and return the result. The expression is guaranteed to be valid. ([LeetCode #224](https://leetcode.com/problems/basic-calculator/))

### Example 1

**Input**
`s = "1 + 1"`

**Output**
`2`

### Example 2

**Input**
`s = " 2-1 + 2 "`

**Output**
`3`

### Example 3

**Input**
`s = "(1+(4+5+2)-3)+(6+8)"`

**Output**
`23`

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=basic-calculator)*

---

## Solution

```python
def calculate(s: str) -> int:
    stack = []
    result = 0
    num = 0
    sign = 1  # +1 or -1

    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch in ('+', '-'):
            result += sign * num
            num = 0
            sign = 1 if ch == '+' else -1
        elif ch == '(':
            # Save current state and reset
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif ch == ')':
            result += sign * num
            num = 0
            result *= stack.pop()   # saved sign before this '('
            result += stack.pop()   # saved result before this '('
        # spaces are skipped implicitly

    result += sign * num
    return result
```

---

## Complexity


---

## Common Interview Mistakes

- **Forgetting to flush `num` at each operator.** When you see `+` or `-`, apply `sign * num` to `result` before resetting `num`. Don't wait until the end.

- **Not flushing `num` at `)`.** Similar to the operator case. Before combining with the stack values, apply the last pending `num`.

- **Building numbers wrong.** Multi-digit numbers require `num = num * 10 + int(ch)`, not just `num = int(ch)`.

- **Using eval().** Never in an interview. Implement the parser manually.

- **Sign across parentheses.** After a `-` followed by `(`, the sign inside the parentheses is negated. Pushing `sign` before the `(` and multiplying by it after the `)` handles this correctly.

---

## Resources

- **Full Walkthrough**: [Basic Calculator: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/basic-calculator-interview-walkthrough/)
- **Practice**: [Mock interview for Basic Calculator](https://intervu.dev/setup2?problem=basic-calculator)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Implement Queue using Stacks](implement-queue-using-stacks.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/implement-queue-using-stacks-interview-walkthrough/)
- [Min Stack](min-stack.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/min-stack-interview-walkthrough/)
- [Valid Parentheses](valid-parentheses.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/valid-parentheses-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
