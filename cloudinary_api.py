import cloudinary
import cloudinary.uploader

import cloudinary.api
import os

cloudinary.config(
  cloud_name = os.environ.get("CLOUDINARY_API_NAME") or "sample",
  api_key = os.environ["CLOUDINARY_API_KEY"],
  api_secret = os.environ["CLOUDINARY_API_SECRET"]
)

def detect_facial_feature(path):
    resource = cloudinary.uploader.upload(path, detection="adv_face")
    data = resource["info"]["detection"]["adv_face"]["data"]

    for attribute in data:
        if "bounding_box" in attribute:
            yield attribute["bounding_box"], \
                  attribute["attributes"]["age"], \
                  attribute["attributes"]["gender"]

    cloudinary.api.delete_resources(resource["public_id"])
