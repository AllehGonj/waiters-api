import requests


def fetch_menu():
    request = requests.get('https://jsonplaceholder.typicode.com/todos')
    is_success = request.status_code == requests.codes.ok
    response = {
        'menu': [1, 2, 3, 4, 5] if is_success else None,
        'message': None if is_success else 'Oops! and error occurred',
        'reason': None if is_success else request.json()
    }
    return remove_empty_value(response.copy()), request.status_code


def take_order(order):
    request = requests.post('https://jsonplaceholder.typicode.com/todos', data=order)
    is_success = request.status_code == requests.codes.created
    response = {
        'message': 'Order successfully entered!' if is_success else 'Oops! and error occurred',
        'reason': None if is_success else request.json()
    }
    return remove_empty_value(response.copy()), request.status_code


def serve_table(order):
    request = requests.post('https://jsonplaceholder.typicode.com/todos', data=order)
    is_success = request.status_code == requests.codes.created
    response = {
        'message': 'Order successfully served!' if is_success else 'Oops! and error occurred',
        'reason': None if is_success else request.json()
    }
    return remove_empty_value(response.copy()), request.status_code


def clean_table(table_id):
    request = requests.put(f'https://jsonplaceholder.typicode.com/todos/{table_id}')
    is_success = request.status_code == requests.codes.ok
    response = {
        'message': 'Table cleaned!' if is_success else 'Oops! and error occurred',
        'reason': None if is_success else request.json()
    }
    return remove_empty_value(response.copy()), request.status_code


def remove_empty_value(data):
    for key, value in list(data.items()):
        if value is None:
            del data[key]
        elif isinstance(value, dict):
            remove_empty_value(value)
    return data
