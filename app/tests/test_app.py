from app.app import app

def test_health():
    client = app.test_client()
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json["status"] == "ok"

def test_hello_valid():
    client = app.test_client()
    r = client.post("/hello", json={"name": "Antonio_123"})
    assert r.status_code == 200
    assert "Hello, Antonio_123" in r.json["message"]

def test_hello_invalid():
    client = app.test_client()
    r = client.post("/hello", json={"name": "bad name with spaces"})
    assert r.status_code == 400
