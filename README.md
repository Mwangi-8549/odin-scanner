Odin S3 Security Scanner
AWS S3 security scanner with optional self-healing for public access, encryption, and policy issues.

A simple AWS S3 security scanner that checks:
- Public Access Block settings
- Encryption configuration
- Bucket policy presence

Optionally, it can auto-fix issues with `--heal`.

## Installation
```bash
git clone https://github.com/YOURUSERNAME/odin-scanner.git
cd odin-scanner
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
11aad28 (v1.0 - AWS S3 Scanner with --heal option)
