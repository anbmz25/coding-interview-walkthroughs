# Majority Element

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/majority-element-interview-walkthrough/)*

> How to solve Majority Element (LeetCode #169) in a coding interview. Covers hash map, sorting, and Boyer-Moore Voting Algorithm approaches with the cancellation intuition explained clearly.

**Difficulty**: Easy
**Patterns**: `arrays`, `boyer-moore`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/majority-element-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=majority-element)**

---

## Problem

Given an array `nums` of size `n`, return the majority element. The majority element is the element that appears more than `n / 2` times. You may assume the majority element always exists in the array.

([LeetCode #169](https://leetcode.com/problems/majority-element/))

### Example 1

**Input**
`nums = [3, 2, 3]`

**Output**
`3`

### Example 2

**Input**
`nums = [2, 2, 1, 1, 1, 2, 2]`

**Output**
`2`

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=majority-element)*

---

## Solution

**Hash map approach:**
```python
from collections import Counter

def majorityElement_hashmap(nums: list[int]) -> int:
    counts = Counter(nums)
    return max(counts, key=counts.get)
```

**Sorting approach:**
```python
def majorityElement_sort(nums: list[int]) -> int:
    nums.sort()
    return nums[len(nums) // 2]
```

**Boyer-Moore Voting (optimal):**
```python
def majorityElement(nums: list[int]) -> int:
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate
```

The sorting approach works because: if an element appears more than n/2 times, it must occupy position `n//2` in a sorted array. Clean and surprising.

---

## Complexity

| Approach | Time | Space |
|---|---|---|
| Hash map | O(n) | O(n) |
| Sort | O(n log n) | O(1) extra |
| Boyer-Moore | O(n) | O(1) |

Boyer-Moore is the asymptotically optimal solution on both dimensions.

---

## Common Interview Mistakes

1. **Not knowing Boyer-Moore.** The hash map solution is acceptable, but interviewers at top companies expect you to at least know the O(1) space approach exists, even if you can't derive it on the spot.

2. **Explaining Boyer-Moore without the cancellation intuition.** "I track a candidate and decrement count for mismatches" without explaining *why* it works sounds like memorization. The key insight: the majority element has more votes than all others combined.

3. **Not exploiting the guarantee.** If you're verifying your candidate at the end, you've forgotten that the problem guarantees a majority element exists. Verification is unnecessary here.

4. **Forgetting the sort trick.** `nums[n//2]` after sorting is surprisingly clean and worth knowing as an alternative.

5. **Over-engineering with divide and conquer.** There's a D&C solution, but it's O(n log n) or O(n) with O(log n) space. Not better than Boyer-Moore.

---

## Resources

- **Full Walkthrough**: [Majority Element: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/majority-element-interview-walkthrough/)
- **Practice**: [Mock interview for Majority Element](https://intervu.dev/setup2?problem=majority-element)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [Binary Tree Right Side View](binary-tree-right-side-view.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/binary-tree-right-side-view-interview-walkthrough/)
- [Contains Duplicate](contains-duplicate.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/contains-duplicate-interview-walkthrough/)
- [Partition Equal Subset Sum](partition-equal-subset-sum.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/partition-equal-subset-sum-interview-walkthrough/)
- [Valid Anagram](valid-anagram.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/valid-anagram-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
