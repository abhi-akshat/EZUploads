import boto3
from dotenv import load_dotenv
import os
load_dotenv()

bucketName = os.getenv('BUCKET_NAME')
bucketRegion = os.getenv('BUCKET_REGION')
accessKey = os.getenv('ACCESS_KEY')
secretAccessKey = os.getenv('SECRET_ACCESS_KEY')

client = boto3.client('s3', region_name=bucketRegion, aws_access_key_id=accessKey, aws_secret_access_key=secretAccessKey)

async def getAllFiles():
    return "All files"

async def downloadFile():
    return "Download file"

async def uploadFile():
    return "Upload file"