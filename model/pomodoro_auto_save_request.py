from pydantic import BaseModel


class PomodoroAutoSaveRequest(BaseModel):
    def __init__(self, numbers_to_save_automatically, tag_group_id):
        self.numbersToSaveAutomatically = numbers_to_save_automatically
        self.tagGroupId = tag_group_id
    numbersToSaveAutomatically: int
    tagGroupId: int
