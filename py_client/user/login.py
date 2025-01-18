import requests
from getpass import getpass

endpoint = 'http://127.0.0.1:8000/api/auth/login/'

username = input('What is your username?\n')
password = getpass("What is your password?\n")

response = requests.post(endpoint, json={ "username": username, "password": password })

print(response.json())