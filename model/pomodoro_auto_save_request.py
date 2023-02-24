from pydantic import BaseModel


class PomodoroAutoSaveRequest(BaseModel):
    numbersToSaveAutomatically: int
    tagGroupId: int
