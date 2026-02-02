# Playbook: SharePoint/OneDrive Mass Download (Tier‑1)

## Goal
Determine whether high-volume file downloads are legitimate or exfiltration risk.

## Steps
1. Validate volume + time window
2. Identify file sensitivity (labels, folder names, owners)
3. Check whether user recently changed password/MFA or had suspicious logins
4. Look for external sharing actions around the same time
5. Confirm business justification (migration, backups) if known

## Escalate when
- sensitive data + unusual login signals
- downloads followed by external shares
- privileged account involved
