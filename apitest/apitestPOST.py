from flask import Flask, jsonify, Response, abort, make_response, request
import json
from flask import Blueprint

apiPOST = Blueprint('apiPOST',__name__)

with open('tasks.json') as data:
  t = json.load(data)
  tasks = t['tasks']
  
@apiPOST.route('/get', methods= ['GET'])
def get_tasks():
  return jsonify(tasks)

@apiPOST.route('/tasks', methods=['POST'])
def create_task():
  if not request.json or not 'title' in request.json:
    abort(404)
  task = {
    'id': tasks[-1]['id'] + 1,
    'title': request.json['title'],
    'description': request.json.get('description', ""),
    'done': False
  }
  tasks.append(task)
  with open('tasks.json', mode='w') as data:
    json.dump(tasks, data)
  return jsonify(tasks), 201

@apiPOST.route('/')
def index():
    return "<h1>Hello, this is the entry for POST</h1>"