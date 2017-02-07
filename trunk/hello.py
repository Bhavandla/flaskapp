from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1 style='color:blue'>Hello, World! welcome!</h1>"

@app.route('/index')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
    
if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080)
      