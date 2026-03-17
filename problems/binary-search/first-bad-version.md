# First Bad Version

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/first-bad-version-interview-walkthrough/)*

> Master First Bad Version for your coding interview. Learn the monotonic binary search pattern, overflow-safe midpoint, common off-by-one mistakes, and what interviewers evaluate.

**Difficulty**: Easy
**Patterns**: `binary-search`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/first-bad-version-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=first-bad-version)**

---

## Problem

You have `n` versions `[1, 2, ..., n]`. After some version, all subsequent versions are bad. Given an API `isBadVersion(version)` which returns `True` if the version is bad, find the first bad version. Minimize the number of API calls.

### Example

**Input:** n = 5, bad = 4
**API calls:** isBadVersion(3) → false, isBadVersion(4) → true
**Output:** 4

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=first-bad-version)*

---

## Solution

```python
def firstBadVersion(n: int) -> int:
    lo, hi = 1, n

    while lo < hi:
        mid = lo + (hi - lo) // 2  # Overflow-safe midpoint
        if isBadVersion(mid):
            hi = mid      # mid could be the answer; keep it in range
        else:
            lo = mid + 1  # mid is good; answer is strictly after

    return lo  # lo == hi: the only candidate remaining
```

---

## Complexity

| Aspect | Complexity |
|---|---|
| Time | O(log n) |
| Space | O(1) |
| API calls | O(log n) |

---

## Common Interview Mistakes

1. **Integer overflow with `(lo + hi) // 2`.** In Python this isn't a practical issue (arbitrary precision integers), but interviewers still expect you to use `lo + (hi - lo) // 2`, it shows awareness and is critical in other languages.

2. **Using `hi = mid - 1` when `isBadVersion(mid)` is True.** This excludes `mid` from consideration, but `mid` could be the first bad version. Must use `hi = mid`.

3. **Off-by-one in the exit condition.** Using `lo <= hi` requires an explicit `return` inside the loop. The `lo < hi` variant terminates cleanly with `lo == hi` pointing to the answer.

4. **Not explaining why minimizing API calls matters.** The interviewer wants to hear "binary search finds the answer in O(log n) calls vs. O(n) for linear scan."

---

## Resources

- **Full Walkthrough**: [First Bad Version: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/first-bad-version-interview-walkthrough/)
- **Practice**: [Mock interview for First Bad Version](https://intervu.dev/setup2?problem=first-bad-version)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Binary Search](binary-search.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/binary-search-interview-walkthrough/)
- [Search in Rotated Sorted Array](search-in-rotated-sorted-array.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/search-in-rotated-sorted-array-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
