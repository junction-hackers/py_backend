import s3utils
from cloudinary_api import *
from crop_utils import crop_image_bounds
import uuid
from matching import detectMatchingVictims
from face_recognition_management import create_album, add_face

from victim_api import update_victim_info
def process_event(bucket, key):
    _id = os.path.basename(key).split(".")[0]
    with s3utils.s3_download(bucket, key) as path:
        album_id = str(uuid.uuid4())
        album_key = create_album(album_id)
        initial = True
        for index, result in enumerate(detect_facial_feature(path)):
            face, age, gender = result
            add_face(album_id, album_key, bucket, album_key, index)

        detectMatchingVictims(_id)

def main(records, context):
    print(records)
    for record in records["Records"]:
        if record["eventSource"] == "aws:s3":
            s3Object = record["s3"]
            bucket = s3Object["bucket"]["name"]
            key = s3Object["object"]["key"]
            if key.startswith("raw/"):
                process_event(bucket,key)

if __name__== "__main__":
    record = {'Records': [{'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'ap-northeast-1', 'eventTime': '2019-02-16T02:06:01.561Z', 'eventName': 'ObjectCreated:Put', 'userIdentity': {'principalId': 'AWS:AIDAIX2WJXJZSZE2473VO'}, 'requestParameters': {'sourceIPAddress': '180.3.139.234'}, 'responseElements': {'x-amz-request-id': '43747DDA3644C8CE', 'x-amz-id-2': 'o9DOPie1rVtsxVRN3/+HkKBPsJXc7OyKs/O9l6E9VNI7owc4sE9wFQRzxaZytdiQF3dElRhadT4='}, 's3': {'s3SchemaVersion': '1.0', 'configurationId': 'f27b5f7c-e4bc-414e-83d3-73d675e20377', 'bucket': {'name': 'hacktoncloudapi-tokyojunctionsearchbucket-e41mee3gvpco', 'ownerIdentity': {'principalId': 'A2MJ4PT31WU8O7'}, 'arn': 'arn:aws:s3:::hacktoncloudapi-tokyojunctionvictimbucket-1dt0qaq4h9akn'}, 'object': {'key': 'raw/4.jpg', 'size': 1060, 'eTag': 'e38fd54eff55663d66d73ee82c2d5e6e', 'sequencer': '005C677009773A1139'}}}]}
    main(record, None)