import json
import os
import requests


def get(url: str):
    return requests.get(os.environ['HOST'] + url)


def post(url: str, body: object):
    body = json.dumps(body)
    headers = {'Content-Type': 'application/json'}
    return requests.request("POST", os.environ['HOST'] + url, headers=headers, data=body)
