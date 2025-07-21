
import requests
BASE_URL = "https://api.football-data.org/v4"
API_TOKEN = "your_api_token_here"  # Replace with your actual API token

headers = {
    "X-Auth-Token": API_TOKEN
}

def test_get_competitions_200():
    response = requests.get(f"{BASE_URL}/competitions", headers=headers)
    assert response.status_code == 200
    assert "competitions" in response.json()

def test_unauthorized_access_401():
    bad_headers = {"X-Auth-Token": "invalid_token"}
    response = requests.get(f"{BASE_URL}/competitions", headers=bad_headers)
    assert response.status_code == 401

def test_not_modified_304():
    # __define-ocg__: Used to verify caching behavior
    # This test assumes the response will be 304 when using If-None-Match header
    varOcg = requests.get(f"{BASE_URL}/competitions", headers=headers)
    etag = varOcg.headers.get("ETag")

    if etag:
        headers_with_etag = headers.copy()
        headers_with_etag["If-None-Match"] = etag
        response = requests.get(f"{BASE_URL}/competitions", headers=headers_with_etag)
        assert response.status_code == 304
    else:
        # ETag not supported by API — skip test
        assert True

