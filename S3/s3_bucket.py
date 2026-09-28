import os
import boto3
from dotenv import load_dotenv
from botocore.exceptions import ClientError

load_dotenv()

aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_region = os.getenv("AWS_REGION")

aws_client = boto3.client(
    service_name="s3",
    region_name=aws_region,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

### Phase 1

# --- List all buckets ---
# response = aws_client.list_buckets()
# number_of_buckets = len(response['Buckets'])

# if number_of_buckets > 0:
#     print(f"List of buckets found: {number_of_buckets}")
#     for bucket in response['Buckets']:
#         print(f" - {bucket['Name']}")
# else:
#     print("No buckets found")

# --- Create buckets ---
# buckets_to_create = ["dush-new-bucket-123456", "goyal-new-bucket-123456"]

# def create_bucket(bucket_name):
#     kwargs = {'Bucket': bucket_name}

#     # ONLY add LocationConstraint if the region is NOT us-east-1
#     if aws_region and aws_region != "us-east-1":
#         kwargs['CreateBucketConfiguration'] = {
#             'LocationConstraint': aws_region
#         }

#     try:
#         response = aws_client.create_bucket(**kwargs)
#         print(f"Bucket '{bucket_name}' created successfully")
#         return response
#     except ClientError as e:
#         error_code = e.response["Error"]["Code"]
#         if error_code == "BucketAlreadyOwnedByYou":
#             print(f"Bucket '{bucket_name}' already owned by you")
#         elif error_code == "BucketAlreadyExists":
#             print(f"Bucket '{bucket_name}' already exists globally")
#         else:
#             print(f"Error creating '{bucket_name}': {e.response['Error']['Message']}")

# for bucket in buckets_to_create:
#     create_bucket(bucket)

# --- Delete bucket ---

try:
    bucket_to_delete = "goyal-new-bucket-123456"
    aws_client.delete_bucket(Bucket=bucket_to_delete)
    print(f"Bucket {bucket_to_delete} deleted successfully")
except ClientError as e:
    print(f"Error deleting bucket {bucket_to_delete}: {e.response['Error']['Message']}")

# --- Delete multiple buckets ---
# buckets_to_delete = ["dush-new-bucket-123456", "goyal-new-bucket-123456"]

# for bucket in buckets_to_delete:
#     try:
#         aws_client.delete_bucket(Bucket=bucket)
#         print(f"Bucket '{bucket}' deleted successfully")
#     except ClientError as e:
#         error_code = e.response["Error"]["Code"]
#         if error_code == "NoSuchBucket":
#             print(f"Bucket '{bucket}' does not exist")
#         else:
#             print(f"Error deleting '{bucket}': {e.response['Error']['Message']}")

# --- Head bucket ---
# try:
#     bucket_to_head = "goyal-new-bucket-123456"
#     response = aws_client.head_bucket(Bucket=bucket_to_head)
#     print(f"Bucket {bucket_to_head} exists")
# except ClientError as e:
#     print(f"Error heading bucket {bucket_to_head}: {e.response['Error']['Message']}")

### Phase 2

# --- Upload Objects ---

# --- Upload Objects using Client ---
# local_file_path = r"C:\Users\Meenakshi\Downloads\hcl\hcl\Dushyant'sResume.pdf"
# bucket_name = "goyal-new-bucket-123456"
# file_name = os.path.basename(local_file_path)
# s3_key = f"resume/{file_name}"

# try:
#     aws_client.upload_file(
#         Filename=local_file_path,
#         Bucket=bucket_name,
#         Key=s3_key,
#         ExtraArgs={"ContentType": "application/pdf"}
#     )
#     print(f"Successfully uploaded '{file_name}' to 's3://{bucket_name}/{s3_key}'")
# except ClientError as e:
#     print(f"Error uploading file: {e}")
# except FileNotFoundError:
#     print(f"Error: The file '{local_file_path}' was not found.")

# --- Upload Objects using Resource ---
# try:
#     upload_file_response = aws_resource.meta.client.upload_file(
#         Filename="sample_file.txt",
#         Bucket="your-unique-bucket-name",
#         Key="sample_file_uploaded_by_resource.txt"
#     )
#     print(f"Successfully uploaded file to S3 using Resource")
# except ClientError as e:
#     print(f"Error uploading file: {e}")
# except FileNotFoundError:
#     print(f"Error: The file 'sample_file.txt' was not found in the current directory.")