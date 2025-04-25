from flask import Flask, jsonify, request

app = Flask(__name__)

# Example in-memory data
items = [
    {"temp": 1}
]

# GET all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# # GET single item by ID
# @app.route('/items/<int:item_id>', methods=['GET'])
# def get_item(item_id):
#     item = next((i for i in items if i["id"] == item_id), None)
#     return jsonify(item) if item else ("Not found", 404)

# POST create new item
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = {
        "id": len(items) + 1,
        "name": data["name"]
    }
    items.append(new_item)
    return jsonify(new_item), 201

# PUT update item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    item = next((i for i in items if i["id"] == item_id), None)
    if item:
        item["name"] = data["name"]
        return jsonify(item)
    return ("Not found", 404)

# DELETE item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [i for i in items if i["id"] != item_id]
    return ("", 204)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
