import requests

review_id = input("Provide review id:\n")

endpoint = f'http://127.0.0.1:8000/api/reviews/{review_id}'

response = requests.get(endpoint)

print(response.json())