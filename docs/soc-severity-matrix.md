# SOC Severity Matrix (Tier‑1 Friendly)

Use this matrix to consistently assign severity during triage.  
Severity should reflect **impact + confidence + exposure**.

## Severity levels

### SEV 1 — Critical
**Impact:** confirmed compromise with material business impact (data loss, active ransomware, privileged account takeover).  
**Confidence:** high (multiple corroborating signals).  
**Examples:** confirmed credential compromise + MFA bypass; confirmed sensitive data exfiltration; active malware spread.

**Tier‑1 actions:** contain if authorized (disable account/isolate endpoint), escalate immediately, preserve evidence.

### SEV 2 — High
**Impact:** likely malicious activity affecting important assets/users; not yet fully confirmed.  
**Examples:** password spray with success indicators; suspicious admin role assignment; mass download of sensitive data.

**Tier‑1 actions:** collect evidence, block obvious IOCs if allowed, escalate with a clear timeline + artifacts.

### SEV 3 — Medium
**Impact:** suspicious behavior with limited exposure or unclear malicious intent.  
**Examples:** brute force without success; suspicious PowerShell on non-critical host; external sharing spike without confirmed sensitivity.

**Tier‑1 actions:** validate, enrich, tune false positives, escalate only if risk is elevated.

### SEV 4 — Low
**Impact:** likely benign or policy-related; minimal risk.  
**Examples:** single failed login from known IP; approved external share; common admin script.

**Tier‑1 actions:** document, close with rationale, recommend tuning if noisy.

## Confidence guidance
- **High:** multiple sources agree, strong IOCs, repeated pattern, or confirmed user interaction.
- **Medium:** detection triggered with partial signals; needs confirmation.
- **Low:** single weak indicator; likely false positive.

## Escalation rule of thumb
Escalate if **any** of the following are true:
- privileged account involved
- sensitive data involved
- repeated behavior + anomaly
- user clicked a malicious link
- signs of successful authentication or execution
