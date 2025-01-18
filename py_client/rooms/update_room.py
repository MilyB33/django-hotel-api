import requests

room_id = input("Provide room id:\n")
is_available = input("Provide availability of the room (True or False):\n")
token = input("Provide authorization token:\n")
endpoint = f'http://127.0.0.1:8000/api/rooms/{room_id}/'

headers = {
    "Authorization": f"Bearer {token}"
}

data = {
    "is_available": is_available,
}

response = requests.patch(endpoint,json=data, headers=headers)

print(response.json())