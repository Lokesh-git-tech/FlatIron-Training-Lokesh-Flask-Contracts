#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

@app.route('/contract/<id>', methods=['GET'])
def get_contract(id):
    contract_info = next((c for c in contracts if c.get("id") == id), None)
    response = {}
    if contract_info:
        response["message"] = "Contract found"
        response["info"] = contract_info
        response_code = 200
    else:
        response_code = 404
        response["message"] = "Contract not found"
    return response, response_code

@app.route('/customer/<customer_name>', methods=['GET'])
def get_customer(customer_name):
    found = True if customer_name in customers else False
    response = {}
    if found:
        response_code = 204
    else:
        response_code = 404
    return response, response_code

if __name__ == '__main__':
    app.run(port=5555, debug=True)
