from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Initial list of cats with IDs and image links
CATS = {
    'cat1': {'id': 'cat1', 'name': 'Fluffy', 'age': 2, 'image_link': 'https://storage.googleapis.com/mle-courses-prod/users/61b6fa1ba83a7e37c8309756/private-files/43c19bd0-66aa-11ef-9b72-9db6eacc12d1-kitty.png'},
    'cat2': {'id': 'cat2', 'name': 'Mittens', 'age': 4, 'image_link': 'https://storage.googleapis.com/mle-courses-prod/users/61b6fa1ba83a7e37c8309756/private-files/41354ba0-66aa-11ef-b0a7-998b84b38d43-kitty__1_.png'},
    'cat3': {'id': 'cat3', 'name': 'Whiskers', 'age': 3, 'image_link': 'https://storage.googleapis.com/mle-courses-prod/users/61b6fa1ba83a7e37c8309756/private-files/3f3d9a50-66aa-11ef-b0a7-998b84b38d43-cat.png'},
}

def abort_if_cat_doesnt_exist(cat_id):
    if cat_id not in CATS:
        abort(404, description="Cat {} doesn't exist".format(cat_id))

@app.route('/', methods=['GET'])
def hello():
    return 'Hello! Welcome to the Cat API.'

# GET all cats
@app.route('/cats', methods=['GET'])
def get_cats():
    return jsonify(CATS)

# GET a specific cat by ID
@app.route('/cats/<cat_id>', methods=['GET'])
def get_cat(cat_id):
    abort_if_cat_doesnt_exist(cat_id)
    return jsonify(CATS[cat_id])

# POST a new cat
@app.route('/cats', methods=['POST'])
def create_cat():
    if not request.json or 'name' not in request.json:
        abort(400, description="Invalid request. Must include 'name'.")
    
    # TODO 1: Tạo id mới cho mèo mới dựa vào chiều dài hiện tại của CATS
    # Ví dụ CATS đang có 3 phần ử thì key mới là cat4
    # cat_id = None
    cat_id = f'cat{len(CATS) + 1}'

    # TODO 2: Lấy dữ liệu từ request
    # new_cat = None
    new_cat = {
        'id': cat_id,
        'name': request.json['name'],
        'age': request.json.get('age', 0),
        'image_link': request.json.get('image_link', '')
    }

    # TODO 3: Thêm dữ liệu vào từ điển
    CATS[cat_id] = new_cat
    return jsonify(CATS[cat_id]), 201

# DELETE a specific cat by ID
@app.route('/cats/<cat_id>', methods=['DELETE'])
def delete_cat(cat_id):
    abort_if_cat_doesnt_exist(cat_id)
    del CATS[cat_id]
    return '', 204

# PUT - Update an entire cat entry
@app.route('/cats/<cat_id>', methods=['PUT'])
def update_cat(cat_id):
    abort_if_cat_doesnt_exist(cat_id)
    if not request.json or 'name' not in request.json:
        abort(400, description="Invalid request. Must include 'name'.")
    
    CATS[cat_id] = {
        'id': cat_id,
        'name': request.json['name'],
        'age': request.json.get('age', 0),
        'image_link': request.json.get('image_link', CATS[cat_id]['image_link'])
    }
    return jsonify(CATS[cat_id]), 200

# PATCH - Update part of a cat entry
@app.route('/cats/<cat_id>', methods=['PATCH'])
def patch_cat(cat_id):
    abort_if_cat_doesnt_exist(cat_id)
    if not request.json:
        abort(400, description="Invalid request. Must include data to update.")
    
    # TODO 4: Tìm mèo hiện tại
    # cat = None
    cat = CATS[cat_id]

    # TODO 5: Cập nhật mèo hiện tại qua các giá trị gửi lên
    # cat['name'] = None
    # cat['age'] = None
    # cat['image_link'] = None
    cat['name'] = request.json.get('name', cat['name'])
    cat['age'] = request.json.get('age', cat['age'])
    cat['image_link'] = request.json.get('image_link', cat['image_link'])
    return jsonify(cat), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5002)
