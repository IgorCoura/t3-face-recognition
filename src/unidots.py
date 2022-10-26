import time
import requests
import math
import random

TOKEN = "BBFF-WBcT054T2Jx5ebXAsGX4YohPRY4L3K"  # Put your TOKEN here
DEVICE_LABEL = "machine"  # Put your device label here 



def build_payload(name, img):
    payload = {"test": {"value":1, "context" : {"name":name, "img": "data:image/png;base64,"+img}}}
    return payload


def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)

    # Processes results
    print(req.status_code, req.json())
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True


def send_image(name, img):
    payload = build_payload(name, img)
    print("[INFO] Attemping to send data")
    post_request(payload)
    print("[INFO] finished")

