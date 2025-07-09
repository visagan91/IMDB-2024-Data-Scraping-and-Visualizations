import pandas as pd
from utils import get_engine

engine = get_engine()

df = pd.read_csv("./data/imdb_movies_cleaned_2024.csv")
print(f"📦 Loaded merged data: {len(df)} rows")

df.to_sql("movies_2024", con=engine, if_exists="replace", index=False)
print("✅ Data successfully written to database!")
