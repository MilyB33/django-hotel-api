import requests
from getpass import getpass

endpoint = 'http://127.0.0.1:8000/api/auth/logout/'

headers = {
    "Authorization": 'Bearer cbbae7c298548f99b1594a733f0cbf773039c078'
}

response = requests.post(endpoint, headers=headers)

print(response.json())