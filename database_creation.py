import sqlite3
import pandas as pd

# Load merged CSV
df = pd.read_csv('imdb_movies_merged_2024.csv')
print(f"✅ Loaded merged data: {len(df)} rows")

# Connect to SQLite (creates file if not exists)
conn = sqlite3.connect('imdb_movies.db')

# Store DataFrame as table named 'movies_2024'
df.to_sql('movies_2024', conn, if_exists='replace', index=False)
print("📦 Saved to database table: movies_2024")

# Verify by running a simple query
result = pd.read_sql_query("SELECT * FROM movies_2024 LIMIT 5", conn)
print("\n🔍 Sample from database:")
print(result)

conn.close()
print("✅ Done. Database saved as imdb_movies.db")
