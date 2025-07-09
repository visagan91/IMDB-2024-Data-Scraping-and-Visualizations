from dotenv import load_dotenv
import os
from urllib.parse import quote_plus
from sqlalchemy import create_engine
import pandas as pd

load_dotenv()

DB_USER = os.getenv("MYSQL_USER")
DB_PASSWORD = quote_plus(os.getenv("MYSQL_PASSWORD"))
DB_HOST = os.getenv("MYSQL_HOST")
DB_PORT = os.getenv("MYSQL_PORT")
DB_NAME = os.getenv("MYSQL_DB")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
print(f"Connecting to DB: {DATABASE_URL}")  # optional for debug

engine = create_engine(DATABASE_URL)

df = pd.read_csv("./data/imdb_movies_merged_2024.csv")
print(f"📦 Loaded merged data: {len(df)} rows")

df.to_sql("movies_2024", con=engine, if_exists="replace", index=False)
print("✅ Data successfully written to database!")
