import requests
from datetime import date, timedelta


room = input("Provide room id.\n")
check_in_date = date.today().isoformat()
check_out_date = (date.today() + timedelta(days=1)).isoformat()
token = input("Provide authorization token:\n")

headers = {
    'Authorization': f'Bearer {token}'
}

endpoint = f'http://127.0.0.1:8000/api/reservations/'

response = requests.post(endpoint, json={ "room": room, "check_in_date" : check_in_date, "check_out_date": check_out_date }, headers=headers)

print(response.json())