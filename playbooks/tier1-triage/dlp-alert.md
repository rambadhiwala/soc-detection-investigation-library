# Playbook: DLP Alert Investigation (Tier‑1)

## Goal
Understand what data was involved, whether it left the organization, and whether it is malicious or policy-related.

## Steps
1. Identify the DLP policy and matched condition (PII/PCI/PHI/Confidential)
2. Identify channel (email/cloud/endpoint/web)
3. Determine if the action was blocked or allowed
4. Validate destination (external domain, cloud app, removable media)
5. Check repeat behavior and user risk context

## Outcomes
- **Benign true positive:** policy violation, non-malicious
- **True positive:** suspicious exfiltration attempt or confirmed leakage
- **False positive:** incorrect classification, allowed business process

## Escalate when
- sensitive data confirmed + external destination
- repeated behavior or escalating pattern
- correlated suspicious login or endpoint signals
