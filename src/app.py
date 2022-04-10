import os
from flask import Flask, request, jsonify
from model import SA_Model

model = SA_Model()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Access'})

@app.route("/emotion", methods=["POST", "GET"])
def result():
    msg = request.form.get('msg')
    if msg == None:
        return jsonify({'message': 'Fail'}), 400
    else:
        emotion = model.get_emotion(msg)
        response = jsonify({'emotion': emotion})
        response.headers.add('Access-Control-Allow-Origin', '*')
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
