# SOC Detection & Investigation Library (Splunk-first)

A **SOC portfolio repository** containing a practical, Tier‑1/Associate‑friendly library of:

- **Detections** (Splunk SPL + Microsoft Sentinel KQL + Sigma)
- **Triage playbooks** (what to check, evidence to collect, escalation criteria)
- **Casebook** (end-to-end written investigations with timelines, evidence, and handoff notes)
- **SOC docs** (severity matrix, evidence checklists, MITRE coverage, workflows)
- **IOC enrichment tool** (offline-friendly template you can extend)

> ✅ No lab required • ✅ No log generation required • ✅ No attack simulations required  
> Everything is documentation + detection logic + realistic investigation write-ups.

---

## What’s inside

### 1) Detections (`/detections`)
Each detection is provided in **three formats**:
- **Splunk SPL** (primary)
- **Sentinel KQL**
- **Sigma** (portable YAML)

Each detection includes:
- **Purpose / Threat** (what it catches)
- **Data requirements** (what log fields are needed)
- **Query**
- **Triage notes** (what to validate)
- **False positives** and tuning tips
- **MITRE ATT&CK mapping**
- **Suggested severity**

### 2) Playbooks (`/playbooks`)
Tier‑1 ready playbooks for:
- Phishing
- Suspicious login
- Password spray / brute force
- MFA fatigue
- Email forwarding rules
- Suspicious PowerShell
- SharePoint/OneDrive mass download
- DLP alert investigation
- Escalation handoff + comms templates

### 3) Casebook (`/casebook`)
10 complete written cases (each case has multiple files):
- `case-summary.md`
- `timeline.md`
- `triage-notes.md`
- `evidence.md`
- `decision.md`
- `escalation.md`
- `lessons-learned.md`

These are written the way a SOC analyst documents tickets: crisp, structured, and escalation-ready.

### 4) SOC Docs (`/docs`)
- Severity matrix (how to classify incidents)
- Evidence checklists (what to collect per alert type)
- MITRE coverage table (detections → techniques)
- Triage workflow (Tier‑1 steps)

---

## Quick start (how to use this repo)

1. Pick a category from `/detections` (auth/email/endpoint/cloud/dlp).
2. Read the detection’s `.md` description (what it catches + tuning + severity).
3. Use the matching playbook in `/playbooks/tier1-triage`.
4. Review the relevant case in `/casebook` to see how a full investigation is documented.
5. Copy the SPL/KQL/Sigma detection into your notes or into a lab later if you build one.

---

## Detection coverage (high level)

- **Authentication & identity:** brute force, spray, impossible travel, MFA fatigue, new admin assignment
- **Email & M365 security:** phishing link, suspicious attachment, auto-forwarding rule, OAuth consent risk
- **Endpoint:** suspicious PowerShell (encoded), Office spawning PowerShell, suspicious LOLBins (basic)
- **Cloud & DLP/Exfil:** SharePoint/OneDrive mass download, external sharing spike, DLP rule match

See `/docs/mitre-coverage.md` for the full mapping table.

---

## Disclaimer

- These detections are **portfolio examples** and should be validated and tuned for your environment.
- All scenarios are **simulated write-ups** using realistic patterns and common SOC workflows.
- No sensitive or proprietary production data is included.

---

## Author

- ** Ram Badhiwala ** (portfolio project)
