import os
import dotenv
import mysql.connector

# load the private data for login to mysql server
dotenv.load_dotenv()

class Operator:
    def __init__(self):
        # connect to database server
        try:
            self.connect = mysql.connector.connect(
                host=os.getenv('DB_HOST'),
                user=os.getenv('DB_USERNAME'),
                password=os.getenv('DB_PASSWORD'),
                database=os.getenv('DB_NAME')
            )
            # if the connection is successful, prompt it
            if self.connect.is_connected() == True:
                print('database connected successfully!')

            # create Cursor object to operate database
            self.cursor = self.connect.cursor()

        except mysql.connector.errors.ProgrammingError as err:
            # if the connection is wrong, prompt the issue
            print('failed to connect since wrong with: \n{}. \nPlease check you infomation correct.'.format(err))

    def add(self, inp_usr, inp_psw, inp_email):
        # add new data
        self.cursor.execute("INSERT INTO tbl_manager(mUsername, mPassword, mEmail) values('{}', '{}', '{}');".format(inp_usr, inp_psw, inp_email))
        # print(inp_usr, inp_psw, inp_email)

        # confirm to execute sql code
        self.connect.commit()

        # close database connection
        self.connect.close()
        self.cursor.close()
    def remove(self, mId):
        # connect to database server
        try:
            connect = mysql.connector.connect(
                host=os.getenv('DB_HOST'),
                user=os.getenv('DB_USERNAME'),
                password=os.getenv('DB_PASSWORD'),
                database=os.getenv('DB_NAME')
            )
            # if the connection is successful, prompt it
            if connect.is_connected() == True:
                print('database connected successfully!')

            # create Cursor object to operate database
            cursor = connect.cursor()
            cursor.execute('INSERT INTO product(id, username, password, email) values(11, "dog", 33);')

            # confirm to execute sql code
            connect.commit()

            # close database connection
            connect.close()
        except mysql.connector.errors.ProgrammingError as err:
            # if the connection is wrong, prompt the issue
            print('failed to connect since wrong with: \n{}. \nPlease check you infomation correct.'.format(err))
    def update(self, mId):
        # connect to database server
        try:
            connect = mysql.connector.connect(
                host=os.getenv('DB_HOST'),
                user=os.getenv('DB_USERNAME'),
                password=os.getenv('DB_PASSWORD'),
                database=os.getenv('DB_NAME')
            )
            # if the connection is successful, prompt it
            if connect.is_connected() == True:
                print('database connected successfully!')

            # create Cursor object to operate database
            cursor = connect.cursor()
            cursor.execute('INSERT INTO product(id, username, password, email) values(11, "dog", 33);')

            # confirm to execute sql code
            connect.commit()

            # close database connection
            connect.close()
        except mysql.connector.errors.ProgrammingError as err:
            # if the connection is wrong, prompt the issue
            print('failed to connect since wrong with: \n{}. \nPlease check you infomation correct.'.format(err))
    def search(self):
        pass
    def login_verification(self, inp_usr, inp_psw):
        try:
            self.cursor.execute("SELECT * FROM tbl_manager WHERE mUsername='{}' AND mPassword={};".format(inp_usr, inp_psw))

            # data from database
            # row = self.cursor.fetchone()
            # db_username = row[1]
            # db_password = row[2]
            # print('from db:', db_username, db_password)

            # confirm to execute sql code
            self.connect.commit()

            # close database connection
            self.cursor.close()
            self.connect.close()
            return True

        except:
            print('fail to log in since. Couldn\' find username and password not match to database.')

def test():
    operator = Operator()
    operator.add('usss', 'passs', 'emmmm')

if __name__ == '__main__':
    test()





