from pydantic import BaseModel
import datetime
from typing import List


class Tag(BaseModel):
    name: str
    removed: bool


class Pomodoro(BaseModel):
    startTime: datetime.datetime
    endTime: datetime.datetime
    savedAutomatically: bool
    pomodoroPauses: List
    tags: List[Tag]


class GetTagsResponse(BaseModel):
    __root__: List[Pomodoro]
