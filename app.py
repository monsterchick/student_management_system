from flask import Flask, render_template, request, redirect
from student_data import students

app = Flask(__name__)


@app.route('/')
def welcome():
    '''welcome page'''
    return 'Welcome to Student Management System!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    '''login page'''
    # get username and password from user
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # print(username, password)
        return redirect('/admin')  # should connect to database and validate the username and password
    return render_template('login.html')


@app.route('/admin')
def admin():
    '''management panel'''
    return render_template('admin.html', students=students)


@app.route('/add', methods=['GET', 'POST'])
def add():
    '''adds new student's data'''
    if request.method == 'POST':
        # infomation that user enter
        name = request.form.get('name')
        course = request.form.get('course')
        mobile = request.form.get('mobile')
        age = request.form.get('age')

        # put the information into database
        students.append({'name': name, 'course': course, 'mobile': mobile, 'age': age})

        return redirect('/admin')
    return render_template('add.html')


@app.route('/delete', methods=['GET'])
# removes student's data
def delete():
    '''deletes student's record'''
    if request.method == 'GET':
        # parameter from html
        name_to_delete = request.args.get('name')

        for stu in students:
            if stu['name'] == name_to_delete:
                students.remove(stu)

    return redirect('/admin')


@app.route('/modify', methods=['GET', 'POST'])
def change():
    '''modifies student's data'''

    # values that user wants it to be
    name_to_changed = request.form.get('name')
    course_to_changed = request.form.get('course')
    mobile_to_changed = request.form.get('mobile')
    age_to_changed = request.form.get('age')

    # the name of the student whose information is been being modifying
    name = request.args.get('name')

    if request.method == 'POST':
        for stu in students:
            # modifies student's information
            if stu['name'] == name:
                stu['name'] = name_to_changed
                stu['course'] = course_to_changed
                stu['mobile'] = mobile_to_changed
                stu['age'] = age_to_changed

        # return to admin page after modifying
        return redirect('/admin')


    for stu in students:
        if stu['name'] == name:
            # delivers original student's information and shows on input box
            return render_template('modify.html', student=stu)


if __name__ == '__main__':
    app.run()
