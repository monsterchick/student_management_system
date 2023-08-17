import os
import dotenv
import mysql.connector

dotenv.load_dotenv()

# connect to database server
connect = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USERNAME'),
    password=os.getenv('DB_PASSWORD'),
    database=os.getenv('DB_NAME')
)
print('database connected successfully!')

# create Cursor object to operate database
cursor = connect.cursor()
cursor.execute('INSERT INTO product(id, name, price) values(11, "dog", 33);')

# confirm to execute sql code
connect.commit()

# close database connection
connect.close()
