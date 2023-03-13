#config:
#python3 -m venv venv //venv/bin/activate or source venv/bin/activate
#pip install boto3
#save depenndencies in requirement.txt
#pip install -r requirement.txt
#aws configure
import boto3

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)