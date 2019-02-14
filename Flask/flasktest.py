from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"
@app.route('/branch1')
def branch1():
    return "I am on branch 1"
@app.route('/testuser/<name>')
def username(name):
    return 'Hello %s' % name

