from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def hello_world():
    x = 1 + 'a'
    return 'Hello, World!'
