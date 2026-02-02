# Detection Tuning Notes

## Principles
- Prefer baseline/behavior signals over single indicators
- Tune thresholds per user group (admins vs users)
- Add allow-lists only for **verified** safe sources
- Track every tuning change with reason + expected effect

## Example tunings
- AUTH-01: exclude known VPN IP ranges; set higher threshold for business hours
- CLOUD-01: exclude migration service accounts; add sensitivity label requirement
