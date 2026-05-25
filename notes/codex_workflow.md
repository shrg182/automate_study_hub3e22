# Codex Workflow Preference

This file records the preferred working habit for Codex sessions in this project.

## Session Log Practice

After meaningful work, update:

```text
notes/codex_session_log.md
```

Use the session log to preserve a short reviewable record of:

- Date
- Files changed
- Summary of work
- Important decisions
- Commands run
- Verification results
- Useful follow-up commands or reminders

## When to Update the Log

Update the log after changes such as:

- Creating or editing scripts.
- Adding documentation.
- Changing command-line behavior.
- Fixing a bug.
- Running important verification commands.
- Making a decision that should be remembered later.

Small conversation-only replies do not need a log update.

## Suggested Log Entry Format

````md
## YYYY-MM-DD - Short Session Title

### Files Changed

- `path/to/file.py`
- `path/to/file.md`

### Summary

Briefly describe what changed and why.

### Decisions

- Record important choices made during the session.

### Verification

```bash
command_that_was_run
```

### Follow-Up

- Optional next step or reminder.
````

## Preferred Tone

Keep entries practical and easy to review later. The log should explain the work clearly without becoming too long.
