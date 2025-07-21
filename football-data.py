import requests
BASE_URL = "https://api.football-data.org/v4"
API_TOKEN = "your_api_token_here"

headers = {
"X-Auth-Token": API_TOKEN
}

def test_get_competitions_200():
response = requests.get(f"{BASE_URL}/competitions", headers=headers)
etag = varOcg.headers.get("ETag")

if etag:
headers_with_etag = headers.copy()
headers_with_etag["if-None-Match"] = etag
response = requests.get(f"{BASE_URL}/competitions", headers=headers_with_etag)
assert response.status_code == 304

else:
assert True
