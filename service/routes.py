from flask import jsonify, request, make_response
from service import app
from service.models import Account

@app.route("/health", methods=["GET"])
def health():
    return jsonify(dict(status="OK")), 200

@app.route("/accounts", methods=["POST"])
def create_accounts():
    data = request.get_json()
    account = Account(name=data.get("name"), email=data.get("email"), address=data.get("address"))
    account.create()
    return jsonify({"id": account.id, "name": account.name, "email": account.email, "address": account.address}), 201

@app.route("/accounts", methods=["GET"])
def list_accounts():
    accounts = Account.all()
    results = [{"id": a.id, "name": a.name, "email": a.email, "address": a.address} for a in accounts]
    return jsonify(results), 200

@app.route("/accounts/<int:account_id>", methods=["GET"])
def get_accounts(account_id):
    account = Account.find(account_id)
    if not account:
        return make_response(jsonify({"error": "Account not found"}), 404)
    return jsonify({"id": account.id, "name": account.name, "email": account.email, "address": account.address}), 200

@app.route("/accounts/<int:account_id>", methods=["PUT"])
def update_accounts(account_id):
    account = Account.find(account_id)
    if not account:
        return make_response(jsonify({"error": "Account not found"}), 404)
    data = request.get_json()
    account.name = data.get("name", account.name)
    account.email = data.get("email", account.email)
    account.address = data.get("address", account.address)
    account.update()
    return jsonify({"id": account.id, "name": account.name, "email": account.email, "address": account.address}), 200

@app.route("/accounts/<int:account_id>", methods=["DELETE"])
def delete_accounts(account_id):
    account = Account.find(account_id)
    if account:
        account.delete()
    return "", 204
