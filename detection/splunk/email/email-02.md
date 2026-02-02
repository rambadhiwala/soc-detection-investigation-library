# EMAIL-02 — Suspicious Attachment Delivery (Executable/Archive)

**Category:** email  
**Suggested Severity:** HIGH  
**MITRE ATT&CK:** T1566 Phishing

## What this detects
Detects inbound emails with risky attachment types (archives, ISO, executable-like extensions) from external senders.

## Data requirements
This detection expects authentication/email/endpoint/cloud/DLP events that include (as applicable):
- timestamp
- user / account
- source IP and/or device identifier
- action/result (success/failure/operation)
- host/application context (mailbox, endpoint, SharePoint, etc.)

If your environment uses different field names, map them in a normalization layer or adjust the query.

## Triage steps (Tier‑1)
1. **Confirm scope:** single user vs multiple users, single IP vs many IPs.
2. **Establish baseline:** is this user/admin known to travel or use VPN?
3. **Check success indicators:** any successful login/execution following failures?
4. **Enrich:** reputation for IP/domain, prior history for the user, device posture.
5. **Decide:** TP/FP/needs escalation.
6. **Document:** include a short timeline and evidence links.

## Common false positives
- Password resets causing bursts of failures
- VPN egress IPs shared by many users
- Legitimate bulk operations (SharePoint migrations, mail forwarding for business use)
- Security testing or monitoring tools (approved scanners)

## Tuning suggestions
- Exclude known corporate VPN ranges (if approved)
- Add thresholds per user group (admins vs standard users)
- Use “new device” or “new geo” as a confidence booster
- Add allow-lists for sanctioned automation accounts

## Escalation criteria
Escalate if any of the following are true:
- privileged/admin account involved
- success indicators present (successful login, rule created, large download)
- sensitive data is involved
- behavior is repeated or escalating over time

## References (general)
- MITRE ATT&CK technique: **T1566 Phishing**
