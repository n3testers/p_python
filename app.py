from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for items
items = []

# Create a new item
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    item_id = len(items) + 1
    item = {
        'id': item_id,
        'name': data['name'],
        'description': data.get('description', '')
    }
    items.append(item)
    return jsonify(item), 201

# Get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items), 200

# Get a single item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    return jsonify(item), 200

# Update an item by ID
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    item['name'] = data.get('name', item['name'])
    item['description'] = data.get('description', item['description'])
    return jsonify(item), 200

# Delete an item by ID
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
