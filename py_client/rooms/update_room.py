import requests

room_id = input("Provide room id:\n")
type = input("Provide room type (single, double, suite):\n")
token = input("Provide authorization token:\n")
endpoint = f'http://127.0.0.1:8000/api/rooms/{room_id}/'

headers = {
    "Authorization": f"Bearer {token}"
}

data = {
    "room_type": type,
}

response = requests.patch(endpoint,json=data, headers=headers)

print(response.json())