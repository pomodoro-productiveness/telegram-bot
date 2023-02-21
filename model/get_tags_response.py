from pydantic import BaseModel
from typing import List


class Tag(BaseModel):
    id: int
    name: str
    removed: bool


class TagsGroup(BaseModel):
    id: int
    pomodoroTags: List[Tag]
    orderNumber: int


class GetTagsResponse(BaseModel):
    __root__: List[TagsGroup]
