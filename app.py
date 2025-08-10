# app.py
import os
from flask import Flask, jsonify, request, abort

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret')

@app.route('/')
def index():
    return "Secure CI/CD Demo - Hello!"

@app.route('/health')
def health():
    return jsonify(status='ok')

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json(silent=True)
    if not data:
        abort(400, description='JSON required')
    return jsonify(received=data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
