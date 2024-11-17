import requests
import json

BASE = "http://127.0.0.1:5000"

response = requests.post(f"{BASE}/beer-company", json={
    "name": "Rocco"
})

print(response.status_code)
print(json.dumps(response.json(), indent=2))

print("///////////////////")

response_id = response.json()["id"]

response_get = requests.get(f"{BASE}/beer-company/rocco-s-beer-company")

print(response_get.status_code)
print(json.dumps(response_get.json(), indent=2))

print("///////////////////")

response_update = requests.put(f"{BASE}/beer-company/{response_id}", json={
    "description": "my description"
})

print(response_update.status_code)
print(json.dumps(response_update.json(), indent=2))

print("///////////////////")

response_delete = requests.delete(f"{BASE}/beer-company/bad-id")
print(response_delete.status_code)
print(json.dumps(response_delete.json(), indent=2))

print("///////////////////")

requests.post(f"{BASE}/beer-company", json={
    "name": "James"
})

response_list = requests.get(f"{BASE}/beer-companies")
print(response_list.status_code)
print(json.dumps(response_list.json(), indent=2))