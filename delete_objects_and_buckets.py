#install aws cli
#configure aws cli with access credentials
#run pip install boto3 in cmd
#run the code below
#replace the name of bucket
import boto3
try:
    session = boto3.Session() 
    s3 = session.resource(service_name='s3') 
    #example: s3://bucket_old_data
    bucket = s3.Bucket('bucket_old_data')  
    bucket.object_versions.delete()
    bucket.delete()
except:
    print("erro")
  
#another example
try:
    session = boto3.Session() 
    s3 = session.resource(service_name='s3') 
    #example: s3://bucket_old_services
    bucket = s3.Bucket('bucket_old_services')  
    bucket.object_versions.delete()
    bucket.delete()
 except Exception as e:
     print e.message
