This example intentionally includes a publicly readable S3 bucket and an overly permissive security group, which can be detected by tools like `tfsec`, `kics`, or AWS Config.

### cloud/gcp_command_center_sim.md
```
# Simulated GCP Security Command Center (SCC) Workflow

This document demonstrates how GCP SCC might detect and surface security findings in a real-world environment.

## Scenario: Publicly Accessible Cloud Storage Bucket

### 1. Misconfiguration Introduced
A developer creates a GCS bucket with public access:

```bash
gsutil mb -p my-project gs://open-dev-bucket/
gsutil iam ch allUsers:objectViewer gs://open-dev-bucket
```

### 2. SCC Alert Triggered
GCP SCC scans the environment and flags the bucket:
```
FINDING: STORAGE_BUCKET_PUBLICLY_ACCESSIBLE
Severity: HIGH
Category: Misconfiguration
Resource: //storage.googleapis.com/open-dev-bucket
```

### 3. Suggested Remediation
- Revoke public access:
  ```bash
  gsutil iam ch -d allUsers gs://open-dev-bucket
  ```
- Apply IAM conditions restricting access
- Enable VPC-SC for sensitive workloads

### 4. Detection Tools
This finding can also be detected using:
- `gcloud scc findings list`
- Security Health Analytics in the SCC UI
- Custom rules with Event Threat Detection or Forseti
```

## 📊 SIEM Logs Simulation
- Sample logs in JSON with injected anomalies
- Could be ingested by Splunk/QRadar
- Python script to correlate and flag suspicious activity