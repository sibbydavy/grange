#!flask/bin/python
from flask import render_template, jsonify
from FlaskWebProject1 import app

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)