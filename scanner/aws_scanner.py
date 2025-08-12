import boto3
from scanner.checks import check_public_access_block, check_bucket_encryption, check_bucket_policy_status
from scanner.fixers import fix_public_access_block, fix_bucket_encryption
from scanner.explain import explain_results

def run_all_checks(bucket_name, heal=False):
    s3 = boto3.client('s3')
    results = {}

    # Public Access
    results['public_access_block'] = check_public_access_block(s3, bucket_name)
    if heal and not all(results['public_access_block'].values()):
        print(f"[!] Fixing public access block for: {bucket_name}")
        fix_public_access_block(s3, bucket_name)
        results['public_access_block'] = check_public_access_block(s3, bucket_name)

    # Encryption
    results['encryption'] = check_bucket_encryption(s3, bucket_name)
    if heal and "error" in results['encryption']:
        print(f"[!] Enabling encryption for: {bucket_name}")
        fix_bucket_encryption(s3, bucket_name)
        results['encryption'] = check_bucket_encryption(s3, bucket_name)

    # Policy
    results['policy_status'] = check_bucket_policy_status(s3, bucket_name)

    return {
        "bucket_name": bucket_name,
        "results": results,
        "explanations": explain_results(results)
    }

def scan_all_buckets(heal=False):
    s3 = boto3.client('s3')
    all_results = []

    try:
        bucket_list = s3.list_buckets()["Buckets"]
    except Exception as e:
        print(f"[ERROR] Could not list buckets: {str(e)}")
        return []

    for bucket in bucket_list:
        bucket_name = bucket["Name"]
        print(f"\n--- Scanning bucket: {bucket_name} ---")
        bucket_result = run_all_checks(bucket_name, heal=heal)
        all_results.append(bucket_result)

    return all_results

