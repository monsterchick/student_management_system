from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def Welcome():  # put application's code here
    return 'Welcome to Student Management System!'

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/manage_panel')
def panel():
    return render_template('manage_panel.html')
if __name__ == '__main__':
    app.run()
