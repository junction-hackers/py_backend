import requests
import os

def detect_faces(image_url):
    response = requests.post("https://MicrosoftFaceApidimasV1.p.rapidapi.com/detectFaces",
                                headers={
                                "X-RapidAPI-Key":  os.environ["RAPID_API_KEY"]
                                },
                                json={"image": image_url,
                                      "region": os.environ["MICROSOFT_REGION"],
                                      "subscriptionKey": os.environ["MICROSOFT_API_KEY"],
                                      "status_msg": ""}
                            )
    return response