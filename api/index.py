from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Optional, only if you want to allow cross-origin requests

# Sample data
data1 = {"apple": "red", "banana": "yellow"}
data2 = {"car": "blue", "bike": "green"}

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask API!"})

@app.route('/data1', methods=['GET'])
def get_data1():
    return jsonify(data1)

@app.route('/data2', methods=['GET'])
def get_data2():
    return jsonify(data2)

@app.route('/data1/<key>', methods=['GET'])
def get_data1_key(key):
    return jsonify({key: data1.get(key, "Key not found")})

@app.route('/data2/<key>', methods=['GET'])
def get_data2_key(key):
    return jsonify({key: data2.get(key, "Key not found")})

@app.route('/data1', methods=['POST'])
def update_data1():
    content = request.get_json()
    data1.update(content)
    return jsonify({"message": "data1 updated", "data1": data1})

@app.route('/data2', methods=['POST'])
def update_data2():
    content = request.get_json()
    data2.update(content)
    return jsonify({"message": "data2 updated", "data2": data2})


# THIS is the Vercel handler entrypoint:

def handler(environ, start_response):
    # `app` is your Flask WSGI app
    return app(environ, start_response)
