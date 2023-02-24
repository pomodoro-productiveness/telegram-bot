from model.pomodoro_auto_save_request import PomodoroAutoSaveRequest
from rest import http_backend_client


def save_pomodoro_automatically(key):
    auto_save_request = PomodoroAutoSaveRequest(numbersToSaveAutomatically=1, tagGroupId=key)
    response = http_backend_client.post("/pomodoro/auto", auto_save_request.json())
    return response.status_code
