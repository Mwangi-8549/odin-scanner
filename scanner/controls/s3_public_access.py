import boto3

def check_s3_public_buckets():
    s3 = boto3.client('s3')
    findings = []

    for bucket in s3.list_buckets()["Buckets"]:
        bucket_name = bucket["Name"]
        acl = s3.get_bucket_acl(Bucket=bucket_name)
        for grant in acl["Grants"]:
            if grant["Grantee"].get("URI") == "http://acs.amazonaws.com/groups/global/AllUsers":
                findings.append({
                    "bucket": bucket_name,
                    "issue": "Bucket is publicly accessible",
                    "severity": "High",
                    "control": "CIS 2.1.1"
                })
    return findings

