from flask import Flask, render_template, request, redirect, url_for, make_response
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
        first_name = request.values.get('first_name')
        last_name = request.values.get('last_name')
        response = make_response(redirect(url_for('registered')))
        response.set_cookie('first_name', 'John')
        return response
    return render_template('form.html')

@app.route('/thank_you')
def registered():
    first_name = request.cookies.get('first_name')
    return f'Thank you, {first_name}!'
