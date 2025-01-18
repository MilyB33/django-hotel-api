import requests

review_id = input("Provide review id\n")
rating = input("Provide rating\n")
token = input("Provide authorization token:\n")

endpoint = f'http://127.0.0.1:8000/api/reviews/{review_id}/'

data = {
    "rating": rating
}

headers = {
    'Authorization': f'Bearer {token}'
}


response = requests.patch(endpoint, json=data, headers=headers)

print(response.json())