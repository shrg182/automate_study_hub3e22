# Example Project Instructions for Codex

This is an example instruction file. It is not automatically enforced unless copied into a project instruction location such as `AGENTS.md`, a project README section, or another tool-specific settings file.

## Suggested Instruction Text

```md
# Project Instructions for Codex

When making meaningful changes in this repository, also update:

notes/codex_session_log.md

The log update should include:

- Date
- Files changed
- Summary of work
- Important decisions
- Commands run
- Verification results
- Useful follow-up commands or reminders

Do not update the session log for very small conversation-only replies.

Before editing files, inspect the relevant existing files and follow the current project style.

Do not revert unrelated user changes. If the worktree contains unrelated modified files, leave them alone and mention them only when relevant.
```

## Optional Stronger Version

Use this version if you want every code or documentation change to include a log update.

```md
# Project Instructions for Codex

For every code or documentation change, update:

notes/codex_session_log.md

Each entry should briefly record:

- What changed
- Why it changed
- Which files were touched
- Which commands verified the work
- Any follow-up command the user may want to run

Keep the log concise. Prefer a useful summary over a full transcript.
```

## How to Use

Recommended lightweight setup:

1. Keep `notes/codex_workflow.md` as the human-readable workflow preference.
2. Keep `notes/codex_session_log.md` as the running work history.
3. Copy one instruction block from this file into a future `AGENTS.md` if you want Codex to follow it more consistently.

