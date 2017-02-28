from flask import Flask, jsonify, Response, abort, make_response, request
import json
from flask import Blueprint

apiPOST = Blueprint('apiPOST',__name__)

def tt():
  with open('tasks.json') as data:
    tasks = json.load(data)
  return tasks
  
@apiPOST.route('/get', methods= ['GET'])
def get_tasks():
  return jsonify(tasks)

@apiPOST.route('/tasks/<int:task_id>', methods = ["PUT"])
def update_task(task_id):
  tlist = tt()
  task = [task for task in tlist if task['id']== task_id]
  if len(task) == 0:
    abort(404)
  if not request.json:
    abort(404)
  if 'title' in request.json and type(request.json['title']) != unicode:
    abort(404)
  if 'description' in request.json and type(request.json['description']) != unicode:
    abort(404)
  if 'done' in request.json and type(request.json['done']) != bool:
    abort(404)
  task[0]['title'] = request.json.get('title', task[0]['title'])
  task[0]['description'] = request.json.get('description', task[0]['description'])
  task[0]['done'] = request.json.get('done', task[0]['done'])
  with open('tasks.json', mode='w') as data:
    json.dump(tlist, data)
  return jsonify(task[0])

@apiPOST.route('/tasks/<int:task_id>', methods=['DELETE','PUT'])
def delete_task(task_id):
  tlist = tt()
  task = [task for task in tlist if task['id']== task_id]
  if len(task)==0:
    abort(404)
  tlist.remove(task[0])
  with open('tasks.json', mode='w') as data:
    json.dump(tlist, data)
  return jsonify({'result':True}), 201
  
@apiPOST.route('/tasks', methods=['GET', 'POST'])
def create_task():
  if not request.json or not 'title' in request.json:
    abort(404)
  tlist = tt()
  task = {
    'id': tlist[-1]['id'] + 1,
    'title': request.json['title'],
    'description': request.json.get('description', ""),
    'done': False
  }
  tlist.append(task)
  with open('tasks.json', mode='w') as data:
    json.dump(tlist, data)
  return jsonify(task), 201

@apiPOST.route('/')
def index():
    return "<h1>Hello, this is the entry for POST</h1>"