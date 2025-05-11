# DevSecOps Lab

This repository is a comprehensive showcase of real-world DevSecOps expertise, simulating a modern security-focused SDLC. It includes implementations and examples across GitHub Advanced Security, penetration testing workflows, cryptographic techniques, cloud security hardening, and SIEM-style log correlation.

## 🔐 Core Features

- **GitHub Advanced Security integration** with secret scanning and code scanning
- **CI/CD security automation** using GitHub Actions
- **Sample vulnerable app** for penetration testing and analysis
- **Real cryptography examples** using AES, 3DES, Diffie-Hellman, and RSA
- **Cloud misconfiguration detection** with Terraform and static analysis tools
- **Simulated SIEM analysis** with mock logs and detection rules

## 🗂️ Project Structure

```bash
expert-devsecops-lab/
├── .github/
│   └── workflows/
│       └── security-pipeline.yml        # GitHub Actions security automation
├── src/
│   └── vulnerable-app/
│       └── app.py                       # Deliberately vulnerable Flask app
├── crypto/
│   └── secure_comms.py                 # Cryptographic utilities
├── pentest/
│   ├── recon_nmap.sh                   # Automated reconnaissance script
│   └── burp_scan_report.md            # Sample report findings
├── cloud/
│   ├── aws_baseline.tf                # Misconfigured and hardened Terraform example
│   └── gcp_command_center_sim.md      # Simulated GCP SCC workflow
├── siem/
│   └── splunk_logs.json               # Simulated events for correlation
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## 🚀 Getting Started

### Requirements
- Docker & Docker Compose
- Python 3.11+

### Run the vulnerable app
```bash
docker-compose up --build
```

### Run cryptographic example
```bash
python3 crypto/secure_comms.py
```

### Run Nmap scan
```bash
chmod +x pentest/recon_nmap.sh
./pentest/recon_nmap.sh
```

## 🔍 CI/CD with GitHub Actions

The security pipeline includes:
- Secret scanning with `gitleaks`
- Static analysis with `semgrep`
- Dependency vulnerability check with `npm audit` or `pip-audit`

## 💣 Penetration Testing
- Simulates end-to-end phases: Recon → Scan → Exploit
- Integrates with Burp Suite and Nmap (manual or CLI-driven)
- Includes vulnerable endpoints (e.g., XSS, insecure crypto)

## 🧮 Cryptography
Demonstrates encryption/decryption flows:
- AES (CBC/CTR)
- 3DES
- RSA for key exchange
- Diffie-Hellman shared secrets

## ☁️ Cloud Security
- Terraform misconfig (e.g., public S3 bucket, open security groups)
- `tfsec` and `kics` analysis
- GCP Security Command Center event simulation

## 📊 SIEM Logs Simulation
- Sample logs in JSON with injected anomalies
- Could be ingested by Splunk/QRadar
- Python script to correlate and flag suspicious activity

**Author:** Mariano Dorado  
**Contact:** [LinkedIn](https://linkedin.com/in/nanodorado)