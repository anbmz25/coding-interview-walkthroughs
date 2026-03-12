#!/usr/bin/env python3
"""
Reads each walkthrough from the Intervu blog source and generates a condensed
GitHub-friendly Markdown version in ../problems/.

Usage:
    python3 scripts/sync_walkthroughs.py
"""

import os
import re
import glob
import yaml

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
BLOG_DIR = os.environ.get(
    "BLOG_DIR",
    os.path.join(REPO_ROOT, "..", "intervu-blog", "src", "content", "blog", "walkthroughs"),
)
OUT_DIR = os.path.join(REPO_ROOT, "problems")
os.makedirs(OUT_DIR, exist_ok=True)

# GitHub repo URL placeholder — update after creating the repo
GITHUB_REPO = "https://github.com/anbmz25/coding-interview-walkthroughs"


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
    "trapping-rain-water": "Hard",
}


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
    # In code comments, use colons
    text = re.sub(r'(#[^\n]*?) — ', r'\1: ', text)
    # In link descriptions ("text — description"), use commas
    text = re.sub(r'(\]\([^)]+\)) — ', r'\1, ', text)
    # General prose: replace with comma, colon, or period depending on context
    # Before a short phrase that completes the sentence, use a colon
    text = re.sub(r' — (O\(|which |so |this |that |the )', r': \1', text)
    # Before an independent clause or aside, use a comma
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


def generate_condensed(fm: dict, body: str, slug: str) -> str:
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
        # Strip any trailing --- from the extracted section to avoid duplicates
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
        "",
        "---",
        "",
        f"*Part of the [Coding Interview Walkthroughs]({GITHUB_REPO}) collection by [Intervu](https://intervu.dev), AI-powered mock interviews with instant feedback.*",
        "",
    ]
    return "\n".join(lines)


def main():
    pattern = os.path.join(BLOG_DIR, "*-interview-walkthrough.md")
    files = sorted(glob.glob(pattern))

    if not files:
        print(f"No walkthrough files found in {BLOG_DIR}")
        return

    count = 0
    for src in files:
        filename = os.path.basename(src)
        slug = filename.replace("-interview-walkthrough.md", "")

        with open(src) as f:
            content = f.read()

        fm, body = parse_frontmatter(content)
        condensed = generate_condensed(fm, body, slug)
        condensed = cleanup_ai_patterns(condensed)

        out_path = os.path.join(OUT_DIR, f"{slug}.md")
        with open(out_path, "w") as f:
            f.write(condensed)

        count += 1
        print(f"✓ {slug}")

    print(f"\nSynced {count} walkthrough(s) to {OUT_DIR}")


if __name__ == "__main__":
    main()
