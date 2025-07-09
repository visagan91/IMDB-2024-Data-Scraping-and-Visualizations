import os
from sqlalchemy import create_engine, inspect
from dotenv import load_dotenv

# Load DB config
load_dotenv()
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
host = os.getenv("MYSQL_HOST")
port = os.getenv("MYSQL_PORT")
db = os.getenv("MYSQL_DB")

# Build DB URL
db_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
engine = create_engine(db_url)

# Check connection and list tables
with engine.connect() as conn:
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print(f"📊 Tables in database '{db}': {tables}")
