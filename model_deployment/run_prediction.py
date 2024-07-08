import requests

url = "http://127.0.0.1:8000/predict"
payload = {
    "Temperature": 25.0,
    "Oxygen": 21.0,
    "Humidity": 60.0
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
