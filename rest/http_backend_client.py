import json
import os

import requests

from util.constants import URL_BASE

base_url = os.environ['HOST'] + URL_BASE


def get(url: str):
    return requests.get(base_url + url)


def post(url: str, body: object):
    json_body = json.dumps(body, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    headers = {'Content-Type': 'application/json'}
    return requests.request("POST", base_url + url, headers=headers, data=json_body)
