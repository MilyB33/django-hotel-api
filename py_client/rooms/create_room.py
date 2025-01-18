import requests

hotel_id = input("Provide hotel id:\n")
type = input("Provide room type (single, double, suite):\n")
capacity = input("Provide room capacity:\n")
price_per_night = input("Provide price per night:\n")
is_available = input("Provide availability of the room (True or False):\n")
token = input("Provide authorization token:\n")
endpoint = f'http://127.0.0.1:8000/api/hotels/{hotel_id}/rooms/'

headers = {
    "Authorization": f"Bearer {token}"
}

data = {
    "room_type": type,
    "capacity": capacity,
    "price_per_night": price_per_night,
    "is_available": is_available,
}

response = requests.post(endpoint,json=data, headers=headers)

print(response.json())