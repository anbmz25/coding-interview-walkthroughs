# Valid Parentheses

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/valid-parentheses-interview-walkthrough/)*

> A step-by-step guide to solving Valid Parentheses in a coding interview: stack-based reasoning, bracket matching with hash maps, edge cases, and what strong candidates sound like.

**Difficulty**: Easy
**Patterns**: `stacks`, `strings`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/valid-parentheses-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=valid-parentheses)**

---

## Problem

Given a string `s` containing only the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine if the input string is **valid**. ([LeetCode #20](https://leetcode.com/problems/valid-parentheses/))

A string is valid if:
- Every open bracket is closed by the same type of closing bracket.
- Open brackets are closed in the correct order.
- Every closing bracket has a corresponding open bracket.

### Example

**Input**
`s = "()[{}]"`

**Output**
`true`

Each opening bracket is matched by its correct closing bracket, and they are properly nested. A second example: `s = "(]"` returns `false` because the `(` is closed by `]`, which is the wrong type. And `s = "([)]"` returns `false` because the brackets are interleaved, `(` is not closed before `[` closes. Order matters as much as type.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=valid-parentheses)*

---

## Solution

```python
def isValid(s: str) -> bool:
    stack = []

    # Maps each closing bracket to its expected opening bracket
    matches = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in matches:
            # It's a closing bracket: check against the top of the stack
            if not stack or stack[-1] != matches[char]:
                return False  # Stack empty (no opener) or wrong type
            stack.pop()
        else:
            # It's an opening bracket: push onto the stack
            stack.append(char)

    # Valid only if all openers have been matched and popped
    return len(stack) == 0
```

Implementation notes worth calling out in an interview:

- **`if char in matches`** cleanly distinguishes closing brackets from opening ones, since `matches` only contains closing brackets as keys. This avoids a separate `if char in "([{"` check.
- **`if not stack or stack[-1] != matches[char]`** handles both failure cases (empty stack and wrong type) in a single condition. Checking `not stack` first prevents an `IndexError` via short-circuit evaluation.
- **`return len(stack) == 0`** is the critical final check. Returning `True` unconditionally after the loop is one of the most common bugs in this problem.
- The `matches` dictionary makes the bracket pairing data-driven. Adding a new bracket type (e.g., `<>`) requires adding a single entry, no logic changes.

---

## Complexity

| Operation | Complexity |
|---|---|
| Time | O(n) |
| Space | O(n) |

**Time:** We iterate through the string exactly once. Each character triggers exactly one stack operation (push or pop), both O(1). Total: O(n).

**Space:** In the worst case (a string of all opening brackets like `"((((("`) every character is pushed without being popped. Stack grows to O(n).

A common follow-up: *"Can you reduce space below O(n)?"* For the general case with three bracket types, no. You need to remember all unmatched openers. If the input only uses one type (e.g., `()`), you could use a counter instead of a stack, reducing space to O(1).

---

## Common Interview Mistakes

1. **Forgetting the final empty-stack check.** The single most common bug. After the loop, leftover opening brackets mean the string is invalid. Returning `True` unconditionally produces wrong answers for inputs like `"(("` or `"({["`.

2. **Not checking for an empty stack before popping.** When a closing bracket arrives, verify the stack is non-empty before accessing `stack[-1]`. An empty stack means there's no opener to match. Forgetting this causes an `IndexError` on inputs like `")"`.

3. **Using a chain of `if/elif` instead of a hash map.** Verbose, harder to read, and easy to miscopy one condition. A `matches` dictionary expresses the same logic in a single lookup.

4. **Only checking character count.** Counting opening and closing brackets catches some invalid strings but misses mismatched types (`"(]"`) and wrong order (`"([)]"`). Counting is necessary but not sufficient.

5. **Not naming the three failure modes before coding.** Candidates who articulate all three failure modes (wrong type, underflow, unclosed openers) before writing code demonstrate genuine understanding rather than pattern recall.

6. **Treating this as too simple to explain carefully.** Because it's rated Easy, some candidates rush without communicating reasoning. A fluent, well-explained Easy solution is far more impressive than a silent correct one.

---

## Resources

- **Full Walkthrough**: [Valid Parentheses: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/valid-parentheses-interview-walkthrough/)
- **Practice**: [Mock interview for Valid Parentheses](https://intervu.dev/setup2?problem=valid-parentheses)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Basic Calculator](basic-calculator.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/basic-calculator-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
