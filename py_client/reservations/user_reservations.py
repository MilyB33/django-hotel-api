import requests

token = input("Provide authorization token:\n")

headers = {
    'Authorization': f'Bearer {token}'
}

endpoint = f'http://127.0.0.1:8000/api/user/reservations/'

response = requests.get(endpoint, headers=headers)

print(response.json())