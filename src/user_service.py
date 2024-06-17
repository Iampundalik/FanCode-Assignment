from src.api_client import get_users, get_todos

def is_fancode_city(lat, lng):
    return -40 < float(lat) < 5 and 5 < float(lng) < 100

def get_fancode_users(users):
    return [user for user in users if is_fancode_city(user['address']['geo']['lat'], user['address']['geo']['lng'])]

def calculate_completion_rate(user_id, todos):
    user_todos = [todo for todo in todos if todo['userId'] == user_id]
    completed_todos = [todo for todo in user_todos if todo['completed']]
    return len(completed_todos) / len(user_todos) if user_todos else 0

def get_fancode_users_with_high_completion():
    users = get_users()
    todos = get_todos()
    fancode_users = get_fancode_users(users)
    return [user for user in fancode_users if calculate_completion_rate(user['id'], todos) > 0.5]
