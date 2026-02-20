from app import app


def test_health_check():
    client = app.test_client()
    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json["status"] == "ok"


def test_predict_endpoint():
    client = app.test_client()
    response = client.post(
        "/api/predict",
        json={"student_id": "0001"}
    )

    assert response.status_code == 200
    assert "predicted_final_grade" in response.json
