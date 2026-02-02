"""
IOC Enrichment Tool (Portfolio Template)

This script is intentionally lightweight and safe for a portfolio:
- It reads IOCs from a text file (one per line)
- It outputs a JSON structure you can extend later
- It does NOT call external APIs by default (no keys required)

To extend:
- Add VirusTotal / AbuseIPDB / URLhaus lookups
- Add caching and rate limiting
- Add output fields for verdicts and links
"""

import json
import re
from pathlib import Path
from typing import Dict, List

IP_RE = re.compile(r"^(?:\d{1,3}\.){3}\d{1,3}$")
DOMAIN_RE = re.compile(r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.(?:[A-Za-z]{2,63})$")
HASH_RE = re.compile(r"^[A-Fa-f0-9]{32}$|^[A-Fa-f0-9]{40}$|^[A-Fa-f0-9]{64}$")

def classify_ioc(ioc: str) -> str:
    ioc = ioc.strip()
    if IP_RE.match(ioc):
        return "ip"
    if HASH_RE.match(ioc):
        return "hash"
    if DOMAIN_RE.match(ioc):
        return "domain"
    if ioc.startswith("http://") or ioc.startswith("https://"):
        return "url"
    return "unknown"

def enrich_iocs(iocs: List[str]) -> Dict:
    results = []
    for ioc in iocs:
        kind = classify_ioc(ioc)
        results.append({
            "ioc": ioc,
            "type": kind,
            "verdict": "unknown",
            "notes": "Add external enrichment here (optional)."
        })
    return {"generated_by": "ioc-enrichment.py", "count": len(results), "results": results}

def main():
    input_path = Path("sample-input.txt")
    out_path = Path("sample-output.json")

    if not input_path.exists():
        raise SystemExit("sample-input.txt not found. Create it with one IOC per line.")

    iocs = [line.strip() for line in input_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    output = enrich_iocs(iocs)
    out_path.write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"Wrote {out_path} with {len(iocs)} IOCs.")

if __name__ == "__main__":
    main()
