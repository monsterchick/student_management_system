from flask import Flask, render_template, redirect, request
from database_operator import Operator




app = Flask(__name__)
@app.route('/')
def Welcome():  # put application's code here
    return 'Welcome to Student Management System!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    operator = Operator()
    if request.method=='POST':
        # information for registering account
        username = request.form.get('username')
        password = request.form.get('password')
        # print(username, password)
        operator.search(inp_usr=username, inp_psw=password)

    return render_template('login.html')

@app.route('/signup',methods=['GET','POST'])
def signup():
    operator = Operator()
    if request.method=='POST':
        # while True:
        # information for registering account
        username = request.form.get('username')
        password = request.form.get('password')
        verification = request.form.get('verification')
        email = request.form.get('email')
        # print(username, email, password, verification)
        if (password == verification) & (len(username) <= 20):
            operator.add(inp_usr=username, inp_psw=password, inp_email=email)
            return redirect('/login')
        else:
            print('something wrong! try again.')

    return render_template('signup.html')

@app.route('/manage_panel')
def panel():
    return render_template('manage_panel.html')
if __name__ == '__main__':
    app.run()
