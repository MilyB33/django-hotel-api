import requests


hotel_id = input("Provide hotel_id\n")
hotel_name = input("Provide hotel name.\n") or None
location = input("Provide hotel location.\n") or None
description = input("Provide hotel description.\n") or None
token = input("Provide authorization token:\n")

headers = {
    'Authorization': f'Bearer {token}'
}

endpoint = f'http://127.0.0.1:8000/api/hotels/{hotel_id}/'

response = requests.patch(endpoint, json={ "name": hotel_name, "location" : location, "description": description }, headers=headers)

print(response.json())