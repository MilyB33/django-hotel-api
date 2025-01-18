import requests

reservation_id = input("Provide reservation id:\n")
rating = input("Provide rating\n")
comment = input("Provide comment\n")
token = input("Provide authorization token:\n")

endpoint = f'http://127.0.0.1:8000/api/reservations/{reservation_id}/reviews/'

data = {
    "rating": rating,
    "comment": comment,
}

headers = {
    'Authorization': f'Bearer {token}'
}


response = requests.post(endpoint, json=data, headers=headers)

print(response.json())