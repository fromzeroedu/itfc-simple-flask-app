from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greeting/<int:planet>')
def hello(planet):
    return render_template('hello.html', t_planet=planet)
