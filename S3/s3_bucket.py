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

### 🚩🚩🚩 Phase 1

# --- List all buckets ---
response = aws_client.list_buckets()
number_of_buckets = len(response['Buckets'])

if number_of_buckets > 0:
    print(f"List of buckets found: {number_of_buckets}")
    for bucket in response['Buckets']:
        print(f" - {bucket['Name']}")
else:
    print("No buckets found")

# --- Create buckets ---
# buckets_to_create = ["dush-new-bucket-123456", "goyal-new-bucket-123456"]
# buckets_to_create = ["goyal-new-bucket-123457"]

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

# try:
#     bucket_to_delete = "goyal-new-bucket-123457"
#     aws_client.delete_bucket(Bucket=bucket_to_delete)
#     print(f"Bucket {bucket_to_delete} deleted successfully")
# except ClientError as e:
#     print(f"Error deleting bucket {bucket_to_delete}: {e.response['Error']['Message']}")

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

### 🚩🚩🚩Phase 2

# --- Upload Objects ---

# --- Upload Objects using Client ---
local_file_path = r"C:\Users\Meenakshi\Downloads\hcl\hcl\Dushyant'sResume.pdf"
bucket_name = "goyal-new-bucket-123457"
file_name = os.path.basename(local_file_path)
s3_key = f"resume/{file_name}"

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
#     upload_file_response = aws_client.upload_file(
#         Filename=local_file_path,
#         Bucket=bucket_name,
#         Key=s3_key
#     )
#     print(f"Successfully uploaded file to S3 using Resource")
# except ClientError as e:
#     print(f"Error uploading file: {e}")
# except FileNotFoundError:
#     print(f"Error: The file 'sample_file.txt' was not found in the current directory.")

# --- Upload Objects using Client with ExtraArgs ---
# ExtraArgs is used to pass optional arguments for the upload operation.
# try:
#     aws_client.upload_file(
#         Filename=local_file_path,
#         Bucket=bucket_name,
#         Key=s3_key,
#         ExtraArgs={"ContentType": "application/pdf"}
#     )
#     print(f"Successfully uploaded '{file_name}' to 's3://{bucket_name}/{s3_key}' with ContentType")
# except ClientError as e:
#     print(f"Error uploading file: {e}")
# except FileNotFoundError:
#     print(f"Error: The file '{local_file_path}' was not found.")

# --- List objects in a bucket & Pagination ---
# try:
#     response = aws_client.list_objects_v2(Bucket=bucket_name)

#     # Check if bucket has objects inside
#     if 'Contents' in response and len(response['Contents']) > 0:
#         print(f"Bucket '{bucket_name}' contains following objects:")
#         for obj in response['Contents']:
#             print(f" - {obj['Key']}")

#         # --- Pagination (runs only if bucket has objects) ---
#         paginator = aws_client.get_paginator('list_objects_v2')
#         pages = paginator.paginate(Bucket=bucket_name)

#         print(f"\nListing objects with pagination in bucket '{bucket_name}':")
#         object_count = 0
#         for page in pages:
#             if 'Contents' in page:
#                 for obj in page['Contents']:
#                     print(f" - {obj['Key']}")
#                     object_count += 1

#         print(f"Total objects found: {object_count}")
#     else:
#         print(f"Bucket '{bucket_name}' exists but is empty.")

# except ClientError as e:
#     error_code = e.response["Error"]["Code"]
#     if error_code == "NoSuchBucket":
#         print(f"Bucket '{bucket_name}' does not exist.")
#     else:
#         print(f"Error accessing bucket '{bucket_name}': {e.response['Error']['Message']}")

# --- Delete Objects ---

# Delete a single object
# try:
#     aws_client.delete_object(Bucket=bucket_name, Key=s3_key)
#     print(f"Successfully deleted '{s3_key}' from bucket '{bucket_name}'")
# except ClientError as e:
#     print(f"Error deleting object: {e}")

# --- Batch Delete Objects ---
# try:
#     aws_client.delete_objects(
#         Bucket=bucket_name,
#         Delete={
#             'Objects': [
#                 {'Key': s3_key},
#                 {'Key': 'resume/Dushyant\'sResume.pdf'}
#             ]
#         }
#     )
#     print(f"Successfully deleted objects from bucket '{bucket_name}'")
# except ClientError as e:
#     print(f"Error deleting objects: {e}")

# --- Read Object Content ---
# try:
#     response = aws_client.get_object(
#         Bucket=bucket_name,
#         Key=s3_key
#     )
    
#     # Read and decode the content
#     file_content = response['Body'].read()
    
#     print(f"Successfully read content from '{s3_key}':")
#     print(file_content)
    
# except ClientError as e:
#     print(f"Error reading object: {e}")
# except FileNotFoundError:
#     print(f"Error: The file '{local_file_path}' was not found.")

# --- Download and Read Objects ---
# try:
#     aws_client.download_file(
#         Bucket=bucket_name,
#         Key=s3_key,
#         Filename=os.path.join(".", "downloaded_file.pdf")
#     )
#     print(f"Successfully downloaded '{s3_key}' from bucket '{bucket_name}'")
# except ClientError as e:
#     print(f"Error downloading file: {e}")

### 🚩🚩🚩Phase 3

# --- Copy Objects ---
# try:
#     aws_client.copy_object(
#         Bucket=bucket_name,
#         CopySource={'Bucket': bucket_name, 'Key': s3_key},
#         Key=f"copy_of_{s3_key}"
#     )
#     print(f"Successfully copied '{s3_key}' to 's3://{bucket_name}/copy_of_{s3_key}'")
# except ClientError as e:
#     print(f"Error copying object: {e}")

# --- Move Objects ---
# try:
#     aws_client.copy_object(
#         Bucket=bucket_name,
#         CopySource={'Bucket': bucket_name, 'Key': s3_key},
#         Key=f"moved_{s3_key}"
#     )
#     print(f"Successfully copied '{s3_key}' to 's3://{bucket_name}/moved_{s3_key}'")
#     aws_client.delete_object(Bucket=bucket_name, Key=s3_key)
#     print(f"Successfully deleted '{s3_key}' from bucket '{bucket_name}'")
# except ClientError as e:
#     print(f"Error moving object: {e}")

# --- Rename Objects ---
# try:
#     aws_client.copy_object(
#         Bucket=bucket_name,
#         CopySource={'Bucket': bucket_name, 'Key': s3_key},
#         Key=f"rename_{s3_key}"
#     )
#     print(f"Successfully copied '{s3_key}' to 's3://{bucket_name}/rename_{s3_key}'")
#     aws_client.delete_object(Bucket=bucket_name, Key=s3_key)
#     print(f"Successfully deleted '{s3_key}' from bucket '{bucket_name}'")
# except ClientError as e:
#     print(f"Error renaming object: {e}")

