import json
from typing import Any
import boto3

def json_file(file_name, data: Any):
    data_str = json.dumps(data)
    binary_file(file_name, data_str)

def binary_file(file_name, data: str | bytes):
    s3 = boto3.client("s3")
    bucket_name = "resume.leonklute.nl"
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=data)
    print(f"saved file: {file_name} to {bucket_name}")