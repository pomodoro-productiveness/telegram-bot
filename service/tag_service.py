from model import get_pomodoro_response, get_tags_response
from rest import http_backend_client
import datetime


def get_tag_groups():
    response = http_backend_client.get("/tag-groups")
    return get_tags_response.GetTagsResponse.parse_raw(response.text)


def show_tags_with_today():
    response = http_backend_client.get(f'/pomodoro?start={datetime.datetime.today().strftime("%Y-%m-%d")}&'
                                       f'end={datetime.datetime.today().strftime("%Y-%m-%d")}')
    return get_pomodoro_response.GetTagsResponse.parse_raw(response.text)
