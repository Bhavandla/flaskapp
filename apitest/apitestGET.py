#!flask/bin/python
from flask import Flask, jsonify, Response, abort, make_response, request
import json, os
from flask import Blueprint
import uris, auth

# apiGET = Flask(__name__)
apiGET = Blueprint('apiGET',__name__)

def tt():
  with open('tasks.json') as data:
    tasks = json.load(data)
  return tasks

@apiGET.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
  task = [task for task in tt() if task['id']==task_id]
#   task = [task for task in tasks['tasks'] if task['id']==task_id]
  if len(task) == 0:
    abort(404)
  return jsonify(task[0])

@apiGET.route('/tasks', methods= ['GET'])
@auth.auth.login_required
def get_tasks():
#   return Response(json.dumps(tasks, indent = None), mimetype='application/json')
  #return json.dumps({'tasks':tasks}, indent = None)
  return jsonify([uris.make_public_task(task) for task in tt()])
#   return jsonify(tt())

@apiGET.errorhandler(404)
def not_found(error):
  return make_response(jsonify({'error':'not found'}), 404)

@apiGET.route('/')
def index():
    return "<h1>Hello, this is the entry for GET</h1>"

# if __name__ == '__main__':
#     apiGET.run(host='0.0.0.0', port=8080, debug=True)