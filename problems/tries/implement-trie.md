# Implement Trie (Prefix Tree)

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/implement-trie-interview-walkthrough/)*

> A step-by-step walkthrough of LeetCode #208 as it unfolds in a real coding interview. Learn how to design a Trie from scratch, explain node structure clearly, and avoid the is_end flag mistake that catches most candidates.

**Difficulty**: Medium
**Patterns**: `trie`, `data-structure-design`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/implement-trie-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=implement-trie)**

---

## Problem

Implement a data structure called a **Trie** (pronounced "try") that supports three operations:

- `insert(word)`: Insert a word into the trie.
- `search(word)`: Return `True` if the word exists in the trie, `False` otherwise.
- `startsWith(prefix)`: Return `True` if any previously inserted word starts with the given prefix.

([LeetCode #208](https://leetcode.com/problems/implement-trie-prefix-tree/))

### Example

**Input**
```
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
```

**Output**
```
[null, null, true, false, true, null, true]
```

After inserting `"apple"`, searching for `"apple"` returns `true` and searching for `"app"` returns `false`, because `"app"` was never fully inserted. However, `startsWith("app")` returns `true` because `"apple"` begins with `"app"`. After inserting `"app"` directly, searching for it also returns `true`. This illustrates the crucial distinction between a complete word and a prefix path in the trie.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev)*

---

## Solution

```python
class TrieNode:
    def __init__(self):
        # Maps each character to its child TrieNode
        self.children = {}
        # True if this node marks the end of a complete word
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            # Create a new node if this character path doesn't exist yet
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        # Mark the final node as a complete word
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False  # Path breaks: word doesn't exist
            node = node.children[char]
        # Must reach end AND the node must be a complete word
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False  # No word with this prefix exists
            node = node.children[char]
        # If we traversed the full prefix without breaking, it exists
        return True
```

Notice how `search` and `startsWith` share an almost identical traversal loop. The only difference is the final return value. This is a clean signal that the design is right.

---

## Complexity

| Operation | Time Complexity | Space Complexity |
|---|---|---|
| `insert(word)` | O(m), m = word length | O(m), new nodes per character |
| `search(word)` | O(m) | O(1), no new allocations |
| `startsWith(prefix)` | O(m) | O(1) |
| Total space | | O(n × m), n words, avg length m |

**Time:** Each operation traverses the word character by character, doing O(1) hash map lookups at each step. Total: O(m) per operation.

**Space:** The trie's real power shines when many words share prefixes. In the worst case (no shared prefixes), you use O(n × m) space, but in practice, tries compress shared prefixes significantly compared to storing full strings separately.

This is a common interview follow-up: *"Can you reduce space further?"* For lowercase letters only, you could use a fixed-size array of 26 instead of a hash map, O(1) space per node relative to character set size, though the total space remains O(n × m) in the worst case.

---

## Common Interview Mistakes

1. **Forgetting the `is_end` flag.** A lot of candidates build the traversal correctly but forget to mark, or check, the end-of-word flag. This causes `search("app")` to return `true` even if only `"apple"` was inserted.

2. **Mixing up `search` and `startsWith`.** Both methods look nearly identical. Candidates sometimes return `True` from `search` without checking `is_end`, effectively making it behave like `startsWith`. Slow down and be explicit.

3. **Creating a new root per method call.** This is a subtle bug: if you initialize `node = TrieNode()` instead of `node = self.root` at the top of your methods, you're starting from an empty node, not the actual trie.

4. **Not handling the empty string.** What should `insert("")` do? What about `search("")`? The loop handles these gracefully (zero iterations), but candidates who haven't thought about edge cases may be caught off-guard if the interviewer asks.

5. **Using a fixed array of 26 instead of a dict without justification.** Using `[None] * 26` is a valid optimization for lowercase letters, but jumping straight to it without explaining *why* (and without asking about character constraints first) suggests you memorized the solution rather than reasoned through it.

6. **Coding before explaining.** Tries are one of those problems where a 60-second verbal explanation of the node structure dramatically reduces bugs during implementation. Candidates who dive straight into code often lose track of when to create nodes vs. traverse them.

7. **Confusing `startsWith` with exact match.** Reading the problem too quickly and implementing `startsWith` as an exact search is a common mistake. The method name is a clue: it checks a path, not a complete word.

---

## Resources

- **Full Walkthrough**: [Implement Trie (Prefix Tree): Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/implement-trie-interview-walkthrough/)
- **Practice**: [Mock interview for Implement Trie (Prefix Tree)](https://intervu.dev/setup2?problem=implement-trie)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
