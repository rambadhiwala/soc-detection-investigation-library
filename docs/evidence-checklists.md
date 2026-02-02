# Evidence Checklists (Tier‑1 SOC)

Use these checklists to collect consistent artifacts for investigations and handoffs.

## Phishing / Email alerts
- Full email headers (Received chain, SPF/DKIM/DMARC results)
- Sender domain reputation, lookalike analysis
- URLs and attachment hashes (if available)
- Targeted recipients and distribution scope
- User interaction (clicked/opened/replied)
- Mailbox rules (forwarding, inbox rules) created after delivery

## Suspicious login / identity alerts
- Username, account type (user/admin/service)
- Source IP + geo + ASN (if available)
- MFA status and failures
- Prior successful logins (baseline)
- Device fingerprint / user agent / client app
- Concurrent sessions, new device registration
- Any password resets or security info changes

## Endpoint execution alerts
- Hostname, user, process tree (parent → child)
- Command line (encoded commands, suspicious flags)
- Network connections from the process
- File writes and persistence locations
- EDR verdict + telemetry details
- Prior similar events on the host

## Cloud data access / exfil alerts
- File sensitivity label / path / owner
- Download volume and time window
- External sharing recipients/domains
- New app consent or API token activity
- Access time anomalies (outside business hours)
- Correlation with suspicious login or endpoint activity

## DLP alerts
- Policy name + matched condition
- Data type (PII/PHI/PCI/Confidential)
- Source and destination (email, cloud share, USB, web upload)
- User role and business justification (if known)
- Repeat behavior (history of violations)
- Whether data actually left the organization (blocked vs allowed)
