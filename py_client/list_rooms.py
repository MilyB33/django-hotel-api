import requests

hotel_id = input("Provide hotel id:\n")

endpoint = ""

endpoint = f'http://127.0.0.1:8000/api/hotels/{hotel_id}/rooms/'


response = requests.get(endpoint)

print(response.json())