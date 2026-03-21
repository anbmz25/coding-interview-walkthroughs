#!/usr/bin/env python3
"""
Reads each walkthrough from the Intervu blog source and generates a condensed
GitHub-friendly Markdown version in ../problems/<topic>/.

Usage:
    python3 scripts/sync_walkthroughs.py
"""

import os
import re
import glob
import shutil
import yaml
from typing import Optional

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
BLOG_DIR = os.environ.get(
    "BLOG_DIR",
    os.path.join(REPO_ROOT, "..", "intervu-blog", "src", "content", "blog", "walkthroughs"),
)
OUT_DIR = os.path.join(REPO_ROOT, "problems")

GITHUB_REPO = "https://github.com/anbmz25/coding-interview-walkthroughs"

# ---------------------------------------------------------------------------
# Topic mapping: slug → subdirectory
# ---------------------------------------------------------------------------
TOPIC_MAP = {
    "two-sum": "arrays",
    "best-time-to-buy-and-sell-stock": "arrays",
    "maximum-subarray": "arrays",
    "merge-intervals": "arrays",
    "three-sum": "arrays",
    "trapping-rain-water": "arrays",
    "merge-two-sorted-lists": "linked-lists",
    "reverse-linked-list": "linked-lists",
    "linked-list-cycle": "linked-lists",
    "lru-cache": "linked-lists",
    "invert-binary-tree": "trees",
    "binary-tree-level-order-traversal": "trees",
    "number-of-islands": "graphs",
    "course-schedule": "graphs",
    "climbing-stairs": "dynamic-programming",
    "coin-change": "dynamic-programming",
    "longest-substring-without-repeating-characters": "strings",
    "valid-parentheses": "stacks",
    "binary-search": "binary-search",
    "implement-trie": "tries",
    "product-of-array-except-self": "arrays",
    "validate-binary-search-tree": "trees",
    "search-in-rotated-sorted-array": "binary-search",
    "combination-sum": "backtracking",
    "permutations": "backtracking",
    "lowest-common-ancestor": "trees",
    "word-break": "dynamic-programming",
    "longest-palindromic-substring": "strings",
    "container-with-most-water": "arrays",
    "merge-k-sorted-lists": "linked-lists",
    "minimum-window-substring": "strings",
    "01-matrix": "graphs",
    "accounts-merge": "graphs",
    "add-binary": "strings",
    "balanced-binary-tree": "trees",
    "basic-calculator": "stacks",
    "binary-tree-right-side-view": "trees",
    "contains-duplicate": "arrays",
    "majority-element": "arrays",
    "partition-equal-subset-sum": "dynamic-programming",
    "valid-anagram": "strings",
    "valid-palindrome": "strings",
    "maximum-depth-of-binary-tree": "trees",
    "diameter-of-binary-tree": "trees",
    "lowest-common-ancestor-of-a-binary-search-tree": "trees",
    "first-bad-version": "binary-search",
    "min-stack": "stacks",
    "meeting-rooms": "arrays",
    "middle-of-the-linked-list": "linked-lists",
    "flood-fill": "graphs",
    "implement-queue-using-stacks": "stacks",
    "ransom-note": "arrays",
    "clone-graph": "graphs",
    "rotting-oranges": "graphs",
    "evaluate-reverse-polish-notation": "stacks",
    "kth-smallest-element-in-a-bst": "trees",
    "longest-palindrome": "arrays",
    "insert-interval": "arrays",
    "subsets": "backtracking",
    "sort-colors": "arrays",
    "word-search": "backtracking",
    "spiral-matrix": "arrays",
    "unique-paths": "dynamic-programming",
    "k-closest-points-to-origin": "arrays",
    "find-all-anagrams-in-a-string": "arrays",
    "letter-combinations-of-a-phone-number": "backtracking",
    "time-based-key-value-store": "binary-search",
    "string-to-integer-atoi": "strings",
    "task-scheduler": "arrays",
    "minimum-height-trees": "graphs",
    "construct-binary-tree-from-preorder-and-inorder-traversal": "trees",
    "serialize-and-deserialize-binary-tree": "trees",
    "find-median-from-data-stream": "arrays",
    "word-ladder": "graphs",
    "largest-rectangle-in-histogram": "stacks",
    "maximum-profit-in-job-scheduling": "dynamic-programming",
}

TOPIC_DESCRIPTIONS = {
    "arrays": "Array manipulation, hashing, sorting, and two-pointer techniques.",
    "linked-lists": "Pointer manipulation, cycle detection, and node-level operations.",
    "trees": "Tree traversals, recursion, and structural transformations.",
    "graphs": "Graph traversal (BFS/DFS), cycle detection, and topological sorting.",
    "dynamic-programming": "Overlapping subproblems, memoization, and bottom-up tabulation.",
    "strings": "Sliding window, character frequency tracking, and substring problems.",
    "stacks": "LIFO-based pattern matching, bracket validation, and expression parsing.",
    "binary-search": "Divide-and-conquer search on sorted data.",
    "tries": "Prefix trees for fast string lookup, autocomplete, and dictionary operations.",
    "backtracking": "Recursive search with pruning, decision trees, and constraint satisfaction.",
}

# ---------------------------------------------------------------------------
# Difficulty mapping: slug → LeetCode difficulty
# ---------------------------------------------------------------------------
DIFFICULTY_MAP = {
    "two-sum": "Easy",
    "best-time-to-buy-and-sell-stock": "Easy",
    "valid-parentheses": "Easy",
    "merge-two-sorted-lists": "Easy",
    "reverse-linked-list": "Easy",
    "linked-list-cycle": "Easy",
    "climbing-stairs": "Easy",
    "binary-search": "Easy",
    "invert-binary-tree": "Easy",
    "maximum-subarray": "Medium",
    "binary-tree-level-order-traversal": "Medium",
    "longest-substring-without-repeating-characters": "Medium",
    "merge-intervals": "Medium",
    "number-of-islands": "Medium",
    "coin-change": "Medium",
    "three-sum": "Medium",
    "course-schedule": "Medium",
    "lru-cache": "Medium",
    "implement-trie": "Medium",
    "product-of-array-except-self": "Medium",
    "validate-binary-search-tree": "Medium",
    "search-in-rotated-sorted-array": "Medium",
    "combination-sum": "Medium",
    "permutations": "Medium",
    "lowest-common-ancestor": "Medium",
    "word-break": "Medium",
    "longest-palindromic-substring": "Medium",
    "container-with-most-water": "Medium",
    "trapping-rain-water": "Hard",
    "merge-k-sorted-lists": "Hard",
    "minimum-window-substring": "Hard",
    "01-matrix": "Medium",
    "accounts-merge": "Medium",
    "add-binary": "Easy",
    "balanced-binary-tree": "Easy",
    "basic-calculator": "Hard",
    "binary-tree-right-side-view": "Medium",
    "contains-duplicate": "Easy",
    "majority-element": "Easy",
    "partition-equal-subset-sum": "Medium",
    "valid-anagram": "Easy",
    "valid-palindrome": "Easy",
    "maximum-depth-of-binary-tree": "Easy",
    "diameter-of-binary-tree": "Easy",
    "lowest-common-ancestor-of-a-binary-search-tree": "Easy",
    "first-bad-version": "Easy",
    "min-stack": "Easy",
    "meeting-rooms": "Easy",
    "middle-of-the-linked-list": "Easy",
    "flood-fill": "Easy",
    "implement-queue-using-stacks": "Easy",
    "ransom-note": "Easy",
    "clone-graph": "Medium",
    "rotting-oranges": "Medium",
    "evaluate-reverse-polish-notation": "Medium",
    "kth-smallest-element-in-a-bst": "Medium",
    "longest-palindrome": "Easy",
    "insert-interval": "Medium",
    "subsets": "Medium",
    "sort-colors": "Medium",
    "word-search": "Medium",
    "spiral-matrix": "Medium",
    "unique-paths": "Medium",
    "k-closest-points-to-origin": "Medium",
    "find-all-anagrams-in-a-string": "Medium",
    "letter-combinations-of-a-phone-number": "Medium",
    "time-based-key-value-store": "Medium",
    "string-to-integer-atoi": "Medium",
    "task-scheduler": "Medium",
    "minimum-height-trees": "Medium",
    "construct-binary-tree-from-preorder-and-inorder-traversal": "Medium",
    "serialize-and-deserialize-binary-tree": "Hard",
    "find-median-from-data-stream": "Hard",
    "word-ladder": "Hard",
    "largest-rectangle-in-histogram": "Hard",
    "maximum-profit-in-job-scheduling": "Hard",
}


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Split YAML frontmatter from Markdown body."""
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            fm = yaml.safe_load(parts[1])
            body = parts[2].strip()
            return fm, body
    return {}, content


def extract_section(body: str, heading: str) -> str:
    """Extract content under a ## heading, up to the next ## heading."""
    pattern = rf"^## {re.escape(heading)}\s*\n(.*?)(?=^## |\Z)"
    m = re.search(pattern, body, re.MULTILINE | re.DOTALL)
    return m.group(1).strip() if m else ""


def extract_difficulty(slug: str, tags: list[str]) -> str:
    """Look up difficulty from the canonical map, fall back to tags."""
    if slug in DIFFICULTY_MAP:
        return DIFFICULTY_MAP[slug]
    tag_set = set(t.lower() for t in tags)
    if "hard" in tag_set:
        return "Hard"
    if "easy" in tag_set:
        return "Easy"
    return "Medium"


def extract_patterns(tags: list[str]) -> list[str]:
    """Extract algorithm/pattern tags, excluding meta tags."""
    skip = {"interview-walkthrough", "coding-interview", "easy", "medium", "hard"}
    return [t for t in tags if t.lower() not in skip]


def cleanup_ai_patterns(text: str) -> str:
    """Remove common AI writing patterns per the cleanup-ai-writing skill."""
    # Rule 1: Replace em dashes with appropriate punctuation
    text = re.sub(r'(#[^\n]*?) — ', r'\1: ', text)
    text = re.sub(r'(\]\([^)]+\)) — ', r'\1, ', text)
    text = re.sub(r' — (O\(|which |so |this |that |the )', r': \1', text)
    text = re.sub(r' — ', ', ', text)

    # Rule 2: Remove filler phrases
    filler_patterns = [
        r"Here's why this matters[.:] *",
        r"Here's the insight that unlocks the optimal solution[.:] *",
        r"It's important to note that ",
        r"Let's dive in[.!] *",
        r"This is where things get interesting[.:] *",
    ]
    for pattern in filler_patterns:
        text = re.sub(pattern, '', text, flags=re.IGNORECASE)

    return text


def generate_condensed(fm: dict, body: str, slug: str, related: Optional[list] = None) -> str:
    """Build the condensed GitHub Markdown for one problem."""
    title = fm.get("title", slug)
    description = fm.get("description", "")
    tags = fm.get("tags", [])
    problem_name = title.replace(" — Coding Interview Walkthrough", "")

    blog_url = f"https://intervu.dev/blog/walkthroughs/{slug}-interview-walkthrough/"
    practice_url = f"https://intervu.dev/setup2?problem={slug}"

    difficulty = extract_difficulty(slug, tags)
    patterns = extract_patterns(tags)
    pattern_str = ", ".join(f"`{p}`" for p in patterns) if patterns else ""

    # Extract key sections
    problem_section = extract_section(body, "The Problem")
    impl_section = extract_section(body, "Python Implementation")
    complexity_section = extract_section(body, "Time & Space Complexity")
    if not complexity_section:
        complexity_section = extract_section(body, "Time Complexity")
    mistakes_section = extract_section(body, "Common Interview Mistakes")

    lines = [
        f"# {problem_name}",
        "",
        f"*Originally published at [intervu.dev]({blog_url})*",
        "",
        f"> {description}",
        "",
        f"**Difficulty**: {difficulty}",
    ]
    if pattern_str:
        lines.append(f"**Patterns**: {pattern_str}")
    lines += [
        "",
        f"**[Read the full interview walkthrough →]({blog_url})**",
        f"**[Practice in a mock interview →]({practice_url})**",
        "",
        "---",
        "",
        "## Problem",
        "",
    ]
    if problem_section:
        lines.append(problem_section.rstrip().rstrip("-").rstrip())
    lines += [
        "",
        "---",
        "",
        "## Solution",
        "",
    ]
    if impl_section:
        lines.append(impl_section.rstrip().rstrip("-").rstrip())
    lines += [
        "",
        "---",
        "",
        "## Complexity",
        "",
    ]
    if complexity_section:
        lines.append(complexity_section.rstrip().rstrip("-").rstrip())
    lines += [
        "",
        "---",
        "",
        "## Common Interview Mistakes",
        "",
    ]
    if mistakes_section:
        lines.append(mistakes_section.rstrip().rstrip("-").rstrip())
    lines += [
        "",
        "---",
        "",
        "## Resources",
        "",
        f"- **Full Walkthrough**: [{problem_name}: Coding Interview Walkthrough]({blog_url})",
        f"- **Practice**: [Mock interview for {problem_name}]({practice_url})",
        f"- [How to Prepare for a Coding Interview](https://intervu.dev/blog/how-to-prepare-for-coding-interview/)",
        f"- [The Grind 75 Study Pathway](https://intervu.dev/blog/grind-75-practice-pathway/)",
        f"- [Why LeetCode Alone Isn't Enough](https://intervu.dev/blog/why-leetcode-is-not-enough/)",
    ]
    # Related problems (same topic, excluding self)
    if related:
        lines += [
            "",
            "---",
            "",
            "## Related Problems",
            "",
        ]
        for r in related:
            r_blog = f"https://intervu.dev/blog/walkthroughs/{r['slug']}-interview-walkthrough/"
            lines.append(
                f"- [{r['name']}]({r['slug']}.md) ({r['difficulty']}) · [Full walkthrough →]({r_blog})"
            )
    lines += [
        "",
        "---",
        "",
        f"*Part of the [Coding Interview Walkthroughs]({GITHUB_REPO}) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*",
        "",
    ]
    return "\n".join(lines)


def generate_topic_readme(topic: str, problems: list[dict]) -> str:
    """Generate a README.md for a topic subdirectory."""
    title = topic.replace("-", " ").title()
    desc = TOPIC_DESCRIPTIONS.get(topic, "")

    lines = [
        f"# {title}",
        "",
        desc,
        "",
        "| Problem | Difficulty | Full Walkthrough | Practice |",
        "|---------|-----------|-----------------|----------|",
    ]
    for p in problems:
        slug = p["slug"]
        name = p["name"]
        diff = p["difficulty"]
        blog = f"https://intervu.dev/blog/walkthroughs/{slug}-interview-walkthrough/"
        practice = f"https://intervu.dev/setup2?problem={slug}"
        lines.append(
            f"| [{name}]({slug}.md) | {diff} "
            f"| [Read →]({blog}) | [Practice →]({practice}) |"
        )
    lines += [
        "",
        "---",
        "",
        f"*Part of the [Coding Interview Walkthroughs]({GITHUB_REPO}) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*",
        "",
    ]
    return "\n".join(lines)


MIN_CONTENT_LENGTH = 500  # minimum chars for a generated problem file

REQUIRED_SECTIONS = ["## Problem", "## Solution", "## Complexity", "## Common Interview Mistakes"]

EXPECTED_LINK_PATTERNS = [
    r"https://intervu\.dev/blog/walkthroughs/[\w-]+-interview-walkthrough/",
    r"https://intervu\.dev/setup2\?problem=[\w-]+",
    r"https://intervu\.dev/blog/how-to-prepare-for-coding-interview/",
    r"https://intervu\.dev/blog/grind-75-practice-pathway/",
    r"https://intervu\.dev/blog/why-leetcode-is-not-enough/",
]


def validate_output(slug: str, content: str, topic: str) -> list[str]:
    """Run QA checks on a generated problem file. Returns list of warnings."""
    warnings = []

    # 1. Missing topic mapping
    if slug not in TOPIC_MAP:
        warnings.append(f"WARN  slug '{slug}' not in TOPIC_MAP (landed in '{topic}/')")

    # 2. Missing difficulty mapping
    if slug not in DIFFICULTY_MAP:
        warnings.append(f"WARN  slug '{slug}' not in DIFFICULTY_MAP (defaulted)")

    # 3. Missing required sections
    for section in REQUIRED_SECTIONS:
        if section not in content:
            warnings.append(f"ERROR missing section '{section}'")

    # 4. Minimum content length
    if len(content) < MIN_CONTENT_LENGTH:
        warnings.append(
            f"WARN  content too short ({len(content)} chars, min {MIN_CONTENT_LENGTH})"
        )

    # 5. Broken/missing intervu.dev links
    for pattern in EXPECTED_LINK_PATTERNS:
        if not re.search(pattern, content):
            warnings.append(f"ERROR missing expected link pattern: {pattern}")

    # 6. Em dashes still present (cleanup failure)
    if "—" in content:
        count = content.count("—")
        warnings.append(f"WARN  {count} em dash(es) still present after cleanup")

    # 7. Canonical attribution present
    if "Originally published at" not in content:
        warnings.append(f"ERROR missing canonical attribution line")

    return warnings


def main():
    pattern = os.path.join(BLOG_DIR, "*-interview-walkthrough.md")
    files = sorted(glob.glob(pattern))

    if not files:
        print(f"No walkthrough files found in {BLOG_DIR}")
        return

    # Clean out old flat files (but keep subdirectories that may already exist)
    for f in glob.glob(os.path.join(OUT_DIR, "*.md")):
        os.remove(f)

    # Track problems per topic for README generation
    topic_problems: dict[str, list[dict]] = {}

    # Duplicate slug detection
    seen_slugs: set[str] = set()

    count = 0
    all_warnings: list[str] = []
    has_errors = False

    # --- Pass 1: collect all problem metadata ---
    problem_data: list[dict] = []
    for src in files:
        filename = os.path.basename(src)
        slug = filename.replace("-interview-walkthrough.md", "")

        if slug in seen_slugs:
            all_warnings.append(f"[{slug}] ERROR duplicate slug detected")
            has_errors = True
            continue
        seen_slugs.add(slug)

        with open(src) as f:
            content = f.read()

        fm, body = parse_frontmatter(content)
        topic = TOPIC_MAP.get(slug, "other")
        title = fm.get("title", slug)
        problem_name = title.replace(" — Coding Interview Walkthrough", "")
        difficulty = extract_difficulty(slug, fm.get("tags", []))

        problem_data.append({
            "src": src,
            "slug": slug,
            "fm": fm,
            "body": body,
            "topic": topic,
            "name": problem_name,
            "difficulty": difficulty,
        })

    # Build topic → problems index for cross-linking
    topic_problems: dict[str, list[dict]] = {}
    for p in problem_data:
        topic_problems.setdefault(p["topic"], []).append({
            "slug": p["slug"],
            "name": p["name"],
            "difficulty": p["difficulty"],
        })

    # --- Pass 2: generate files with cross-links ---
    for p in problem_data:
        slug = p["slug"]
        topic = p["topic"]

        # Related = same-topic siblings, excluding self
        related = [r for r in topic_problems.get(topic, []) if r["slug"] != slug]

        condensed = generate_condensed(p["fm"], p["body"], slug, related=related)
        condensed = cleanup_ai_patterns(condensed)

        topic_dir = os.path.join(OUT_DIR, topic)
        os.makedirs(topic_dir, exist_ok=True)

        # QA validation
        warnings = validate_output(slug, condensed, topic)
        for w in warnings:
            tag = f"[{topic}/{slug}]"
            all_warnings.append(f"  {tag} {w}")
            if w.startswith("ERROR"):
                has_errors = True

        out_path = os.path.join(topic_dir, f"{slug}.md")
        with open(out_path, "w") as f:
            f.write(condensed)

        count += 1
        print(f"✓ {topic}/{slug}")

    # Generate per-topic READMEs
    for topic, problems in topic_problems.items():
        readme_path = os.path.join(OUT_DIR, topic, "README.md")
        readme_content = generate_topic_readme(topic, problems)
        with open(readme_path, "w") as f:
            f.write(readme_content)
        print(f"📄 {topic}/README.md")

    print(f"\nSynced {count} walkthrough(s) to {OUT_DIR}")

    # QA report
    if all_warnings:
        print(f"\n{'='*60}")
        print(f"QA Report: {len(all_warnings)} issue(s) found")
        print(f"{'='*60}")
        for w in all_warnings:
            print(w)
        if has_errors:
            print(f"\n❌ ERRORS found. Review before committing.")
            raise SystemExit(1)
        else:
            print(f"\n⚠️  Warnings only. Safe to commit, but review recommended.")
    else:
        print(f"\n✅ QA passed: no issues found.")


if __name__ == "__main__":
    main()

