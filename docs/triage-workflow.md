# Tier‑1 Triage Workflow (Repeatable)

## Step 1 — Understand the alert
- What detection fired?
- What data source triggered it?
- What asset/user is involved?
- What is the suspected technique?

## Step 2 — Quick validation
- Check for obvious false positives (known automation, known scanners, maintenance windows)
- Confirm basic context (user role, device type, geo baseline)

## Step 3 — Collect evidence
Use the checklists in `/docs/evidence-checklists.md`.

## Step 4 — Decide outcome
- **True Positive**
- **False Positive**
- **Benign True Positive (policy violation)**
- **Needs Escalation / More Context**

## Step 5 — Contain (if authorized)
Common Tier‑1 containment actions (only if allowed):
- disable account / force password reset
- isolate endpoint
- block sender/domain
- revoke sessions

## Step 6 — Document and handoff
Use `/playbooks/escalation/tier1_to_tier2_handoff.md` for consistent escalation notes.

## Step 7 — Tuning feedback
If noisy:
- capture examples
- propose tuning conditions
- record in `/tuning-metrics/false_positive_log.md`
