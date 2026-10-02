#!/usr/bin/env bash
# The gate for one role of the skill line. Exit 0 = green, anything else = red; the output is the
# role's feedback. Usage: SKILL=<name> ./gate.sh <builder|cleaner|reviewer>
# Without SKILL, the skill is the one top-level <name>/SKILL.md changed since $BASE (default
# skills/2026.11) or in the working tree; anything other than exactly one is red.
# Line of record: /opt/brain/docs/issues/ai4bcm-skills/build-plan-2026.11.md, ticket 61.
set -uo pipefail
cd "$(dirname "$0")" || exit 3
role="${1:?role}"
BASE="${BASE:-skills/2026.11}"
skill="${SKILL:-}"
if [ -z "$skill" ]; then
  skill=$( { git diff --name-only "$BASE"...HEAD 2>/dev/null; git status --porcelain -uall | cut -c4-; } \
           | grep -E '^[^/]+/SKILL\.md$' | cut -d/ -f1 | sort -u )
  if [ "$(printf '%s\n' "$skill" | grep -c .)" -ne 1 ]; then
    echo "cannot tell which skill this walk is for (changed: ${skill:-none}); set SKILL=<name>"
    exit 3
  fi
fi
echo "### skill: $skill"

case "$role" in
  builder)
    python3 tools/skill_check.py "$skill"
    ;;
  cleaner)
    # The builder's commit is HEAD while the cleaner works: its body is the length to beat.
    left=$(git show "HEAD:$skill/SKILL.md" 2>/dev/null | python3 -c 'import sys; sys.path.insert(0, "tools"); import skill_check as s; print(s.words(s.split_frontmatter(sys.stdin.read())[1]))')
    python3 tools/skill_check.py "$skill" --clean ${left:+--max-words "$left"}
    ;;
  reviewer)
    python3 tools/skill_check.py "$skill" --review
    ;;
  *) echo "unknown role $role"; exit 3 ;;
esac
