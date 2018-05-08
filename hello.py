from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<int:planet>')
def hello(planet):
    return render_template('hello.html', t_planet=planet)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        return f'First Name: {first_name}, Last Name: {last_name}'
    return render_template('form.html')
