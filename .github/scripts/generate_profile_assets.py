#!/usr/bin/env python3

import html
import json
import os
import sys
import urllib.error
import urllib.request
from collections import defaultdict
from datetime import date, datetime, timezone

GRAPHQL_URL = "https://api.github.com/graphql"
CARD_WIDTH = 560
OUTPUT_DIR = "svg"
ACCENTS = ["#4285F4", "#EA4335", "#FBBC04", "#34A853"]

THEMES = {
    "dark": {
        "bg_top": "#171614",
        "bg_bottom": "#1B1916",
        "card_border": "#3B372F",
        "surface": "#23211D",
        "surface_border": "#3F3A33",
        "text": "#F4EFE7",
        "muted": "#B7AEA1",
        "subtle": "#90877A",
        "accent_soft": "#2D2923",
    },
    "light": {
        "bg_top": "#F7F3EB",
        "bg_bottom": "#F4F0E7",
        "card_border": "#E5DDD0",
        "surface": "#FFFCF7",
        "surface_border": "#ECE4D8",
        "text": "#1E1C19",
        "muted": "#6D655A",
        "subtle": "#8B8173",
        "accent_soft": "#EEE6DA",
    },
}

OVERVIEW_QUERY = """
query($login: String!) {
  user(login: $login) {
    followers {
      totalCount
    }
    pullRequests {
      totalCount
    }
    issues {
      totalCount
    }
    publicRepositories: repositories(ownerAffiliations: OWNER, isFork: false, privacy: PUBLIC) {
      totalCount
    }
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            date
            contributionCount
          }
        }
      }
    }
  }
}
"""

PRIVATE_REPO_COUNT_QUERY = """
query($login: String!) {
  user(login: $login) {
    privateRepositories: repositories(ownerAffiliations: OWNER, isFork: false, privacy: PRIVATE) {
      totalCount
    }
  }
}
"""

REPOS_QUERY = """
query($login: String!, $after: String) {
  user(login: $login) {
    repositories(
      first: 50
      after: $after
      ownerAffiliations: OWNER
      isFork: false
      privacy: PUBLIC
      orderBy: {field: STARGAZERS, direction: DESC}
    ) {
      pageInfo {
        hasNextPage
        endCursor
      }
      nodes {
        name
        stargazerCount
        primaryLanguage {
          name
          color
        }
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
          edges {
            size
            node {
              name
              color
            }
          }
        }
      }
    }
  }
}
"""


def require_env(name, fallback=None):
    value = os.environ.get(name, fallback)
    if value:
        return value
    print(f"Missing required environment variable: {name}", file=sys.stderr)
    sys.exit(1)


def escape(value):
    return html.escape(str(value), quote=True)


def fmt_number(value):
    if value >= 1_000_000:
        return f"{value / 1_000_000:.1f}M"
    if value >= 1_000:
        return f"{value / 1_000:.1f}k"
    return str(value)


def graphql_request(token, query, variables):
    payload = json.dumps({"query": query, "variables": variables}).encode("utf-8")
    request = urllib.request.Request(
        GRAPHQL_URL,
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "profile-stats-generator",
        },
    )
    try:
        with urllib.request.urlopen(request) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        details = exc.read().decode("utf-8", errors="replace")
        print(details, file=sys.stderr)
        raise

    if "errors" in data:
        raise RuntimeError(json.dumps(data["errors"]))

    return data["data"]


def compute_streaks(weeks):
    contribution_days = []
    for week in weeks:
        for day in week["contributionDays"]:
            contribution_days.append(
                (datetime.strptime(day["date"], "%Y-%m-%d").date(), day["contributionCount"])
            )

    contribution_days.sort(key=lambda item: item[0])
    longest = 0
    running = 0

    for _, count in contribution_days:
        if count > 0:
            running += 1
            longest = max(longest, running)
        else:
            running = 0

    current = 0
    by_day = {day: count for day, count in contribution_days}
    cursor = datetime.now(timezone.utc).date()
    if by_day.get(cursor, 0) == 0:
        cursor = date.fromordinal(cursor.toordinal() - 1)

    while by_day.get(cursor, 0) > 0:
        current += 1
        cursor = date.fromordinal(cursor.toordinal() - 1)

    return current, longest


def fetch_repositories(token, username):
    repositories = []
    after = None

    while True:
        data = graphql_request(token, REPOS_QUERY, {"login": username, "after": after})
        connection = data["user"]["repositories"]
        repositories.extend(connection["nodes"])
        if not connection["pageInfo"]["hasNextPage"]:
            return repositories
        after = connection["pageInfo"]["endCursor"]


def aggregate_languages(repositories):
    language_sizes = defaultdict(int)
    language_colors = {}
    language_repos = defaultdict(int)

    for repo in repositories:
        repo_languages = set()
        for edge in repo["languages"]["edges"]:
            language = edge["node"]["name"]
            if not language:
                continue
            language_sizes[language] += edge["size"]
            repo_languages.add(language)
            if edge["node"]["color"]:
                language_colors[language] = edge["node"]["color"]

        primary = repo.get("primaryLanguage")
        if primary and primary.get("name") and primary.get("color"):
            language_colors.setdefault(primary["name"], primary["color"])

        for language in repo_languages:
            language_repos[language] += 1

    total_size = sum(language_sizes.values())
    top_languages = sorted(language_sizes.items(), key=lambda item: item[1], reverse=True)[:6]
    return top_languages, total_size, language_colors, language_repos


def svg_open(height, theme, title, description, transparent=False):
    palette = THEMES[theme]
    shadow = "rgba(83,73,55,0.10)" if theme == "light" else "rgba(0,0,0,0.28)"
    grid_major = "rgba(160,140,108,0.10)" if theme == "light" else "rgba(255,255,255,0.06)"
    grid_minor = "rgba(160,140,108,0.06)" if theme == "light" else "rgba(255,255,255,0.03)"
    parts = [
        f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {CARD_WIDTH} {height}' "
        f"width='{CARD_WIDTH}' height='{height}' role='img' aria-labelledby='title desc' "
        "font-family=\"Poppins, 'Segoe UI', Roboto, sans-serif\">",
        f"<title>{escape(title)}</title>",
        f"<desc>{escape(description)}</desc>",
    ]

    parts.append(
        "<defs>"
        "<linearGradient id='card-bg' x1='0' y1='0' x2='0' y2='1'>"
        f"<stop offset='0%' stop-color='{palette['bg_top']}'/>"
        f"<stop offset='100%' stop-color='{palette['bg_bottom']}'/>"
        "</linearGradient>"
        "<pattern id='grid-minor' width='44' height='44' patternUnits='userSpaceOnUse'>"
        f"<path d='M 44 0 L 0 0 0 44' fill='none' stroke='{grid_minor}' stroke-width='1'/>"
        "</pattern>"
        "<pattern id='grid-major' width='176' height='176' patternUnits='userSpaceOnUse'>"
        f"<rect width='176' height='176' fill='url(#grid-minor)'/>"
        f"<path d='M 176 0 L 0 0 0 176' fill='none' stroke='{grid_major}' stroke-width='1'/>"
        "</pattern>"
        "<filter id='soft-shadow' x='-10%' y='-10%' width='120%' height='130%'>"
        f"<feDropShadow dx='0' dy='8' stdDeviation='12' flood-color='{shadow}' flood-opacity='1'/>"
        "</filter>"
        "<style>"
        ".frame{fill:url(#card-bg);stroke:"
        f"{palette['card_border']};stroke-opacity:.55;stroke-width:1;filter:url(#soft-shadow);"
        "}"
        ".surface{fill:"
        f"{palette['surface']};stroke:{palette['surface_border']};stroke-opacity:.38;stroke-width:1;"
        "}"
        ".title{fill:"
        f"{palette['text']};font-size:22px;font-weight:700;letter-spacing:-.02em;"
        "}"
        ".subtitle{fill:"
        f"{palette['muted']};font-size:12px;font-weight:400;"
        "}"
        ".eyebrow{fill:"
        f"{palette['muted']};font-size:11px;font-weight:700;letter-spacing:.08em;"
        "}"
        ".value-xl{fill:"
        f"{palette['text']};font-size:30px;font-weight:700;letter-spacing:-.03em;"
        "}"
        ".value-lg{fill:"
        f"{palette['text']};font-size:18px;font-weight:700;letter-spacing:-.02em;"
        "}"
        ".hint{fill:"
        f"{palette['subtle']};font-size:11px;font-weight:400;"
        "}"
        ".footer{fill:"
        f"{palette['subtle']};font-size:11px;font-weight:400;"
        "}"
        ".body{fill:"
        f"{palette['text']};font-size:14px;font-weight:700;letter-spacing:-.01em;"
        "}"
        ".meta{fill:"
        f"{palette['muted']};font-size:11px;font-weight:400;"
        "}"
        ".track{fill:"
        f"{palette['accent_soft']};"
        "}"
        ".grid{fill:url(#grid-major);opacity:.9;}"
        ".soft-badge{fill:"
        f"{palette['accent_soft']};"
        "}"
        "</style>"
        "</defs>"
    )
    parts.append(
        f"<rect class='frame' x='0.5' y='0.5' width='{CARD_WIDTH - 1}' height='{height - 1}' rx='20'/>"
    )
    parts.append(
        f"<rect class='grid' x='0.5' y='0.5' width='{CARD_WIDTH - 1}' height='{height - 1}' rx='20'/>"
    )
    strip_y = 0 if not transparent else 8
    strip_x = 1 if not transparent else 20
    strip_w = (CARD_WIDTH - 2) / 4 if not transparent else (CARD_WIDTH - 40) / 4
    strip_h = 4
    strip_rx = 20 if not transparent else 3
    for index, color in enumerate(ACCENTS):
        x = strip_x + index * strip_w
        parts.append(
            f"<rect x='{x}' y='{strip_y}' width='{strip_w}' height='{strip_h}' rx='{strip_rx if index in (0, 3) else 0}' fill='{color}'/>"
        )

    return "".join(parts)


def svg_close():
    return "</svg>"


def render_stats_card(stats, updated_label, theme):
    cols = 3
    card_pad = 28
    cell_gap = 16
    cell_w = 157
    cell_h = 96
    rows = (len(stats) + cols - 1) // cols
    grid_top = 94
    footer_y = grid_top + rows * (cell_h + cell_gap) + 8
    height = footer_y + 28

    parts = [
        svg_open(
            height=height,
            theme=theme,
            title="GitHub Overview",
            description="Overview card generated from the GitHub GraphQL API.",
        )
    ]
    parts.append(
        f"<text class='title' x='{card_pad}' y='44'>GitHub Overview</text>"
    )
    parts.append(
        f"<text class='subtitle' x='{card_pad}' y='68'>"
        "Public GitHub activity pulled directly from the GitHub API.</text>"
    )

    for index, stat in enumerate(stats):
        row = index // cols
        col = index % cols
        x = card_pad + col * (cell_w + cell_gap)
        y = grid_top + row * (cell_h + cell_gap)
        accent = ACCENTS[index % len(ACCENTS)]

        parts.append(
            f"<rect class='surface' x='{x}' y='{y}' width='{cell_w}' height='{cell_h}' rx='18'/>"
        )
        parts.append(f"<rect x='{x}' y='{y}' width='{cell_w}' height='3' rx='1.5' fill='{accent}'/>")
        parts.append(
            f"<circle cx='{x + 24}' cy='{y + 28}' r='7' fill='none' stroke='{accent}' stroke-width='1.2'/>"
        )
        parts.append(
            f"<text class='eyebrow' x='{x + 40}' y='{y + 32}'>"
            f"{escape(stat['label']).upper()}</text>"
        )
        parts.append(
            f"<text class='value-xl' x='{x + 18}' y='{y + 66}'>"
            f"{escape(stat['value'])}</text>"
        )
        parts.append(
            f"<text class='hint' x='{x + 18}' y='{y + 86}'>"
            f"{escape(stat['hint'])}</text>"
        )

    parts.append(
        f"<text class='footer' x='{card_pad}' y='{height - 14}'>{escape(updated_label)}</text>"
    )
    parts.append(svg_close())
    return "".join(parts)


def render_streak_card(current_streak, longest_streak, total_contributions, updated_label, theme):
    palette = THEMES[theme]
    height = 224
    parts = [
        svg_open(
            height=height,
            theme=theme,
            title="Contribution Streak",
            description="Contribution streak summary from the GitHub contribution calendar.",
            transparent=True,
        )
    ]
    parts.append(
        f"<text class='title' x='24' y='44'>Contribution Streak</text>"
    )
    parts.append(
        f"<text class='subtitle' x='24' y='68'>"
        "Live streak summary generated from your contribution calendar.</text>"
    )
    parts.append(
        f"<rect class='surface' x='28' y='92' width='238' height='92' rx='18'/>"
    )
    parts.append(
        f"<rect class='surface' x='294' y='92' width='238' height='92' rx='18'/>"
    )
    parts.append(
        f"<rect x='28' y='92' width='238' height='3' rx='1.5' fill='{ACCENTS[1]}'/>"
    )
    parts.append(
        f"<rect x='294' y='92' width='238' height='3' rx='1.5' fill='{ACCENTS[0]}'/>"
    )
    parts.append(
        f"<circle cx='76' cy='138' r='19' fill='none' stroke='{ACCENTS[1]}' stroke-width='1.4'/>"
    )
    parts.append(
        f"<circle cx='342' cy='138' r='19' fill='none' stroke='{ACCENTS[0]}' stroke-width='1.4'/>"
    )
    parts.append(f"<text x='76' y='145' text-anchor='middle' fill='{ACCENTS[1]}' font-size='16' font-weight='700'>🔥</text>")
    parts.append(f"<text x='342' y='145' text-anchor='middle' fill='{ACCENTS[0]}' font-size='16' font-weight='700'>⚡</text>")
    parts.append(
        f"<text class='eyebrow' x='110' y='122'>CURRENT STREAK</text>"
    )
    parts.append(
        f"<text class='value-xl' x='110' y='154'>{current_streak} days</text>"
    )
    parts.append(
        "<text class='hint' x='110' y='172'>Active contribution run</text>"
    )
    parts.append(
        f"<text class='eyebrow' x='376' y='122'>LONGEST STREAK</text>"
    )
    parts.append(
        f"<text class='value-xl' x='376' y='154'>{longest_streak} days</text>"
    )
    parts.append(
        "<text class='hint' x='376' y='172'>Best streak so far</text>"
    )
    parts.append(
        f"<text class='subtitle' x='28' y='206'>"
        f"{fmt_number(total_contributions)} contributions tracked in the last 12 months</text>"
    )
    parts.append(
        f"<text class='footer' x='28' y='{height - 14}'>{escape(updated_label)}</text>"
    )
    parts.append(svg_close())
    return "".join(parts)


def render_languages_card(top_languages, total_size, language_colors, language_repos, updated_label, theme):
    items = top_languages[:3]
    height = 236
    card_x = 28
    card_w = CARD_WIDTH - 56
    row_y = 92
    row_h = 38
    row_gap = 18
    track_w = 168

    parts = [
        svg_open(
            height=height,
            theme=theme,
            title="Language Footprint",
            description="Language usage weighted by bytes across public repositories.",
            transparent=True,
        )
    ]
    parts.append(
        f"<text class='title' x='24' y='44'>Language Footprint</text>"
    )
    parts.append(
        f"<text class='subtitle' x='24' y='68'>"
        "Top 3 languages by bytes across public, non-fork repositories.</text>"
    )

    for index, (language, size) in enumerate(items):
        y = row_y + index * (row_h + row_gap)
        color = ACCENTS[index % len(ACCENTS)]
        percent = 0 if total_size == 0 else (size / total_size) * 100
        repo_count = language_repos.get(language, 0)
        progress_w = 0 if total_size == 0 else round((size / total_size) * track_w, 2)

        parts.append(
            f"<rect class='surface' x='{card_x}' y='{y - 6}' width='{card_w}' height='{row_h}' rx='19'/>"
        )
        parts.append(
            f"<circle cx='{card_x + 16}' cy='{y + 11}' r='6' fill='{color}'/>"
        )
        parts.append(
            f"<text class='body' x='{card_x + 32}' y='{y + 15}'>"
            f"{index + 1}. {escape(language)}</text>"
        )
        parts.append(
            f"<text class='meta' x='{card_x + 32}' y='{y + 31}'>"
            f"{percent:.1f}% · {fmt_number(size)} bytes · {repo_count} repos</text>"
        )
        parts.append(
            f"<rect class='track' x='{card_x + 304}' y='{y + 2}' width='{track_w}' height='8' rx='4'/>"
        )
        if progress_w > 0:
            parts.append(
                f"<rect x='{card_x + 304}' y='{y + 2}' width='{progress_w}' height='8' rx='4' fill='{color}'/>"
            )
        parts.append(
            f"<text class='body' x='{card_x + 488}' y='{y + 15}' text-anchor='end'>"
            f"{percent:.1f}%</text>"
        )

    parts.append(
        f"<text class='footer' x='28' y='{height - 14}'>{escape(updated_label)}</text>"
    )
    parts.append(svg_close())
    return "".join(parts)


def contribution_tier(total_contributions):
    if total_contributions >= 1000:
        return "Diamond"
    if total_contributions >= 500:
        return "Platinum"
    if total_contributions >= 250:
        return "Gold"
    if total_contributions >= 100:
        return "Silver"
    return "Bronze"


def streak_tier(longest_streak):
    if longest_streak >= 60:
        return "Relentless"
    if longest_streak >= 30:
        return "Marathon"
    if longest_streak >= 14:
        return "Steady"
    if longest_streak >= 7:
        return "Momentum"
    return "Warm-up"


def follower_tier(followers):
    if followers >= 250:
        return "Amplified"
    if followers >= 100:
        return "Noticed"
    if followers >= 50:
        return "Growing"
    if followers >= 10:
        return "Emerging"
    return "Starting"


def render_trophy_card(
    repositories,
    top_languages,
    total_contributions,
    longest_streak,
    followers,
    prs,
    issues,
    updated_label,
    theme,
):
    top_repo = max(repositories, key=lambda repo: repo["stargazerCount"], default=None)
    top_language = top_languages[0][0] if top_languages else "N/A"

    trophies = [
        {
            "title": "Contribution Tier",
            "value": contribution_tier(total_contributions),
            "detail": f"{fmt_number(total_contributions)} contributions",
        },
        {
            "title": "Consistency Tier",
            "value": streak_tier(longest_streak),
            "detail": f"{longest_streak} day best streak",
        },
        {
            "title": "Community Tier",
            "value": follower_tier(followers),
            "detail": f"{followers} followers",
        },
        {
            "title": "Most Starred Repo",
            "value": top_repo["name"] if top_repo else "N/A",
            "detail": f"{top_repo['stargazerCount']} stars" if top_repo else "No public repos",
        },
        {
            "title": "Primary Strength",
            "value": top_language,
            "detail": "Top weighted language",
        },
        {
            "title": "Collaboration",
            "value": fmt_number(prs + issues),
            "detail": f"{prs} PRs + {issues} issues",
        },
    ]

    cols = 2
    card_pad = 28
    cell_gap = 16
    cell_w = 244
    cell_h = 78
    rows = (len(trophies) + cols - 1) // cols
    grid_top = 94
    footer_y = grid_top + rows * (cell_h + cell_gap) + 8
    height = footer_y + 26

    parts = [
        svg_open(
            height=height,
            theme=theme,
            title="Achievement Board",
            description="Profile highlights generated from public GitHub activity.",
            transparent=True,
        )
    ]
    parts.append(
        f"<text class='title' x='{card_pad}' y='44'>Achievement Board</text>"
    )
    parts.append(
        f"<text class='subtitle' x='{card_pad}' y='68'>"
        "Self-hosted highlights derived from public profile activity.</text>"
    )

    for index, trophy in enumerate(trophies):
        row = index // cols
        col = index % cols
        x = card_pad + col * (cell_w + cell_gap)
        y = grid_top + row * (cell_h + cell_gap)
        accent = ACCENTS[index % len(ACCENTS)]

        parts.append(
            f"<rect class='surface' x='{x}' y='{y}' width='{cell_w}' height='{cell_h}' rx='18'/>"
        )
        parts.append(f"<rect x='{x}' y='{y}' width='{cell_w}' height='3' rx='1.5' fill='{accent}'/>")
        parts.append(
            f"<circle cx='{x + 22}' cy='{y + 26}' r='7' fill='none' stroke='{accent}' stroke-width='1.2'/>"
        )
        parts.append(
            f"<text class='eyebrow' x='{x + 36}' y='{y + 30}'>"
            f"{escape(trophy['title']).upper()}</text>"
        )
        parts.append(
            f"<text class='value-lg' x='{x + 18}' y='{y + 54}'>"
            f"{escape(trophy['value'])}</text>"
        )
        parts.append(
            f"<text class='hint' x='{x + 18}' y='{y + 70}'>"
            f"{escape(trophy['detail'])}</text>"
        )

    parts.append(
        f"<text class='footer' x='{card_pad}' y='{height - 14}'>{escape(updated_label)}</text>"
    )
    parts.append(svg_close())
    return "".join(parts)


def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(content)


def main():
    username = require_env("GH_USERNAME", os.environ.get("GITHUB_REPOSITORY_OWNER"))
    token = require_env("GH_TOKEN", os.environ.get("GITHUB_TOKEN"))
    has_private_repo_token = bool(os.environ.get("GH_TOKEN"))

    overview = graphql_request(token, OVERVIEW_QUERY, {"login": username})["user"]
    repositories = fetch_repositories(token, username)
    private_repo_count = 0
    if has_private_repo_token:
        private_repo_count = graphql_request(token, PRIVATE_REPO_COUNT_QUERY, {"login": username})["user"][
            "privateRepositories"
        ]["totalCount"]

    calendar = overview["contributionsCollection"]["contributionCalendar"]
    total_contributions = calendar["totalContributions"]
    current_streak, longest_streak = compute_streaks(calendar["weeks"])
    followers = overview["followers"]["totalCount"]
    public_repos = overview["publicRepositories"]["totalCount"]
    total_repos = public_repos + private_repo_count
    prs = overview["pullRequests"]["totalCount"]
    issues = overview["issues"]["totalCount"]
    total_stars = sum(repo["stargazerCount"] for repo in repositories)
    top_languages, total_size, language_colors, language_repos = aggregate_languages(repositories)
    updated_label = "Updated " + datetime.now(timezone.utc).strftime("%b %d, %Y %H:%M UTC")

    stats = [
        {"label": "Contributions", "value": fmt_number(total_contributions), "hint": "Last 12 months"},
        {"label": "Current Streak", "value": fmt_number(current_streak), "hint": "Consecutive active days"},
        {"label": "Longest Streak", "value": fmt_number(longest_streak), "hint": "Best run to date"},
        {"label": "Total Stars", "value": fmt_number(total_stars), "hint": "Across public repos"},
        {
            "label": "Total Repos",
            "value": fmt_number(total_repos),
            "hint": (
                f"{public_repos} public · {private_repo_count} private"
                if has_private_repo_token
                else f"{public_repos} public · add STATS_TOKEN for private"
            ),
        },
        {"label": "Followers", "value": fmt_number(followers), "hint": "GitHub community"},
    ]

    for theme in THEMES:
        write_file(f"{OUTPUT_DIR}/custom-stats-{theme}.svg", render_stats_card(stats, updated_label, theme))
        write_file(
            f"{OUTPUT_DIR}/streak-{theme}.svg",
            render_streak_card(
                current_streak=current_streak,
                longest_streak=longest_streak,
                total_contributions=total_contributions,
                updated_label=updated_label,
                theme=theme,
            ),
        )
        write_file(
            f"{OUTPUT_DIR}/top-langs-{theme}.svg",
            render_languages_card(
                top_languages=top_languages,
                total_size=total_size,
                language_colors=language_colors,
                language_repos=language_repos,
                updated_label=updated_label,
                theme=theme,
            ),
        )
        write_file(
            f"{OUTPUT_DIR}/trophy-{theme}.svg",
            render_trophy_card(
                repositories=repositories,
                top_languages=top_languages,
                total_contributions=total_contributions,
                longest_streak=longest_streak,
                followers=followers,
                prs=prs,
                issues=issues,
                updated_label=updated_label,
                theme=theme,
            ),
        )

    write_file(f"{OUTPUT_DIR}/custom-stats.svg", render_stats_card(stats, updated_label, "dark"))
    write_file(
        f"{OUTPUT_DIR}/streak.svg",
        render_streak_card(
            current_streak=current_streak,
            longest_streak=longest_streak,
            total_contributions=total_contributions,
            updated_label=updated_label,
            theme="dark",
        ),
    )
    write_file(
        f"{OUTPUT_DIR}/top-langs.svg",
        render_languages_card(
            top_languages=top_languages,
            total_size=total_size,
            language_colors=language_colors,
            language_repos=language_repos,
            updated_label=updated_label,
            theme="dark",
        ),
    )
    write_file(
        f"{OUTPUT_DIR}/trophy.svg",
        render_trophy_card(
            repositories=repositories,
            top_languages=top_languages,
            total_contributions=total_contributions,
            longest_streak=longest_streak,
            followers=followers,
            prs=prs,
            issues=issues,
            updated_label=updated_label,
            theme="dark",
        ),
    )

    print(
        "Generated theme-aware assets: custom-stats, streak, top-langs, and trophy "
        "for light and dark modes."
    )


if __name__ == "__main__":
    main()
