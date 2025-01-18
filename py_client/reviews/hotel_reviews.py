import requests

hotel_id = input("Provide hotel id:\n")

endpoint = f'http://127.0.0.1:8000/api/hotels/{hotel_id}/reviews/'


response = requests.get(endpoint)

print(response.json())