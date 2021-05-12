from flask import Blueprint, request, jsonify
from flask_cors import cross_origin

from src.app.services import fetch_menu, take_order, serve_table, clean_table

api = Blueprint('waiters', __name__)


@api.route('/menu', methods=['GET'])
@cross_origin()
def menu():
    data, status_code = fetch_menu()
    return jsonify(data), status_code


@api.route('/order', methods=['POST'])
@cross_origin()
def order():
    content = request.get_json()
    if content is None:
        data = {
            'message': 'Body is required'
        }
        status_code = 400
    else:
        data, status_code = take_order(content)

    return jsonify(data), status_code


@api.route('/serve', methods=['POST'])
@cross_origin()
def serve():
    content = request.get_json()
    if content is None:
        data = {
            'message': 'Body is required'
        }
        status_code = 400
    else:
        data, status_code = serve_table(content)
    return jsonify(data), status_code


@api.route('/clean', methods=['POST'])
@cross_origin()
def clean():
    table_id = request.args.get('tableId')
    if table_id is None:
        data = {
            'message': 'Table ID is required'
        }
        status_code = 400
    else:
        data, status_code = clean_table(table_id)

    return jsonify(data), status_code
