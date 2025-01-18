import requests

hotel_id = input("Provide hotel id:\n")
token = input("Provide authorization token:\n")
endpoint = f'http://127.0.0.1:8000/api/hotels/{hotel_id}/'

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.delete(endpoint, headers=headers)

print(response.status_code)