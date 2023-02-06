import requests
import json
import os


def post_tags(key):
    j = json.dumps({
        "numbersToSaveAutomatically": 1,
        "tagGroupId": key
    })
    headers = {'Content-Type': 'application/json'}
    p = requests.request("POST", os.environ['HOST'] + '/pomodoro/auto', headers=headers, data=j)
    status_post = p.status_code
    return status_post
