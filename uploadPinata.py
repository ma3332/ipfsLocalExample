from pathlib import Path
import requests
import json
import os


def upload_to_pinata(filepath):
    # https://docs.pinata.cloud/pinata-api/pinning/pin-file-or-directory
    PINATA_BASE_URL = "https://api.pinata.cloud/"
    endpoint = "pinning/pinFileToIPFS"
    headers = {
        "pinata_api_key": "", # pinata api key
        "pinata_secret_api_key": "", # pinata secreate api key
    }
    filename = filepath.split("/")[-1:][0]
    # read file as binary (rb)
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        response = requests.post(
            PINATA_BASE_URL + endpoint,
            files={"file": (filename, image_binary)},
            headers=headers,
        )
    print(response.json())


def main_for_upload_PINATA():
    # loop through all tokens and figure out the metadata for each of them
    list_file = os.listdir("./img")
    image_name = [x.split(".")[0] for x in list_file]
    metadata_file_name_path = (
        f"./metadata/{image_name}.json"
    )
    upload_to_pinata(metadata_file_name_path)  # upload metadata to Pinata
    image_path = "./img/" + ".jpg"
    image_uri = upload_to_pinata(image_path)  # upload image to Pinata
