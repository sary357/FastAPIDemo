from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_save_vote():
    response = client.post("/save-vote",json={"key": "value"})
    assert response.status_code == 200

def test_save_vote_invalid_request():
    response = client.post(
        "/save-vote",
        #json="",  # 不傳入 JSON 字串，應該觸發 400 錯誤
    )
    assert response.status_code == 400