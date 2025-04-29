
>[!NOTE]
> 
> Os conteúdos deste repositório não foram concluidos ainda.

## Script Automation for S3 AWS 💡 ☁  

Functions and scripts developed based on official AWS recommendations to reduce waste, complying with FinOps best practices, in relation to files that are no longer used.


- https://docs.aws.amazon.com/cli/latest/reference/s3api/delete-bucket.html
- https://docs.aws.amazon.com/cli/latest/reference/s3api/delete-object.html
- https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

Additional documentation for S3 management best practices:
- https://docs.aws.amazon.com//AmazonS3/latest/userguide/storage-class-intro.html
- https://docs.aws.amazon.com/AmazonS3/latest/userguide/analytics-storage-class.html
- https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html
- https://calculator.aws/#/

 **Example:**
 ````
#list buckets 
aws s3 ls

#delete objects
aws s3 rm --recursive s3://namebucket

#remove bucket
aws s3 rb --force s3://namebucket
````
## Download AWS ClI ⬇️
**Choose Linux, Mac or Windows:**
  - Download: https://docs.aws.amazon.com/pt_br/cli/latest/userguide/getting-started-install.html

## Generate Create access key 🔑
  - https://docs.aws.amazon.com/keyspaces/latest/devguide/create.keypair.html
    
## Install AWS Cli 💻
  - **type:** 
```aws configure``` in cmd or gitbash

## Set with you credentials ⚙️

````
$ aws configure
AWS Access Key ID [None]: EXAMPLE
AWS Secret Access Key [None]:  EXAMPLE
Default region name [None]: example
Default output format [None]: json
````

