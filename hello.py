from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)

app.secret_key = 'You Will Never Guess'

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
        session['first_name'] = first_name
        return redirect(url_for('registered'))
    return render_template('form.html')

@app.route('/thank_you')
def registered():
    first_name = session.get('first_name')
    return f'Thank you, {first_name}!'
