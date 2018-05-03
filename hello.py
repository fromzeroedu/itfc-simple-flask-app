from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<int:planet>')
def hello(planet):
    return render_template('hello.html', t_planet=planet)

@app.route('/form', methods=['GET'])
def form():
    import pdb; pdb.set_trace()
    first_name = request.args['first_name']
    last_name = request.args['last_name']
    return f'First Name: {first_name}, Last Name: {last_name}'
