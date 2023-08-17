from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def Welcome():  # put application's code here
    return 'Welcome to Student Management System!'

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method=='POST':
        # information for registering account
        username = request.form.get('username')
        password = request.form.get('password')
        verification = request.form.get('verification')
        email = request.form.get('email')
        # print(username, email, password, verification)
        if (password == verification) & (len(username) <= 20):
            print('=====')
        else:
            print('nnnnnnn')
        return redirect('/login')

    if request.method=='GET':
        print('getttt')


    return render_template('signup.html')

@app.route('/manage_panel')
def panel():
    return render_template('manage_panel.html')
if __name__ == '__main__':
    app.run()
