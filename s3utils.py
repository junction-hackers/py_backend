import boto3
import contextlib
import tempfile
import os

def s3():
    client = boto3.client("s3")
    resource = boto3.resource("s3")
    return client, resource

@contextlib.contextmanager
def s3_download(bucket, key):
    client, _ = s3()
    with tempfile.TemporaryDirectory() as directory:
        path = os.path.join(directory, os.path.basename(key))
        client.download_file(bucket, key, path)
        yield path



def s3_upload(bucket, key, path):
    client, _ = s3()
    client.upload_file(path, bucket, key)

def authorize_file(bucket, key):
    client, _ = s3()
    return client.generate_presigned_url(
    ClientMethod='get_object',
    Params={
        'Bucket': bucket,
        'Key': key
    }
)

