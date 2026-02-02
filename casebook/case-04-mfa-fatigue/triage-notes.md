# Triage Notes (Tier‑1)

## What I checked
- Alert type and detection logic
- Whether the actor/entity is known (baseline check)
- Supporting indicators (success, follow-on activity, repeated pattern)
- Immediate risk (privileged account? sensitive data? user interaction?)

## What I ruled out (common false positives)
- Known internal scanners / monitoring tools
- Approved business processes (migration, bulk operations)
- Shared corporate VPN egress

## Tools / artifacts referenced
- SIEM query snippets (SPL/KQL)
- Email headers / audit logs / process command line (depending on case)
- Evidence checklist from `/docs/evidence-checklists.md`
