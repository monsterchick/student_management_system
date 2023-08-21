import os
from dotenv import load_dotenv
import sqlalchemy as db
from sqlalchemy import create_engine
load_dotenv()




def sqlachemy():
    url = os.getenv('DB_HOST')
    engine = create_engine(url)
    connection = engine.connect()
    metadata = db.MetaData()
    table = db.Table('area_code', metadata, autoload=True, autoload_with=engine)

    query = db.insert(table).table(code=10000, name="HK")
    connection.execute(query)
    return
