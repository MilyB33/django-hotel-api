import requests
from getpass import getpass

endpoint = 'http://127.0.0.1:8000/api/auth/register/'

username = input('What is your username?\n')
email = input("What is your email?\n")
password = getpass("What is your password?\n")

response = requests.post(endpoint, json={ "username": username, "password": password, "password2": password, "email": email, "first_name": 'test', "last_name": 'test' })

print(response.json())