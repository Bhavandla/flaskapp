from flask import Flask
import apitestGET, apitestPOST
import auth

app = Flask(__name__)
app.register_blueprint(apitestGET.apiGET, url_prefix = '/GET')
app.register_blueprint(apitestPOST.apiPOST, url_prefix = '/POST')
# app.register_blueprint(apitestPOST)

@app.route('/')
def index():
    return "<h1>Hello, world!</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)