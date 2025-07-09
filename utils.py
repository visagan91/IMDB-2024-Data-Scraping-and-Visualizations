from dotenv import load_dotenv
import os
from urllib.parse import quote_plus
from sqlalchemy import create_engine

def get_engine():
    load_dotenv()

    DB_USER = os.getenv("MYSQL_USER")
    DB_PASSWORD = quote_plus(os.getenv("MYSQL_PASSWORD"))
    DB_HOST = os.getenv("MYSQL_HOST")
    DB_PORT = os.getenv("MYSQL_PORT")
    DB_NAME = os.getenv("MYSQL_DB")

    DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    print(f"Connecting to DB: {DATABASE_URL}")  # optional for debug

    return create_engine(DATABASE_URL)
