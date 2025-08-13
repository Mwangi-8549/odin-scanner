# Odin S3 Security Scanner

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Version](https://img.shields.io/badge/version-1.0-orange)


Odin S3 Security Scanner is a lightweight AWS S3 security auditing tool with an optional self-healing feature for fixing misconfigurations related to public access, encryption, and bucket policies.

It helps ensure your S3 buckets follow AWS security best practices by checking:

- Public Access Block settings
- Encryption configuration
- Bucket policy presence

Optionally, it can auto-remediate issues using the `--heal` flag.

## Features
🚨 Detects insecure public access settings  
🔒 Verifies encryption-at-rest configurations  
📜 Checks for bucket policy presence  
🛠 Optional self-healing with `--heal`  

## Installation
```bash
git clone https://github.com/Mwangi-8549/odin-scanner.git
cd odin-scanner

# Set up a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage
```bash
# Scan all buckets without making changes
python odin_scanner.py

# Scan and automatically fix issues
python odin_scanner.py --heal
```

Requirements
- Python 3.8+
- AWS credentials configured (via AWS CLI or environment variables)
```bash
aws configure
```
Version
v1.0 — Initial release with AWS S3 scanning and --heal option.

