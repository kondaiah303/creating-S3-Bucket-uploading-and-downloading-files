import boto3

client = boto3.client('s3')


def creating_bucket():
    """Creating the Buckets in AWS S3"""

    client.create_bucket(
        ACL='private',
        Bucket='newbucket3034',
        CreateBucketConfiguration={
            'LocationConstraint': 'ap-south-1'
        }
    )


def uploading_files_bucket():
    """Uploading the files in particular Bucket in AWS S3"""

    client.upload_file('Hi.txt', 'newbucket3034', 'Hi_Object.txt')      # .upload_file('file_name', 'Bucket_name', 'Object_name')


def downloading_files_bucket():
    """Downloading the files from the particular Bucket in AWS S3"""

    client.download_file('newbucket3034', 'Hi_Object.txt', 'Hi.txt')        # .Download_file('Bucket_name', 'Object_name', 'File_name')


def main():
    creating_bucket()
    uploading_files_bucket()
    downloading_files_bucket()


if __name__ == '__main__':
    main()
    