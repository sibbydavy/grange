from datetime import datetime
from flask import render_template, jsonify
from FlaskWebProject1 import app
import FlaskWebProject1.FarmMaster



@app.route('/todo/api/v1.0/farms', methods=['GET'])
def get_farms():
    x = FlaskWebProject1.FarmMaster.FarmMasterDetail('ELANCHI') 
    tasks = [
    {
        'id': x._farmCode,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]
    return jsonify({'farms': tasks})
