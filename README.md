# Renovate CVE-2023-36464 fixture

This small project pins `pypdf==3.8.1`, an affected release, and calls
`PdfReader`'s text extraction path. The CVE can cause an infinite loop while
parsing a specially crafted PDF; this fixture does not include or run an
exploit PDF.

## Try it

```sh
python -m pip install -r requirements.txt
python main.py path/to/ordinary.pdf
```

Commit and push this project to GitHub with Renovate enabled. Renovate can
detect the pin in `requirements.txt` and offer a `pypdf` upgrade. To test a
security-specific Renovate PR from GitHub alerts, also enable the repository's
Dependency graph and Dependabot alerts, and grant the Renovate GitHub App
permission to read Dependabot alerts. The `vulnerabilityAlerts` setting asks
Renovate to prefer the highest available version for that fix.

The advisory also lists the legacy `PyPDF2` distribution as affected through
`3.0.1`, but lists no patched `PyPDF2` version; it recommends migrating to
`pypdf>=3.9.0`. Pinning `PyPDF2` itself therefore cannot produce a normal
same-package Renovate update to `pypdf`. This fixture pins the successor package
at a vulnerable version so Renovate has an existing `pypdf` dependency to
upgrade.
