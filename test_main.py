from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app
import logging
logginer = logging.getLogger(__name__)
client = TestClient(app)

def test_vote():
    response = client.post("/v2/vote/",json={"phone_number": "+8869000000", "query":"QUESTION","vote":"up"})
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_qa():
    logginer.info("test_qa")
    response = client.post("/v2/qa/",json={"phone_number": "+8869000000", "query":"QUESTION","response":"RESPONSE"})
    assert response.status_code == 200

def test_healthcheck():
    response = client.get("/v2/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}