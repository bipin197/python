from fastapi import FastAPI
import requests

app = FastAPI()

BASE_URL = "https://api.cricapi.com/v1"

@app.get("/series")
def get_all_cricket_series_data(apiKey: str):
    url = f"{BASE_URL}/series?apikey={apiKey}&offset=0"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch all series data"}

@app.get("/series/{series_id}")
def get_cricket_series_data(series_id: str, apiKey: str):
    url = f"{BASE_URL}/series?apikey={apiKey}&search={series_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch series data"}
