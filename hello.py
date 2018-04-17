from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello/<int:planet>')
def hello(planet):
    return f'Hello, {planet}'
