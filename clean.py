# clean.py
import pandas as pd

# Load the merged CSV
df = pd.read_csv("./data/imdb_movies_merged_2024.csv")
print(f"📦 Loaded merged data: {len(df)} rows")
print("Columns:", df.columns.tolist())

# Remove leading numbers, dot and space from 'Movie Name' column
df['Movie Name'] = df['Movie Name'].str.replace(r'^\d+\.\s*', '', regex=True)

# Optional: preview cleaned titles
print(df['Movie Name'].head())

# Save to new cleaned CSV
df.to_csv("./data/imdb_movies_cleaned_2024.csv", index=False)
print("✅ Saved cleaned data to ./data/imdb_movies_cleaned_2024.csv")
