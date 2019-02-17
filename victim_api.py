import requests
import os

def update_victim_info(_id,album_id, album_key, gender, age):
    response = requests.post(os.environ["BACKEND_URL"]+f"/api/victim/{_id}/addons",
                  json = {
                            "age":age,
                            "gender":gender,
                            "album_key": album_key,
                            "album_id": album_id
                          }
        )
    return response

def get_victims():
    response =  requests.get(os.environ["BACKEND_URL"]+"/api/victims")
    if response.status_code == 200:
        return response.json()
    else:
        return []

def get_searchers():
    response =  requests.get(os.environ["BACKEND_URL"]+"/api/searchers")
    if response.status_code == 200:
        return response.json()
    else:
        return []

def set_matched(matching_indexes):
    response = requests.post(os.environ["BACKEND_URL"] + "/api/match_victim",
                             json = matching_indexes)
    if response.status_code==200:
        return response.json()