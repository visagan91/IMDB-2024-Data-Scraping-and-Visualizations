# database_creation.py
import pandas as pd
from utils import get_engine

engine = get_engine()

# Load cleaned CSV
df = pd.read_csv("./data/imdb_movies_cleaned_2024.csv")
print(f"📦 Loaded cleaned data: {len(df)} rows")
print("Columns and types:")
print(df.dtypes)

# Optional: ensure correct types (can help)
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
df['Voting Counts'] = pd.to_numeric(df['Voting Counts'], errors='coerce')
df['Duration'] = pd.to_numeric(df['Duration'], errors='coerce')

# Write to database
df.to_sql("movies_2024", con=engine, if_exists="replace", index=False)
print("✅ Data successfully written to database!")
