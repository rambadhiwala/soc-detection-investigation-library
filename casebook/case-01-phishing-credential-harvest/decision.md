# Decision

## Classification
- **True Positive / Suspicious (Escalated)**

## Rationale (Tier‑1)
- Signal indicates abnormal behavior consistent with the alert type.
- Supporting indicators increase confidence (baseline deviation, repeated pattern, sensitive data context).

## Severity recommendation
- Start with **SEV 2 (High)** when:
  - privileged accounts involved, or
  - success indicators exist, or
  - sensitive data is implicated.

Otherwise, consider **SEV 3 (Medium)** pending Tier‑2 confirmation.
