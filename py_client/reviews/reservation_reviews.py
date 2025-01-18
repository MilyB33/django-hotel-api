import requests

reservation_id = input("Provide reservation id:\n")
token = input("Provide authorization token:\n")

endpoint = f'http://127.0.0.1:8000/api/reservations/{reservation_id}/reviews/'


headers = {
    'Authorization': f'Bearer {token}'
}


response = requests.get(endpoint, headers=headers)

print(response.json())