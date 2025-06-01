from flask import Flask, jsonify

app = Flask(__name__)

data1 = {"apple": "red", "banana": "yellow"}

@app.route('/')
def home():
    return jsonify({"message": "Hello from Flask!"})

@app.route('/data1', methods=['GET'])
def get_data1():
    return jsonify(data1)

def handler(environ, start_response):
    return app(environ, start_response)
