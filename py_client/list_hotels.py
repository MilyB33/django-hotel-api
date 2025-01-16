import requests

hotel_id = input("Provide hotel id (skip for list):\n")

endpoint = ""

if hotel_id:
    endpoint = f'http://127.0.0.1:8000/api/hotels/{hotel_id}/'
else:
    endpoint = f'http://127.0.0.1:8000/api/hotels/'


response = requests.get(endpoint)

print(response.json())