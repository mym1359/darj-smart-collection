from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_welcome_route():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Darj Smart Collection API"}

def test_recommend_route():
    payload = {
        "delay_days": 45,
        "contact_count": 2,
        "promise_given": True,
        "promise_kept": False
    }
    response = client.post("/recommend", json=payload)
    assert response.status_code == 200
    assert "recommended_action" in response.json()