# Put and delete HTTP verbs
# Working with JSON

from flask import Flask, jsonify, request

app = Flask(__name__)

items = [
    {'id': 1, 'name': 'Task 1', 'description': 'Description of Task 1'},
    {'id': 2, 'name': 'Task 2', 'description': 'Description of Task 2'},
    {'id': 3, 'name': 'Task 3', 'description': 'Description of Task 3'}
]

@app.route('/', methods=['GET'])
def home():
    return "Welcome to a TODO List FLask Implementation"
# Get: retrieve all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

#Get: retrieve a single item by id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({'error': 'Item not found'}), 404
# Post: create a new item
@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.get_json()
    if not new_item or 'name' not in new_item:
        return jsonify({'error': 'Invalid item data'}), 400
    new_item['id'] = len(items) + 1
    items.append(new_item)
    return jsonify(new_item), 201

# Delete: delete an item by id
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'message': 'Item deleted successfully'}), 200

# Put: update an item by id
@app.route('/items/<int:item_id>', methods=['PUT']) 
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    updated_item = request.get_json()
    if not updated_item or 'name' not in updated_item:
        return jsonify({'error': 'Invalid item data'}), 400
    item['name'] = updated_item['name']
    return jsonify(item)

# Run the Flask app
    
if __name__ == '__main__':
    app.run(debug=True)