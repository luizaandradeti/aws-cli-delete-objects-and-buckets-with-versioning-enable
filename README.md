

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

##  AWS config

![App Screenshot](AWS.png) 

````
$ aws configure
AWS Access Key ID [None]: EXMAPLE
AWS Secret Access Key [None]:  EXAMPLE
Default region name [None]: us-west-2
Default output format [None]: json
````

https://docs.aws.amazon.com/cli/latest/reference/configure/

````js
const AWS = require('aws-sdk');
const fs = require('fs');

const s3 = new AWS.S3();
const session = new AWS.Session();
const trn = "list.txt";

fs.readFile(trn, 'utf8', (err, data) => {
    if (err) throw err;
    const lines = data.split('\n');
    lines.forEach(line => {
        const bucketName = line.trim();
        const bucket = s3.bucket(bucketName);
        console.log(bucket);
        prompt('digite algo para continuar');
        s3.listObjectVersions({ Bucket: bucketName }, (err, data) => {
            if (err) throw err;
            const versions = data.Versions;
            versions.forEach(version => {
                s3.deleteObject({ Bucket: bucketName, Key: version.Key, VersionId: version.VersionId }, (err) => {
                    if (err) throw err;
                });
            });
            s3.deleteBucket({ Bucket: bucketName }, (err) => {
                if (err) throw err;
            });
        });
    });
});
````


> [!NOTE]
>
> Repository for personal and professional study purposes
> This material is study personal and does not replace official documentation, always follow the official documentation.
