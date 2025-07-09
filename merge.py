# merge.py
import pandas as pd
import glob

# Find all genre CSV files
csv_files = glob.glob("imdb_movies_*_2024.csv")
print(f"📦 Found files: {csv_files}")

merged_df = pd.DataFrame()

for file in csv_files:
    df = pd.read_csv(file)
    merged_df = pd.concat([merged_df, df], ignore_index=True)

# Merge genres: group by Movie Name, combine genre names
final_df = (
    merged_df.groupby(['Movie Name', 'Rating', 'Voting Counts', 'Duration'], dropna=False)
    .agg({'Genre': lambda x: ', '.join(sorted(set(x)))})
    .reset_index()
)

print(f"✅ Total unique movies after merging: {len(final_df)}")

# Save merged dataset
final_df.to_csv("imdb_movies_merged_2024.csv", index=False)
print("💾 Saved merged data to imdb_movies_merged_2024.csv")
