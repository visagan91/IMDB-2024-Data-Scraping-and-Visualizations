

from sqlalchemy import create_engine, text

# Replace these with your credentials
user = "root"
password = "yourpassword"  # if you haven’t set a password yet, just use ""
host = "127.0.0.1"         # use IP address, NOT localhost or socket
port = 3306

# Step 1: Connect to MySQL server itself (not to a specific DB yet)
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}")

with engine.connect() as conn:
    # Step 2: Create the database if it doesn't exist
    conn.execute(text("CREATE DATABASE IF NOT EXISTS imdb_db"))
    print("✅ Database 'imdb_db' created or already exists")


# Store data into table 'movies_2024'
df.to_sql("movies_2024", con=engine, if_exists="replace", index=False)

print("✅ Data successfully stored into MySQL database (table: movies_2024)")


conn.close()
print("✅ Done. Database saved as imdb_movies.db")
