from botocore.exceptions import ClientError

def fix_public_access_block(s3, bucket_name):
    print(f"[!] Fixing public access block for: {bucket_name}")
    try:
        s3.put_public_access_block(
            Bucket=bucket_name,
            PublicAccessBlockConfiguration={
                'BlockPublicAcls': True,
                'IgnorePublicAcls': True,
                'BlockPublicPolicy': True,
                'RestrictPublicBuckets': True
            }
        )
    except ClientError as e:
        print(f"[ERROR] Failed to fix public access block: {str(e)}")

def fix_bucket_encryption(s3, bucket_name):
    print(f"[!] Fixing encryption for: {bucket_name}")
    try:
        s3.put_bucket_encryption(
            Bucket=bucket_name,
            ServerSideEncryptionConfiguration={
                'Rules': [{
                    'ApplyServerSideEncryptionByDefault': {
                        'SSEAlgorithm': 'AES256'
                    },
                    'BucketKeyEnabled': True
                }]
            }
        )
    except ClientError as e:
        print(f"[ERROR] Failed to enable encryption: {str(e)}")

