import boto3
from botocore.exceptions import ClientError

def check_bucket_policy_status(s3, bucket_name):
    try:
        response = s3.get_bucket_policy_status(Bucket=bucket_name)
        return response.get("PolicyStatus", {})
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchBucketPolicy':
            return {"error": "No policy attached to bucket."}
        return {"error": str(e)}

def check_bucket_encryption(s3, bucket_name):
    try:
        response = s3.get_bucket_encryption(Bucket=bucket_name)
        return response.get("ServerSideEncryptionConfiguration", {})
    except ClientError as e:
        if e.response['Error']['Code'] == 'ServerSideEncryptionConfigurationNotFoundError':
            return {"error": "No encryption configured"}
        return {"error": str(e)}

def check_public_access_block(s3, bucket_name):
    try:
        response = s3.get_public_access_block(Bucket=bucket_name)
        return response.get('PublicAccessBlockConfiguration', {})
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchPublicAccessBlockConfiguration':
            return {"error": "No public access block configuration found."}
        return {"error": str(e)}

