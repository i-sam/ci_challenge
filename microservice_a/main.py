from flask import Flask, jsonify, make_response

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response(jsonify({'message': 'OK'}))
    response.status_code = 200
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
