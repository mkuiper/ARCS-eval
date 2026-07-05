#!/usr/bin/env python3
"""Write a durable weekly UK AISI / Inspect upstream watch note for ARCS.

This script is intentionally self-contained and cron-friendly: it uses only the
Python standard library plus local git commands. It writes a dated markdown note
under docs/, runs lightweight local validation when the venv exists, and commits
+ pushes the note when there are changes.
"""

from __future__ import annotations

import datetime as dt
import json
import subprocess
import sys
import textwrap
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
LOG_DIR = ROOT / "logs"
REPOS = [
    ("UKGovernmentBEIS/inspect_ai", "High"),
    ("UKGovernmentBEIS/inspect_evals", "Medium"),
    ("UKGovernmentBEIS/inspect_cyber", "Low/medium pattern relevance"),
    ("UKGovernmentBEIS/aisi-sandboxing", "Low immediate relevance"),
]
PYPI_PACKAGES = ["inspect-ai", "inspect-evals"]


def run(cmd: list[str], *, timeout: int = 120, check: bool = False) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=timeout,
        check=check,
    )


def fetch_json(url: str) -> tuple[Any | None, str | None]:
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json, application/json",
            "User-Agent": "ARCS-weekly-upstream-check/1.0",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode("utf-8")), None
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError) as exc:
        return None, str(exc)


def latest_commits(repo: str, limit: int = 5) -> tuple[list[dict[str, str]], str | None]:
    data, err = fetch_json(f"https://api.github.com/repos/{repo}/commits?per_page={limit}")
    if err:
        return [], err
    commits: list[dict[str, str]] = []
    for item in data or []:
        commit = item.get("commit", {})
        commits.append(
            {
                "sha": item.get("sha", "")[:7],
                "date": commit.get("committer", {}).get("date", "unknown"),
                "message": commit.get("message", "").splitlines()[0],
                "url": item.get("html_url", ""),
            }
        )
    return commits, None


def latest_release(repo: str) -> str:
    data, err = fetch_json(f"https://api.github.com/repos/{repo}/releases/latest")
    if err or not isinstance(data, dict):
        return f"not resolved ({err or 'unexpected response'})"
    tag = data.get("tag_name") or data.get("name") or "unknown"
    published = data.get("published_at", "unknown date")
    return f"{tag} ({published})"


def pypi_version(package: str) -> str:
    data, err = fetch_json(f"https://pypi.org/pypi/{package}/json")
    if err or not isinstance(data, dict):
        return f"not resolved ({err or 'unexpected response'})"
    info = data.get("info", {})
    if not isinstance(info, dict):
        return "unknown"
    return str(info.get("version", "unknown"))


def local_package_version(package: str) -> str:
    python = ROOT / ".venv" / "bin" / "python"
    if not python.exists():
        return "local .venv missing"
    proc = run([str(python), "-m", "pip", "show", package], timeout=60)
    if proc.returncode != 0:
        return "not installed"
    for line in proc.stdout.splitlines():
        if line.startswith("Version:"):
            return line.split(":", 1)[1].strip()
    return "installed; version unknown"


def validation_block() -> str:
    python = ROOT / ".venv" / "bin" / "python"
    ruff = ROOT / ".venv" / "bin" / "ruff"
    arcs_tui = ROOT / ".venv" / "bin" / "arcs-tui"
    checks: list[tuple[str, subprocess.CompletedProcess[str]]] = []
    if python.exists():
        checks.append((".venv/bin/python -m pytest -q", run([str(python), "-m", "pytest", "-q"], timeout=300)))
    if ruff.exists():
        checks.append((".venv/bin/ruff check src tests", run([str(ruff), "check", "src", "tests"], timeout=180)))
    if arcs_tui.exists():
        checks.append((".venv/bin/arcs-tui --once", run([str(arcs_tui), "--once"], timeout=120)))
    if not checks:
        return "No local validation run; .venv tools not found.\n"
    parts = []
    for label, proc in checks:
        status = "PASS" if proc.returncode == 0 else f"FAIL ({proc.returncode})"
        excerpt = "\n".join(proc.stdout.splitlines()[:20])
        parts.append(f"$ {label}\nstatus: {status}\n{excerpt}")
    return "\n\n".join(parts) + "\n"


def build_note(now: dt.datetime) -> str:
    today = now.date().isoformat()
    lines = [
        f"# UK AISI / Inspect upstream GitHub check — {today}",
        "",
        f"Date/time checked: {now.isoformat(timespec='seconds')}",
        "",
        "Purpose: weekly upstream monitoring for ARCS (`/home/mike/Projects/companion-ai-safety-eval`) focused on Inspect-compatible, model-agnostic companion-AI safety evaluation, multi-turn roleplay, transcript capture, scorer/rubric behavior, report/viewer support, provider refusal metadata, and sandboxing patterns.",
        "",
        "## Upstream repositories checked",
        "",
        "| Repository | Latest commits observed | Latest release signal | ARCS relevance |",
        "|---|---|---|---|",
    ]
    for repo, relevance in REPOS:
        commits, err = latest_commits(repo)
        if err:
            commit_text = f"not resolved: `{err}`"
        elif commits:
            commit_text = "<br>".join(
                f"[`{c['sha']}`]({c['url']}) — {c['date'][:10]} — {c['message']}" for c in commits
            )
        else:
            commit_text = "no commits returned"
        lines.append(f"| `{repo}` | {commit_text} | {latest_release(repo)} | {relevance} |")

    lines.extend(
        [
            "",
            "## Package/dependency comparison",
            "",
            "| Package | Local version | PyPI latest |",
            "|---|---:|---:|",
        ]
    )
    for package in PYPI_PACKAGES:
        lines.append(f"| `{package}` | `{local_package_version(package)}` | `{pypi_version(package)}` |")

    lines.extend(
        [
            "",
            "## ARCS watch themes",
            "",
            "- Preserve provider refusal / stop metadata when Inspect or target providers expose it; keep provider-specific fields optional.",
            "- Keep transcript handling robust for long-context or attachment-backed content rather than assuming all evidence is inline plain text.",
            "- Treat scorer/assessor exceptions as explicit error or unknown outcomes, never as safe/pass defaults.",
            "- Watch Inspect viewer/reporting changes for future ARCS evidence and rubric review panes.",
            "- Keep browser/sandbox dependencies isolated behind optional extras until needed.",
            "",
            "## Lightweight local verification",
            "",
            "```text",
            validation_block().rstrip(),
            "```",
            "",
            "## Maintenance notes",
            "",
            "This note was generated by `scripts/weekly_upstream_check.py`. The local cron wrapper writes logs to `logs/weekly_upstream_check.log` and commits/pushes dated notes when git has changes.",
            "",
        ]
    )
    return "\n".join(lines)


def commit_if_changed(path: Path) -> str:
    status = run(["git", "status", "--short", str(path.relative_to(ROOT))]).stdout.strip()
    if not status:
        return "No git changes for note."
    run(["git", "add", str(path.relative_to(ROOT))], check=True)
    message = f"docs: add weekly upstream check {path.stem.rsplit('_', 1)[-1]}"
    commit = run(["git", "commit", "-m", message], timeout=120)
    if commit.returncode != 0:
        return f"Git commit skipped/failed:\n{commit.stdout}"
    push = run(["git", "push", "origin", "HEAD"], timeout=300)
    if push.returncode != 0:
        return f"Committed, but push failed:\n{push.stdout}"
    return commit.stdout + "\n" + push.stdout


def main() -> int:
    LOG_DIR.mkdir(exist_ok=True)
    DOCS.mkdir(exist_ok=True)
    now = dt.datetime.now().astimezone()
    note_path = DOCS / f"upstream_uk_aisi_github_check_{now.date().isoformat()}.md"
    note = build_note(now)
    note_path.write_text(note, encoding="utf-8")
    result = commit_if_changed(note_path)
    log_line = f"[{now.isoformat(timespec='seconds')}] wrote {note_path}\n{result}\n\n"
    (LOG_DIR / "weekly_upstream_check.log").open("a", encoding="utf-8").write(log_line)
    print(log_line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
