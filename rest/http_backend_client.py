import json
import os

import requests

from util.constants import URL_BASE

base_url = os.environ['HOST'] + URL_BASE


def get(url: str):
    return requests.get(base_url + url)


def post(url: str, body: str):
    headers = {'Content-Type': 'application/json'}
    return requests.request("POST", base_url + url, headers=headers, data=body)
