import requests
import os
import s3utils
def create_album(album_id):
    response = requests.post("https://lambda-face-recognition.p.rapidapi.com/album",
                            headers={
                                "X-RapidAPI-Key":  os.environ["RAPID_API_KEY"],
                            },
                            params={
                                "album": album_id
                            }
                            )
    return response.json()["albumkey"]

def add_face(album_id, album_key, bucket, key, index):
    url = s3utils.authorize_file(bucket, key)
    response = requests.post("https://lambda-face-recognition.p.rapidapi.com/album_train",
                             headers={
                                 "X-RapidAPI-Key": os.environ["RAPID_API_KEY"],
                             },
                             params={
                                 "album": album_id,
                                 "albumkey": album_key,
                                 "entryid": f"{index}",
                                 "urls": [url,url,url,url]
                             }
        )
    return response