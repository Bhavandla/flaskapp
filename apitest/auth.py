from flask.ext.httpauth import HTTPBasicAuth
from flask import jsonify, make_response

auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
  if username == "manoh":
    return "pythoni"
  return None

@auth.error_handler
def unauthorized():
  return make_response(jsonify({'error': 'Unauthorized access'})), 401