from model.pomodoro_auto_save_request import PomodoroAutoSaveRequest
from rest import http_backend_client


def save_pomodoro_automatically(key):
    body = PomodoroAutoSaveRequest(1, key)
    body = body.json()
    response = http_backend_client.post("/timer/v1/pomodoro/auto", body)
    return response.status_code
