#!/usr/bin/env python3
"""Render the profile README SVGs (header, stats, languages).

Live numbers come from the GitHub GraphQL API. Static copy mirrors the
portfolio (faqihhakim.tech: site.config.ts, lib/copy.ts) and must be
updated by hand when the portfolio changes. No timestamps are rendered,
so the workflow only commits when a number actually changes.
"""

import html
import json
import os
import re
import sys
import urllib.error
import urllib.request
from collections import Counter

GRAPHQL_URL = "https://api.github.com/graphql"
OUTPUT_DIR = "svg"
WIDTH = 960

# Portfolio palette (porto/tailwind.config.js).
PAPER = "#F8F7F3"
BORDER = "#DED8CA"
GRID = "#C8BAA3"
INK = "#161512"
MUTED = "#77664F"
SUBTLE = "#AD9D7F"
ACCENT = "#B7361A"
STATUS = "#0F9D58"

# Dark variant: same layout, palette remapped in one pass (zen scale
# inverted, accent lifted for contrast on the dark paper).
DARK = {
    PAPER: "#161512",
    BORDER: "#40372F",
    GRID: "#5F5142",
    INK: "#F0EEE8",
    MUTED: "#AD9D7F",
    SUBTLE: "#8A7A62",
    ACCENT: "#E8664A",
    STATUS: "#34C77B",
}
DARK_PATTERN = re.compile("|".join(map(re.escape, DARK)))

SERIF = "Newsreader, Georgia, 'Times New Roman', serif"
SANS = "Inter, 'Segoe UI', system-ui, sans-serif"
MONO = "'Roboto Mono', ui-monospace, SFMono-Regular, Menlo, monospace"

PROFILE = {
    "name": "Muhammad Faqih Hakim",
    "initials": "FH",
    "title": "AI/ML Engineer",
    "focus": "Agentic AI · Graph ML · HPC / Local LLMs",
    "now": "AI Engineer, Transformation Office @ PT Tunas Ridean Tbk",
    "status": "Open to full-time roles · early 2027",
    "location": "JAKARTA, ID",
}

STATIC_STATS = [
    ("3.88", "GPA · cum laude"),
    ("42", "certifications"),
    ("400+", "students mentored"),
]

QUERY = """
query($login: String!, $after: String) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar { totalContributions }
    }
    repositories(first: 100, after: $after, ownerAffiliations: OWNER,
                 isFork: false, privacy: PUBLIC) {
      totalCount
      pageInfo { hasNextPage endCursor }
      nodes {
        stargazerCount
        primaryLanguage { name color }
      }
    }
  }
}
"""


def esc(value):
    return html.escape(str(value), quote=True)


def graphql(token, variables):
    request = urllib.request.Request(
        GRAPHQL_URL,
        data=json.dumps({"query": QUERY, "variables": variables}).encode(),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "profile-assets",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        data = json.loads(response.read())
    if "errors" in data:
        raise RuntimeError(json.dumps(data["errors"]))
    return data["data"]["user"]


def fetch_profile(token, login):
    after, repos, user = None, [], None
    while True:
        user = graphql(token, {"login": login, "after": after})
        page = user["repositories"]
        repos += page["nodes"]
        if not page["pageInfo"]["hasNextPage"]:
            break
        after = page["pageInfo"]["endCursor"]
    return {
        "contributions": user["contributionsCollection"]["contributionCalendar"]["totalContributions"],
        "repo_count": user["repositories"]["totalCount"],
        "stars": sum(repo["stargazerCount"] for repo in repos),
        "repos": repos,
    }


def fetch_with_fallback(login):
    # STATS_TOKEN (PAT) sees private contributions but expires; the
    # workflow's own GITHUB_TOKEN never expires, so it is the fallback.
    tokens = [(name, os.environ.get(name)) for name in ("STATS_TOKEN", "GITHUB_TOKEN")]
    tokens = [(name, token) for name, token in tokens if token]
    if not tokens:
        sys.exit("Set STATS_TOKEN or GITHUB_TOKEN")
    for index, (name, token) in enumerate(tokens):
        try:
            return fetch_profile(token, login)
        except urllib.error.HTTPError as exc:
            if exc.code not in (401, 403) or index == len(tokens) - 1:
                raise
            print(f"::warning::{name} rejected (HTTP {exc.code}); falling back", file=sys.stderr)


def compact(value):
    return f"{value / 1000:.1f}k".replace(".0k", "k") if value >= 10_000 else f"{value:,}"


def card(height, label, body):
    return (
        f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {WIDTH} {height}' width='100%' "
        f"role='img' aria-label='{esc(label)}'><title>{esc(label)}</title>"
        "<defs><pattern id='g' width='32' height='32' patternUnits='userSpaceOnUse'>"
        f"<path d='M32 0H0V32' fill='none' stroke='{GRID}' stroke-opacity='.28'/></pattern></defs>"
        f"<rect x='.5' y='.5' width='{WIDTH - 1}' height='{height - 1}' rx='14' fill='{PAPER}' stroke='{BORDER}'/>"
        f"<rect x='.5' y='.5' width='{WIDTH - 1}' height='{height - 1}' rx='14' fill='url(#g)'/>"
        f"{body}</svg>\n"
    )


def text(x, y, content, font, size, fill, extra=""):
    return f"<text x='{x}' y='{y}' font-family=\"{font}\" font-size='{size}' fill='{fill}' {extra}>{esc(content)}</text>"


def render_header():
    p = PROFILE
    body = "".join([
        f"<circle cx='44' cy='45' r='5' fill='{STATUS}'/>",
        text(58, 50, p["status"].upper(), MONO, 12, MUTED, "letter-spacing='1.2'"),
        text(916, 50, p["location"], MONO, 12, SUBTLE, "text-anchor='end' letter-spacing='1.2'"),
        text(36, 122, p["name"], SERIF, 52, INK, "font-weight='500' letter-spacing='-1'"),
        text(38, 160, p["title"], SANS, 21, ACCENT, "font-weight='600'"),
        text(208, 160, p["focus"], SANS, 18, MUTED),
        f"<line x1='38' y1='184' x2='922' y2='184' stroke='{BORDER}'/>",
        text(38, 210, "NOW", MONO, 11, ACCENT, "font-weight='700' letter-spacing='1.5'"),
        text(82, 210, p["now"], MONO, 13, INK),
        f"<g transform='rotate(-4 860 120)'>"
        f"<rect x='822' y='84' width='76' height='76' rx='8' fill='{ACCENT}'/>"
        f"<rect x='828' y='90' width='64' height='64' rx='5' fill='none' stroke='{PAPER}' stroke-opacity='.7'/>"
        + text(860, 134, p["initials"], SERIF, 34, PAPER, "text-anchor='middle' font-weight='600'")
        + "</g>",
    ])
    return card(236, f"{p['name']}, {p['title']}: {p['focus']}", body)


def render_stats(data):
    cells = [
        (compact(data["contributions"]), "contributions"),
        (str(data["repo_count"]), "public repos"),
        (str(data["stars"]), "stars earned"),
        *STATIC_STATS,
    ]
    cell_w = (WIDTH - 64) / len(cells)
    parts = []
    for index, (value, label) in enumerate(cells):
        x = 32 + index * cell_w
        if index:
            parts.append(f"<line x1='{x:.1f}' y1='30' x2='{x:.1f}' y2='94' stroke='{BORDER}'/>")
        parts.append(text(f"{x + 18:.1f}", 68, value, SERIF, 36, ACCENT if index < 3 else INK, "font-weight='500'"))
        parts.append(text(f"{x + 18:.1f}", 90, label.upper(), MONO, 10, MUTED, "letter-spacing='1'"))
    summary = ", ".join(f"{value} {label}" for value, label in cells)
    return card(124, f"Stats: {summary}", "".join(parts))


def render_languages(repos, top=5):
    colors = {}
    counts = Counter()
    for repo in repos:
        language = repo["primaryLanguage"]
        if language:
            counts[language["name"]] += 1
            colors[language["name"]] = language["color"] or SUBTLE
    total = sum(counts.values()) or 1
    ranked = counts.most_common(top)
    other = total - sum(count for _, count in ranked)
    if other:
        ranked.append(("Other", other))
        colors["Other"] = BORDER

    bar_x, bar_w = 36, WIDTH - 72
    parts = [
        text(36, 46, "LANGUAGES", MONO, 11, ACCENT, "font-weight='700' letter-spacing='1.5'"),
        text(924, 46, f"primary language across {total} public repos", MONO, 11, SUBTLE, "text-anchor='end'"),
        f"<clipPath id='bar'><rect x='{bar_x}' y='64' width='{bar_w}' height='10' rx='5'/></clipPath>",
        "<g clip-path='url(#bar)'>",
    ]
    x = bar_x
    for name, count in ranked:
        width = bar_w * count / total
        parts.append(f"<rect x='{x:.1f}' y='64' width='{width + 0.5:.1f}' height='10' fill='{colors[name]}'/>")
        x += width
    parts.append("</g>")

    col_w = bar_w / 3
    for index, (name, count) in enumerate(ranked):
        cx = bar_x + (index % 3) * col_w
        cy = 108 + (index // 3) * 28
        parts.append(f"<circle cx='{cx + 5:.1f}' cy='{cy - 4}' r='5' fill='{colors[name]}'/>")
        parts.append(text(f"{cx + 18:.1f}", cy, name, SANS, 14, INK, "font-weight='500'"))
        parts.append(text(f"{cx + col_w - 24:.1f}", cy, f"{count * 100 / total:.0f}%", MONO, 12, MUTED, "text-anchor='end'"))

    rows = (len(ranked) + 2) // 3
    summary = ", ".join(f"{name} {count * 100 / total:.0f}%" for name, count in ranked)
    return card(96 + rows * 28, f"Languages: {summary}", "".join(parts))


def write(name, content):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    variants = {"light": content, "dark": DARK_PATTERN.sub(lambda m: DARK[m.group()], content)}
    for theme, svg in variants.items():
        with open(os.path.join(OUTPUT_DIR, f"{name}-{theme}.svg"), "w", encoding="utf-8") as handle:
            handle.write(svg)


def main():
    login = os.environ.get("GH_USERNAME") or os.environ.get("GITHUB_REPOSITORY_OWNER") or "Fqih"
    data = fetch_with_fallback(login)
    write("header", render_header())
    write("stats", render_stats(data))
    write("langs", render_languages(data["repos"]))
    print(f"{login}: {data['contributions']} contributions, {data['repo_count']} repos, {data['stars']} stars")


if __name__ == "__main__":
    main()
