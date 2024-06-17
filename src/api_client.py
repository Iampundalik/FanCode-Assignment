import requests

BASE_URL = "http://jsonplaceholder.typicode.com"

def get_users():
    response = requests.get(f"{BASE_URL}/users")
    response.raise_for_status()
    return response.json()

def get_todos():
    response = requests.get(f"{BASE_URL}/todos")
    response.raise_for_status()
    return response.json()
