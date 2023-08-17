import os
import dotenv
import mysql.connector

# load the private data for login to mysql server
dotenv.load_dotenv()

# connect to database server
try:
    connect = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    if connect.is_connected() == True:
        print('database connected successfully!')

    # create Cursor object to operate database
    cursor = connect.cursor()
    cursor.execute('INSERT INTO product(id, name, price) values(11, "dog", 33);')

    # confirm to execute sql code
    connect.commit()

    # close database connection
    connect.close()
except mysql.connector.errors.ProgrammingError as err:
        print('failed to connect since wrong with: \n{}. \nPlease check you infomation correct.'.format(err))





