from pydantic import BaseModel, ValidationError
from typing import List
import requests
import os


class PomodoroTags(BaseModel):
    id: int
    name: str
    removed: bool


class AllTags(BaseModel):
    id: int
    pomodoroTags: List[PomodoroTags]
    orderNumber: int


class GetTags(BaseModel):
    __root__: List[AllTags]


def get_tags():
    response = requests.get(os.environ['HOST'] + "/tag-groups")
    try:
        get_dict = GetTags.parse_raw(response.text)
    except ValidationError as e:
        print(e.json())
    return get_dict