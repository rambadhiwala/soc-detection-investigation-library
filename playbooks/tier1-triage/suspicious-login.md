# Playbook: Suspicious Login / Identity Alert (Tier‑1)

## Goal
Determine whether authentication activity suggests credential compromise.

## Steps
1. Confirm alert type (brute force, spray, impossible travel, new device)
2. Check account type (admin/service/user) and criticality
3. Validate source IP reputation + geo baseline
4. Look for success indicators (successful login after failures)
5. Check MFA behavior (repeated prompts, bypass, disabled)
6. Check follow-on activity (new rules, downloads, admin changes)

## Containment (if authorized)
- force password reset
- revoke sessions / sign out everywhere
- block IP (if allowed)

## Escalate when
- privileged account
- success indicators present
- suspicious geo + new device + unusual activity
