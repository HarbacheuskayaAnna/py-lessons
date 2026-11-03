import requests

def test_get_user():
    url = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.get(url, timeout=10)
    assert response.status_code == 200, f"GET {url} returns {response.status_code}: {response.text}"
    body = response.json()
    assert body["id"] == 1, f"ID {body['id']} is not equal 1"
    assert 'email' in body, f"Email isn't received in the response. Fields: {list(body)}"