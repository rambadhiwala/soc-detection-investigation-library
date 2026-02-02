# MITRE ATT&CK Coverage

This table maps detections in this repository to MITRE ATT&CK techniques.

| ID | Detection | ATT&CK Technique | Technique ID |
|----|-----------|------------------|--------------|
| AUTH-01 | Brute Force Burst | Brute Force | T1110 |
| AUTH-02 | Password Spray | Brute Force | T1110 |
| AUTH-03 | Impossible Travel | Valid Accounts | T1078 |
| AUTH-04 | MFA Fatigue Pattern | Valid Accounts | T1078 |
| AUTH-05 | New Admin Role Assignment | Account Manipulation | T1098 |
| EMAIL-01 | Suspicious External Email + Link | Phishing | T1566 |
| EMAIL-02 | Suspicious Attachment Delivery | Phishing | T1566 |
| EMAIL-03 | Mailbox Forwarding Rule Created | Email Collection/Exfil | T1114 / T1020 (context) |
| EMAIL-04 | Suspicious OAuth Consent | Account Manipulation | T1098 |
| ENDPT-01 | PowerShell Encoded Command | Command and Scripting Interpreter | T1059.001 |
| ENDPT-02 | Office Spawns PowerShell | Command and Scripting Interpreter | T1059.001 |
| ENDPT-03 | Suspicious LOLBin Use (rundll32/regsvr32) | Signed Binary Proxy Execution | T1218 |
| CLOUD-01 | SharePoint/OneDrive Mass Download | Exfiltration Over Web Service | T1567 |
| CLOUD-02 | External Sharing Spike | Exfiltration Over Web Service | T1567 |
| DLP-01 | Sensitive Data Sent Externally (Email) | Exfiltration | T1041 (context) |
| DLP-02 | Sensitive Files to Removable Media | Exfiltration Over Physical Media | T1052 |
| DLP-03 | Sensitive Files Uploaded to Web | Exfiltration Over Web Service | T1567 |
