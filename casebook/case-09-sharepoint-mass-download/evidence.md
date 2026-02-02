# Evidence Collected

## Entities
- **Primary user:** <user@company.com>
- **Source IP:** <x.x.x.x> (placeholder)
- **Host/device:** <HOSTNAME> (placeholder)
- **App:** <M365 / Endpoint / Cloud> (depending on case)

## Key observations
- The alert pattern matches the intended detection scenario.
- Baseline deviations noted (new geo/device, abnormal volume, unusual parent process, etc.).

## Example queries used
### Splunk (example)
- Search recent events for the user/entity
- Correlate with follow-on actions

### Sentinel (example)
- Filter to the same entity and time window
- Confirm supporting indicators

> Replace placeholders with real values if you later run this in a lab or on training data.
