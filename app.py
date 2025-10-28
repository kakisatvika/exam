import flask
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('greeting.html', name="User")
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    number = request.form.get('number')
    age = request.form.get('age')
    return render_template('greeting.html', name=name, email=email, number=number, age=age)
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
