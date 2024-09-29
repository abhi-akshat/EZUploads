import boto3
from dotenv import load_dotenv
import os
load_dotenv()

bucketName = os.getenv('BUCKET_NAME')
bucketRegion = os.getenv('BUCKET_REGION')
accessKey = os.getenv('ACCESS_KEY')
secretAccessKey = os.getenv('SECRET_ACCESS_KEY')

async def getAllFiles():
    s3_client = boto3.client('s3', region_name=bucketRegion, aws_access_key_id=accessKey, aws_secret_access_key=secretAccessKey)

    response = s3_client.list_objects_v2(Bucket=bucketName)
    files = []
    for obj in response.get('Contents', []):
        files.append(obj.get('Key'))
        
    return files
        

async def downloadFile(file_name):
    s3_client = boto3.client('s3', region_name=bucketRegion, aws_access_key_id=accessKey, aws_secret_access_key=secretAccessKey)
    object_name = file_name 

    try:
        s3_client.download_file(bucketName, object_name, file_name)
        print(f"{object_name} has been downloaded as {file_name}")
    except FileNotFoundError:
        print(f"The file {file_name} was not found locally")

    except Exception as e:
        print(f"Error downloading file: {e}")

async def uploadFile(file_name, file):
    s3_client = boto3.client('s3', region_name=bucketRegion, aws_access_key_id=accessKey, aws_secret_access_key=secretAccessKey)
    
    object_name = file_name

    try:
        s3_client.upload_file(file, bucketName, object_name)
        print(f"{file_name} has been uploaded to {bucketName}")
    except FileNotFoundError:
        print(f"The file {file_name} was not found")
    except Exception as e:
        print("An error occurred: ", e)
    
    return "Upload file"

async def deleteFile(filename):
    s3_client = boto3.client('s3', region_name=bucketRegion, aws_access_key_id=accessKey, aws_secret_access_key=secretAccessKey)
    
    try:
        s3_client.delete_object(Bucket=bucketName, Key=filename)
    except Exception as e:
        print(f"Error deleting file: {e}")