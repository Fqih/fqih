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

# Dark variant: same layout, palette remapped in one pass onto GitHub's
# dark neutrals so cards blend into the page; accent lifted for contrast.
DARK = {
    PAPER: "#0D1117",
    BORDER: "#30363D",
    GRID: "#3D444D",
    INK: "#E6EDF3",
    MUTED: "#9198A1",
    SUBTLE: "#6E7681",
    ACCENT: "#F0714F",
    STATUS: "#3FB950",
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


def wave_path(top, amp, period, bottom):
    # Two card-widths long so a translateX of -WIDTH loops seamlessly;
    # period must divide WIDTH.
    d = f"M0 {top} Q{period / 4} {top - amp} {period / 2} {top}"
    d += "".join(f" T{x} {top}" for x in range(period, 2 * WIDTH + 1, period // 2))
    return f"{d} V{bottom} H0Z"


def render_waves(height, band=46):
    top = height - band
    layers = [  # (color, opacity, amplitude, period, seconds, reverse)
        (GRID, 0.45, 9, 480, 18, False),
        (SUBTLE, 0.22, 7, 320, 12, True),
        (ACCENT, 0.5, 5, 240, 8, False),
    ]
    style = (
        "<style>"
        f"@keyframes drift{{to{{transform:translateX(-{WIDTH}px)}}}}"
        "@keyframes pulse{50%{opacity:.25}}"
        ".wave{animation:drift linear infinite}.pulse{animation:pulse 2.4s ease-in-out infinite}"
        "@media (prefers-reduced-motion:reduce){.wave,.pulse{animation:none}}"
        "</style>"
    )
    paths = "".join(
        f"<path class='wave' d='{wave_path(top + 10 + index * 10, amp, period, height)}' fill='{color}' "
        f"fill-opacity='{opacity}' style='animation-duration:{seconds}s"
        f"{';animation-direction:reverse' if reverse else ''}'/>"
        for index, (color, opacity, amp, period, seconds, reverse) in enumerate(layers)
    )
    clip = f"<clipPath id='edge'><rect x='1' y='1' width='{WIDTH - 2}' height='{height - 2}' rx='13'/></clipPath>"
    return f"{style}{clip}<g clip-path='url(#edge)'>{paths}</g>"


def language_shares(repos, top=4):
    colors, counts = {}, Counter()
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
    return [(name, count / total, colors[name]) for name, count in ranked]


def render_identity(p):
    return "".join([
        f"<circle class='pulse' cx='44' cy='41' r='5' fill='{STATUS}'/>",
        text(58, 46, p["status"].upper(), MONO, 12, MUTED, "letter-spacing='1.2'"),
        text(916, 46, p["location"], MONO, 12, SUBTLE, "text-anchor='end' letter-spacing='1.2'"),
        text(36, 98, p["name"], SERIF, 44, INK, "font-weight='500' letter-spacing='-1'"),
        text(38, 130, p["title"], SANS, 20, ACCENT, "font-weight='600'"),
        text(202, 130, p["focus"], SANS, 17, MUTED),
        text(38, 158, "NOW", MONO, 11, ACCENT, "font-weight='700' letter-spacing='1.5'"),
        text(82, 158, p["now"], MONO, 13, INK),
        f"<g transform='rotate(-4 880 92)'>"
        f"<rect x='852' y='64' width='56' height='56' rx='6' fill='{ACCENT}'/>"
        f"<rect x='856.5' y='68.5' width='47' height='47' rx='4' fill='none' stroke='{PAPER}' stroke-opacity='.7'/>"
        + text(880, 101, p["initials"], SERIF, 25, PAPER, "text-anchor='middle' font-weight='600'")
        + "</g>",
        f"<line x1='38' y1='178' x2='922' y2='178' stroke='{BORDER}'/>",
    ])


def render_stats_row(data, y=218):
    cells = [
        (compact(data["contributions"]), "contributions"),
        (str(data["repo_count"]), "public repos"),
        (str(data["stars"]), "stars earned"),
        *STATIC_STATS,
    ]
    cell_w = (WIDTH - 76) / len(cells)
    parts = []
    for index, (value, label) in enumerate(cells):
        x = 38 + index * cell_w
        parts.append(text(f"{x:.1f}", y, value, SERIF, 30, ACCENT if index < 3 else INK, "font-weight='500'"))
        parts.append(text(f"{x:.1f}", y + 18, label.upper(), MONO, 10, MUTED, "letter-spacing='1'"))
    return "".join(parts), ", ".join(f"{value} {label}" for value, label in cells)


def render_languages_row(shares, y=266):
    bar_x, bar_w = 38, WIDTH - 76
    parts = [f"<clipPath id='bar'><rect x='{bar_x}' y='{y}' width='{bar_w}' height='6' rx='3'/></clipPath><g clip-path='url(#bar)'>"]
    x = bar_x
    for _, share, color in shares:
        parts.append(f"<rect x='{x:.1f}' y='{y}' width='{bar_w * share + 0.5:.1f}' height='6' fill='{color}'/>")
        x += bar_w * share
    parts.append("</g>")
    x = bar_x
    for name, share, color in shares:
        label = f"{name} {share * 100:.0f}%"
        parts.append(f"<circle cx='{x + 4}' cy='{y + 24}' r='4' fill='{color}'/>")
        parts.append(text(x + 14, y + 28, label, MONO, 11, MUTED))
        x += 14 + len(label) * 7 + 22
    return "".join(parts)


def render_profile(data):
    p = PROFILE
    height = 340
    stats, summary = render_stats_row(data)
    shares = language_shares(data["repos"])
    body = render_waves(height, band=40) + render_identity(p) + stats + render_languages_row(shares)
    languages = ", ".join(f"{name} {share * 100:.0f}%" for name, share, _ in shares)
    return card(height, f"{p['name']}, {p['title']}. {summary}. Languages: {languages}", body)


def write(name, content):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    variants = {"light": content, "dark": DARK_PATTERN.sub(lambda m: DARK[m.group()], content)}
    for theme, svg in variants.items():
        with open(os.path.join(OUTPUT_DIR, f"{name}-{theme}.svg"), "w", encoding="utf-8") as handle:
            handle.write(svg)


def main():
    login = os.environ.get("GH_USERNAME") or os.environ.get("GITHUB_REPOSITORY_OWNER") or "Fqih"
    data = fetch_with_fallback(login)
    write("profile", render_profile(data))
    print(f"{login}: {data['contributions']} contributions, {data['repo_count']} repos, {data['stars']} stars")


if __name__ == "__main__":
    main()
