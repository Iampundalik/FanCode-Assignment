from behave import *
from src.user_service import get_fancode_users_with_high_completion, calculate_completion_rate
from src.api_client import get_users, get_todos

@given('the list of users and their todos')
def step_given_users_and_todos(context):
    context.users = get_users()
    context.todos = get_todos()

@when('filtering users from the city "FanCode"')
def step_when_filter_fancode_users(context):
    context.fancode_users = get_fancode_users_with_high_completion()

@then('each FanCode user should have more than 50% of their todos completed')
def step_then_check_completion_rate(context):
    assert all(calculate_completion_rate(user['id'], context.todos) > 0.5 for user in context.fancode_users), \
        "Some FanCode users do not have more than 50% of their todos completed"
