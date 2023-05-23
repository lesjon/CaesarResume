import os
import boto3

def save_file(file_name, data):
    print(f'{file_name=},{data=}')
    s3 = boto3.client('s3')
    print(f'{s3=}')
    bucket_name = "resume.leonklute.nl"

    result = s3.put_object(Bucket=bucket_name, Key=file_name, Body=data)
    print(f'{result=}')