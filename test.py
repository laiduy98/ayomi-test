from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_calculate():
    response = client.post("/calculate/", json={"expression": "3 4 + 2 * 1 /"})
    assert response.status_code == 200
    assert response.json()["result"] == 14.0
    assert "timestamp" in response.json()

def test_export():
    response = client.get("/export/")
    assert response.status_code == 200
    assert response.headers["Content-Disposition"] == "attachment; filename=operations.csv"
    assert "text/csv" in response.headers["content-type"]