# Contains Duplicate

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/contains-duplicate-interview-walkthrough/)*

> How to solve Contains Duplicate (LeetCode #217) in a coding interview. Covers hash set vs. sorting trade-offs, early exit optimization, the follow-up question, and what interviewers are really testing.

**Difficulty**: Easy
**Patterns**: `arrays`, `hash-set`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/contains-duplicate-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=contains-duplicate)**

---

## Problem

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and `false` if every element is distinct.

([LeetCode #217](https://leetcode.com/problems/contains-duplicate/))

### Example 1

**Input**
`nums = [1, 2, 3, 1]`

**Output**
`true`

### Example 2

**Input**
`nums = [1, 2, 3, 4]`

**Output**
`false`

### Example 3

**Input**
`nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]`

**Output**
`true`

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=contains-duplicate)*

---

## Solution

```python
def containsDuplicate(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

**One-liner alternative:**
```python
def containsDuplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))
```

The one-liner is clean but always processes the full array. The loop version returns early on first duplicate found, better in practice when duplicates appear early.

**Sorting approach (O(1) extra space):**
```python
def containsDuplicate(nums: list[int]) -> bool:
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False
```

Note: this modifies the input array, worth flagging in an interview.

---

## Complexity

| Approach | Time | Space |
|---|---|---|
| Brute force | O(n²) | O(1) |
| Hash set | O(n) | O(n) |
| Sort | O(n log n) | O(1) extra |

---

## Common Interview Mistakes

1. **Using the brute force without recognizing it's O(n²).** Always state complexity before the interviewer asks.

2. **Using the one-liner without mentioning early exit.** `set(nums)` builds the full set regardless. If a duplicate appears at index 1 of a million-element array, the loop is vastly faster.

3. **Sorting without noting it modifies the input.** In-place sort changes the caller's data, worth mentioning even if it's acceptable here.

4. **Not discussing the time/space trade-off.** The interviewer almost always wants to hear you compare approaches. "I'll use a hash set for O(n) time at the cost of O(n) space. If space is constrained, sorting gives O(n log n) with O(1) extra" is a model answer.

5. **Not asking about the follow-up.** Contains Duplicate II (within k distance) is a natural follow-up. Showing awareness of it signals interviewer-level problem thinking.

---

## Resources

- **Full Walkthrough**: [Contains Duplicate: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/contains-duplicate-interview-walkthrough/)
- **Practice**: [Mock interview for Contains Duplicate](https://intervu.dev/setup2?problem=contains-duplicate)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Best Time to Buy and Sell Stock](best-time-to-buy-and-sell-stock.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/best-time-to-buy-and-sell-stock-interview-walkthrough/)
- [Container With Most Water](container-with-most-water.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/container-with-most-water-interview-walkthrough/)
- [Majority Element](majority-element.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/majority-element-interview-walkthrough/)
- [Maximum Subarray](maximum-subarray.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/maximum-subarray-interview-walkthrough/)
- [Merge Intervals](merge-intervals.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/merge-intervals-interview-walkthrough/)
- [Product of Array Except Self](product-of-array-except-self.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/product-of-array-except-self-interview-walkthrough/)
- [3Sum](three-sum.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/three-sum-interview-walkthrough/)
- [Trapping Rain Water](trapping-rain-water.md) (Hard) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/trapping-rain-water-interview-walkthrough/)
- [Two Sum](two-sum.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/two-sum-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
