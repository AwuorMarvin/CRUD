from flask import render_template
from app import app

@app.route('/')
def index():
    # return render_template('index.html')
    return render_template('index.html')
    # return 'hello from the other side'

@app.route('/login')
def login():
    # return render_template('index.html')
    return render_template('login.html')
    # return 'hello from the other side'
    