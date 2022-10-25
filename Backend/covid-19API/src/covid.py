from flask import Flask, render_template, request, jsonify, Response
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId
import json
import os
from dotenv import load_dotenv
import requests

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False

CORS(app)

@app.route('/', methods=['GET'])
def add_covld():
    res = requests.get('https://covid19-japan-web-api.now.sh/api/v1/prefectures')
    output = json.loads(res.text)
    return jsonify({'result': output})


if __name__ == '__main__':
    app.debug = True 
    app.run(host='0.0.0.0', port=5006)
