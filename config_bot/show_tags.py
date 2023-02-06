from pydantic import BaseModel, ValidationError
import datetime
import requests
import os
from typing import List


class Tags(BaseModel):
    name: str
    removed: bool


class PomodoroToday(BaseModel):
    startTime: datetime.datetime
    endTime: datetime.datetime
    savedAutomatically: bool
    pomodoroPauses: List
    tags: List[Tags]


class PomodoroRoot(BaseModel):
    __root__: List[PomodoroToday]


def get_period():
    response = requests.get(os.environ['HOST'] + f'/pomodoro?start={datetime.datetime.today().strftime("%Y-%m-%d")}&end={datetime.datetime.today().strftime("%Y-%m-%d")}')
    try:
        get_pomodoro = PomodoroRoot.parse_raw(response.text)

    except ValidationError as e:
        print(e.json())
    return get_pomodoro