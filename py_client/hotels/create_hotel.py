import requests

endpoint = 'http://127.0.0.1:8000/api/hotels/'
hotel_name = input("Provide hotel name.\n")
location = input("Provide hotel location.\n")
description = input("Provide hotel description.\n")
token = input("Provide authorization token:\n")

headers = {
    'Authorization': f'Bearer {token}'
}

response = requests.post(endpoint, json={ "name": hotel_name, "location" : location, "description": description }, headers=headers)

print(response.json())