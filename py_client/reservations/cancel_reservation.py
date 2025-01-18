import requests

reservation_id = input("Provide reservation id\n")
token = input("Provide authorization token:\n")

headers = {
    'Authorization': f'Bearer {token}'
}

endpoint = f'http://127.0.0.1:8000/api/reservations/{reservation_id}/'

response = requests.delete(endpoint, headers=headers)

print(response.status_code)