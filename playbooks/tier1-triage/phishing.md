# Playbook: Phishing Alert Triage (Tier‑1)

## Goal
Confirm whether an email is phishing, assess user impact, and decide containment + escalation.

## Inputs
- Alert details (sender, recipient, subject, URL/attachment indicators)
- Email headers (if available)
- User interaction signals (clicked/opened)

## Steps
1. **Validate sender**
   - Is sender external?
   - Lookalike domain (brand impersonation, typosquatting)
   - SPF/DKIM/DMARC results (fail/softfail)

2. **Analyze the payload**
   - URLs: reputation + new domain check
   - Attachments: type (zip/iso/js/lnk), hash if available
   - Language: urgency, payment change, credential request

3. **Assess user interaction**
   - Did the user click?
   - Any sign-in events immediately after click?
   - Any new mailbox rules created?

4. **Containment (if authorized)**
   - Block sender/domain
   - Quarantine email campaign
   - Reset password + revoke sessions if user clicked or provided creds

5. **Document**
   - What you checked, what you found, and why you decided TP/FP.

## Escalate when
- user clicked or credentials submitted
- multiple recipients targeted
- suspicious forwarding rules created
- attachment delivered and opened (or likely)

## Close as FP when
- sender is validated vendor and message matches normal business patterns
- URL is confirmed safe and no user interaction / no anomalies

## Evidence checklist
Use `/docs/evidence-checklists.md`.
