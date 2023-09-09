from flask import Flask, render_template, redirect, request
from database_operator import Operator

app = Flask(__name__)


@app.route('/')
def Welcome():
    '''
    welcome page
    '''
    return render_template('welcome.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''
    This checks if the input entered by user verifies manager's database
    '''
    operator = Operator()
    if request.method == 'POST':
        # information for registering account
        username = request.form.get('username')
        password = request.form.get('password')
        print(username, password)
        info_check = operator.login_verification(inp_usr=username, inp_psw=password)
        print(info_check)
        if info_check == True:
            return redirect('/home?user={}'.format(username))
        else:
            print('fail to log in. Please check your username or password.')
            prompt = 'Fail to log in. Try again!'
            return render_template('login.html', prompt=prompt)

    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    '''
    manager sign up page
    '''
    operator = Operator()
    if request.method == 'POST':
        # while True:
        # information for registering account
        username = request.form.get('username')
        password = request.form.get('password')
        verification = request.form.get('verification')
        email = request.form.get('email')
        print(username, email, password, verification)

        # sign up successfully
        if password == verification:
            operator.sign_up(inp_usr=username, inp_psw=password, inp_email=email)
            return redirect('/login')
        else:
            # sign up fail
            print('something wrong! try again.')

    return render_template('signup.html')


@app.route('/home')
def home():
    '''
    shows user's name and student management system
    '''
    user = request.args.get('user')
    print(user)
    return render_template('manage_panel.html', user=user)


@app.route('/forgot')
def forgot():
    '''
    to find the account missed and reset password
    '''
    return render_template('forgot.html')


if __name__ == '__main__':
    app.run()
