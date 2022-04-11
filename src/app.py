import os
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from model import SA_Model

model = SA_Model()

app = Flask(__name__)
cors = CORS(app,support_credentials = True)

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Access'})

@app.route("/emotion", methods=["POST", "GET"])
@cross_origin(origin='*', supports_credentials=True)
def result():
    msg = request.form.get('msg')
    if msg == None:
        return jsonify({'message': 'Fail'}), 400
    else:
        emotion = model.get_emotion(msg)
        response = jsonify({'emotion': emotion})
        return response

@app.after_request
def add_headers(response):
    response.headers.add('Content-Type', 'application/json')
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'PUT, GET, POST, DELETE, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Expose-Headers', 'Content-Type,Content-Length,Authorization,X-Pagination')
    return response

@app.errorhandler(500)
def server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "server error"
    }), 500


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 2000))
    app.run(host='0.0.0.0', port=port, debug=True)
