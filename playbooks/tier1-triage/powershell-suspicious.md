# Playbook: Suspicious PowerShell Alert (Tier‑1)

## Goal
Validate whether PowerShell activity indicates malicious execution.

## Steps
1. Review command line:
   - EncodedCommand, IEX, DownloadString, hidden window
2. Confirm parent process:
   - Office spawning PowerShell is higher risk
3. Check process tree and any child processes
4. Check network connections from the process
5. Check if the host shows repeated events or persistence indicators

## Escalate when
- encoded command + external network activity
- Office or browser spawns PowerShell
- repeat events across hosts
