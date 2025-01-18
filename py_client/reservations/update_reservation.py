import requests
from datetime import date, timedelta

reservation_id = input("Provide reservation id\n")
check_out_date = (date.today() + timedelta(days=2)).isoformat()
token = input("Provide authorization token:\n")

headers = {
    'Authorization': f'Bearer {token}'
}

endpoint = f'http://127.0.0.1:8000/api/reservations/{reservation_id}/'

response = requests.patch(endpoint, json={ "check_out_date": check_out_date }, headers=headers)

print(response.json())