# Time Based Key-Value Store

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/time-based-key-value-store-interview-walkthrough/)*

> A step-by-step walkthrough of the Time Based Key-Value Store problem as it unfolds in a real coding interview. Learn the optimal approach using binary search on sorted timestamps, common mistakes, and how strong candidates communicate their solution.

**Difficulty**: Medium
**Patterns**: `binary-search`, `design`, `time-based-key-value-store`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/time-based-key-value-store-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=time-based-key-value-store)**

---

## Problem

Implement a `TimeMap` class with two operations:
- `set(key: str, value: str, timestamp: int)` stores the key-value pair at the given timestamp.
- `get(key: str, timestamp: int) -> str` returns the value with the largest timestamp ≤ the given timestamp, or `""` if none exists.

The problem guarantees that `set` is always called with strictly increasing `timestamp` values for a given key. ([LeetCode #981](https://leetcode.com/problems/time-based-key-value-store/))

### Example

```
timeMap.set("foo", "bar", 1)
timeMap.get("foo", 1)   # returns "bar"
timeMap.get("foo", 3)   # returns "bar" (largest ts ≤ 3 is 1)
timeMap.set("foo", "bar2", 4)
timeMap.get("foo", 4)   # returns "bar2"
timeMap.get("foo", 5)   # returns "bar2"
```

The key observation: `get("foo", 3)` doesn't find an exact match at timestamp 3, so it returns the value from the most recent timestamp before 3, which is timestamp 1. This "floor query" behavior is the core challenge.

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=time-based-key-value-store)*

---

## Solution

```python
from collections import defaultdict
from bisect import bisect_right

class TimeMap:
    def __init__(self):
        # Parallel lists: timestamps and values for each key
        self.timestamps = defaultdict(list)
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        ts_list = self.timestamps[key]
        if not ts_list:
            return ""

        # bisect_right gives insertion point after any exact match
        idx = bisect_right(ts_list, timestamp) - 1

        if idx < 0:
            return ""  # All stored timestamps exceed query
        return self.values[key][idx]
```

Why this version is interview-friendly:

- **Parallel lists avoid per-query allocation.** The draft version built `timestamps = [t for t, _ in pairs]` inside every `get` call, which is O(n) memory allocation per query. Maintaining `self.timestamps` and `self.values` separately keeps `get` at pure O(log n).
- **`defaultdict(list)` avoids key-existence checks.** Accessing a missing key returns an empty list, so `if not ts_list` handles the "key not found" case cleanly.
- **`bisect_right - 1` is the standard floor pattern.** Naming this explicitly in an interview shows familiarity with the binary search library.

---

## Complexity

| Operation | Time | Space |
|---|---|---|
| `set` | O(1) amortized | O(1) per call |
| `get` | O(log n) | O(1) |
| Overall space | | O(total set calls) |

`n` = number of `set` calls for a given key. `set` does a list append (O(1) amortized). `get` runs binary search on the timestamps list (O(log n)) with no additional allocation.

A common follow-up: "What if we needed to support `delete`?" Removing from the middle of a list is O(n). You'd need a different structure, like a sorted container or a balanced BST, to keep all operations logarithmic. Mentioning this tradeoff shows design maturity.

---

## Common Interview Mistakes

1. **Linear scan instead of binary search.** Iterating through all timestamps for a key makes `get` O(n). The sorted-input constraint is a direct signal to use binary search. Missing this tells the interviewer you didn't read the constraints carefully.

2. **Rebuilding the timestamps list on every `get` call.** Writing `timestamps = [t for t, _ in pairs]` inside `get` allocates O(n) memory per query. The binary search itself is O(log n), but the list comprehension dominates. Maintain timestamps in a separate persistent list.

3. **Off-by-one: using `bisect_left` instead of `bisect_right`.** Both can work, but the adjustment differs. With `bisect_right`, subtract 1 to get the floor. With `bisect_left`, you'd need to check whether the element at the returned index matches the query before deciding to subtract. `bisect_right - 1` is cleaner and less error-prone.

4. **Not handling `idx < 0`.** When the query timestamp is smaller than all stored timestamps, `bisect_right` returns 0, and `0 - 1 = -1`. In Python, `list[-1]` returns the last element instead of raising an error, silently returning the wrong value. Always check `idx < 0` explicitly.

5. **Using a single tuple list instead of parallel lists.** Storing `(timestamp, value)` tuples is conceptually clean, but `bisect_right` operates on a simple list of comparable values. You'd need to extract timestamps into a separate list for each query (O(n)) or use a custom key function. Parallel lists solve this elegantly.

---

## Resources

- **Full Walkthrough**: [Time Based Key-Value Store: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/time-based-key-value-store-interview-walkthrough/)
- **Practice**: [Mock interview for Time Based Key-Value Store](https://intervu.dev/setup2?problem=time-based-key-value-store)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Binary Search](binary-search.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/binary-search-interview-walkthrough/)
- [First Bad Version](first-bad-version.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/first-bad-version-interview-walkthrough/)
- [Search in Rotated Sorted Array](search-in-rotated-sorted-array.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/search-in-rotated-sorted-array-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
