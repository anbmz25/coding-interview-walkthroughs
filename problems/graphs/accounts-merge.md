# Accounts Merge

*Originally published at [intervu.dev](https://intervu.dev/blog/walkthroughs/accounts-merge-interview-walkthrough/)*

> A step-by-step walkthrough of the Accounts Merge problem as it unfolds in a real coding interview. Learn the Union-Find approach, why name-based merging fails, and how to reconstruct sorted email groups.

**Difficulty**: Medium
**Patterns**: `union-find`, `graph`

**[Read the full interview walkthrough →](https://intervu.dev/blog/walkthroughs/accounts-merge-interview-walkthrough/)**
**[Practice in a mock interview →](https://intervu.dev/setup2?problem=accounts-merge)**

---

## Problem

Given a list of `accounts` where `accounts[i][0]` is the account name and `accounts[i][1:]` are email addresses, merge accounts that share at least one email. After merging, return the accounts with emails sorted alphabetically within each account. Two accounts belong to the same person if they share any email. ([LeetCode #721](https://leetcode.com/problems/accounts-merge/))

### Example

**Input**
```
accounts = [
  ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
  ["John", "johnsmith@mail.com", "john00@mail.com"],
  ["Mary", "mary@mail.com"],
  ["John", "johnnybravo@mail.com"]
]
```

**Output**
```
[
  ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
  ["Mary", "mary@mail.com"],
  ["John", "johnnybravo@mail.com"]
]
```

*Already comfortable with the solution? [Practice it in a mock interview →](https://intervu.dev/setup2?problem=accounts-merge)*

---

## Solution

**Union-Find:**
```python
from collections import defaultdict

def accountsMerge(accounts: list[list[str]]) -> list[list[str]]:
    parent = {}
    email_to_name = {}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # path compression
        return parent[x]

    def union(x, y):
        root_x, root_y = find(x), find(y)
        if root_x != root_y:
            parent[root_x] = root_y

    # Build union-find
    for account in accounts:
        name = account[0]
        first_email = account[1]
        for email in account[1:]:
            if email not in parent:
                parent[email] = email
            email_to_name[email] = name
            union(first_email, email)

    # Group emails by root
    components = defaultdict(list)
    for email in parent:
        root = find(email)
        components[root].append(email)

    # Build result
    result = []
    for root, emails in components.items():
        result.append([email_to_name[root]] + sorted(emails))

    return result
```

**DFS approach:**
```python
from collections import defaultdict

def accountsMerge_dfs(accounts: list[list[str]]) -> list[list[str]]:
    email_to_accounts = defaultdict(list)  # email -> list of account indices

    for i, account in enumerate(accounts):
        for email in account[1:]:
            email_to_accounts[email].append(i)

    visited_accounts = set()
    result = []

    def dfs(account_idx: int, emails: list[str]) -> None:
        if account_idx in visited_accounts:
            return
        visited_accounts.add(account_idx)
        for email in accounts[account_idx][1:]:
            emails.append(email)
            for neighbor_account in email_to_accounts[email]:
                dfs(neighbor_account, emails)

    for i, account in enumerate(accounts):
        if i not in visited_accounts:
            emails = []
            dfs(i, emails)
            result.append([account[0]] + sorted(set(emails)))

    return result
```

---

## Complexity


---

## Common Interview Mistakes

- **Merging by name instead of by email.** Same name does not mean same person. Only shared emails trigger a merge.

- **Not using path compression in Union-Find.** Without it, find operations degrade to O(n). Path compression makes it nearly O(1) amortized.

- **Forgetting to initialize `parent[email] = email`** for every new email before unioning. Without this, `find` will throw a key error.

- **Duplicating emails.** In DFS, an email may be added multiple times (from different account paths visiting the same email). Use `set(emails)` when building the result.

- **Using account names as keys for components.** Different accounts with the same name are different people. Use the root email or account index as the component key.

---

## Resources

- **Full Walkthrough**: [Accounts Merge: Coding Interview Walkthrough](https://intervu.dev/blog/walkthroughs/accounts-merge-interview-walkthrough/)
- **Practice**: [Mock interview for Accounts Merge](https://intervu.dev/setup2?problem=accounts-merge)
- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)
- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)
- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)

---

## Related Problems

- [01 Matrix](01-matrix.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/01-matrix-interview-walkthrough/)
- [Clone Graph](clone-graph.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/clone-graph-interview-walkthrough/)
- [Course Schedule](course-schedule.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/course-schedule-interview-walkthrough/)
- [Flood Fill](flood-fill.md) (Easy) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/flood-fill-interview-walkthrough/)
- [Number of Islands](number-of-islands.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/number-of-islands-interview-walkthrough/)
- [Rotting Oranges](rotting-oranges.md) (Medium) · [Full walkthrough →](https://intervu.dev/blog/walkthroughs/rotting-oranges-interview-walkthrough/)

---

*Part of the [Coding Interview Walkthroughs](https://github.com/anbmz25/coding-interview-walkthroughs) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*
