from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# from a server point of view
# POST is used to receive data
# GET is used to send data
# from the browser's point of view, however, this is the opposite

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]


# Some endpoints

# POST  /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    
    request_data = request.get_json()
    
    new_store = {
        'name': request_data['name'],
        'items': []
    }

    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>
# "http://127.0.1.1:5000/store/some_name"
@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    # iterate over stores, if name match, return store
    # else return an error message
    
    for store in stores:
        if store['name'] == name:
            return jsonify({'store':store})

    return jsonify({'message':"store '%s' not found" % name})


# GET /store
@app.route('/store')  # GET is default
def get_stores():
    return jsonify({'stores':stores})


# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    
    request_data = request.get_json()

    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }

            store['items'].append(new_item)
            return jsonify({'store':store['items']})

    return jsonify({'message':"store '%s' not found" % name})


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    # iterate over stores, if name match, return store
    # else return an error message
    
    for store in stores:
        if store['name'] == name:
            return jsonify({'items':store['items']})

    return jsonify({'message':"store '%s' not found" % name})


@app.route('/')  # root endpoint
def home():
    return render_template('index.html')

app.run(port=5000)
