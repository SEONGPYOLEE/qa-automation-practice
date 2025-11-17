import requests

BASE = "https://jsonplaceholder.typicode.com"

def test_get_user():
    r = requests.get(f"{BASE}/users/1")
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == 1

def test_post_user():
    payload = {"name": "lee", "job": "qa"}
    r = requests.post(f"{BASE}/posts", json=payload)
    assert r.status_code == 201
    assert r.json()["name"] == "lee"

def test_put_user():
    payload = {"id": 1, "name": "lee2", "job": "qa senior"}
    r = requests.put(f"{BASE}/posts/1", json=payload)
    assert r.status_code == 200
    assert r.json()["id"] == 1

def test_delete_user():
    r = requests.delete(f"{BASE}/posts/1")
    assert r.status_code == 200   # JSONPlaceholder는 DELETE → 200 반환