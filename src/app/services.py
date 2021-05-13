import random
import time

import requests

menu_mock = [1, 2, 3, 4, 5]

waiters_entity_time_attrs = {
    "obtain-menu": 1.0,
    "take-order": 3.0,
    "serve-table": 3.0,
    "clean-table": 2.0,
}

waiter_id = random.randint(1, 3)

kitchen_root_domain = 'https://jsonplaceholder.typicode.com'
table_root_domain = 'https://scmesas.azurewebsites.net'


def fetch_menu():
    request = requests.get(f'{kitchen_root_domain}/todos')
    is_success = request.status_code == requests.codes.ok
    response = {
        'menu': menu_mock if is_success else None,
        'message': None if is_success else 'Oops! and error occurred',
        'reason': None if is_success else request.json()
    }
    time.sleep(waiters_entity_time_attrs["obtain-menu"])
    return remove_empty_value(response.copy()), request.status_code


def take_order(order):
    request = requests.post(f'{kitchen_root_domain}/todos', data=order)
    is_success = request.status_code == requests.codes.created
    response = {
        'message': 'Order successfully entered!' if is_success else 'Oops! and error occurred',
        'reason': None if is_success else request.json()
    }
    time.sleep(waiters_entity_time_attrs["take-order"])
    return remove_empty_value(response.copy()), request.status_code


def serve_table(order):
    params = {
        'encargado': waiter_id
    }
    table_id = order["id_mesa"]

    request = requests.get(f'{table_root_domain}/servirMesa/{table_id}', params=params)
    is_success = request.status_code == requests.codes.ok
    response = {
        'message': 'Order successfully served!' if is_success else 'Oops! and error occurred',
        'reason': None if is_success else request.json()
    }
    time.sleep(waiters_entity_time_attrs["serve-table"])
    return remove_empty_value(response.copy()), request.status_code


def clean_table(table_id):
    request = requests.put(f'{table_root_domain}/limpiarMesa/{table_id}')
    is_success = request.status_code == requests.codes.ok
    response = {
        'message': 'Table cleaned!' if is_success else 'Oops! and error occurred',
        'reason': None if is_success else request.json()
    }
    time.sleep(waiters_entity_time_attrs["clean-table"])
    return remove_empty_value(response.copy()), request.status_code


def remove_empty_value(data):
    for key, value in list(data.items()):
        if value is None:
            del data[key]
        elif isinstance(value, dict):
            remove_empty_value(value)
    return data
