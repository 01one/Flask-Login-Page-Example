from flask import Flask, render_template, request, redirect, session
from datetime import timedelta

import secrets


app = Flask(__name__)
app.secret_key =secrets.token_urlsafe(32) 
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=3)


@app.route('/')
def index():
	if session.get('logged_in'):
		return 'You are Already Logged in'
	else:
		return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username == 'username' and password == 'password':
        session['logged_in'] = True
        session.permanent = True
        return redirect('/user')
    else:
        return redirect('/')

@app.route('/user')
def user():
    if session.get('logged_in'):
        return 'Login Successful'
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)







