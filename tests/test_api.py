from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_route():
    payload = {
        "delay_days": 45,
        "contact_count": 3,
        "promise_given": True,
        "promise_kept": False
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "recommended_action" in response.json()