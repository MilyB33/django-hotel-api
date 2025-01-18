import requests

room_id = input("Provide room id:\n")

endpoint = f'http://127.0.0.1:8000/api/rooms/{room_id}/'


response = requests.get(endpoint)

print(response.json())