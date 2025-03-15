import boto3

s3 = boto3.client('s3')
session = boto3.Session() 
s3 = session.resource(service_name='s3') 

trn = "list.txt"

with open(trn) as trn_list:
    for line in trn_list:
        bucket = s3.Bucket(line)
        print(bucket)
        input('digite algo para continuar')
        bucket.object_versions.delete()
        bucket.delete()
