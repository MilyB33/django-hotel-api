import requests

room_id = input("Provide room id:\n")
token = input("Provide authorization token:\n")
endpoint = f'http://127.0.0.1:8000/api/rooms/{room_id}/'

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.delete(endpoint, headers=headers)

print(response.status_code)