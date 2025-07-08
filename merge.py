import pandas as pd
import glob

# Step 1: Load all CSVs
csv_files = glob.glob('imdb_movies_*_2024.csv')
print(f"🗂 Found {len(csv_files)} CSV files to merge: {csv_files}")

all_dfs = []
for file in csv_files:
    df = pd.read_csv(file)
    all_dfs.append(df)

# Step 2: Concatenate
merged_df = pd.concat(all_dfs, ignore_index=True)

# Step 3: Group by Movie Name and combine genres
merged_df = merged_df.groupby(
    ['Movie Name', 'Rating', 'Voting Counts', 'Duration'],
    as_index=False
).agg({'Genre': lambda x: ', '.join(sorted(set(x)))})

# Step 4: Save merged file
merged_df.to_csv('imdb_movies_merged_2024.csv', index=False)
print(f"✅ Merged dataset saved to imdb_movies_merged_2024.csv with {len(merged_df)} unique movies")

# Optional: view first few rows
print(merged_df.head())
