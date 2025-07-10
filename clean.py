import pandas as pd
import re

# Load data
df = pd.read_csv("./data/imdb_movies_merged_2024.csv")
print(f"📦 Loaded merged data: {len(df)} rows")
print("Columns:", df.columns.tolist())

# Remove leading numbers in movie name
df['Movie Name'] = df['Movie Name'].str.replace(r'^\d+\.\s*', '', regex=True)

# Parse votes
def parse_votes(v):
    v = str(v).strip().upper()
    v = v.replace('(', '').replace(')', '').replace(',', '').strip()
    try:
        if 'K' in v:
            return float(v.replace('K','')) * 1_000
        elif 'M' in v:
            return float(v.replace('M','')) * 1_000_000
        else:
            return float(v)
    except:
        return None

df['Voting Counts'] = df['Voting Counts'].apply(parse_votes)

# Parse durations like '1h 58m' → total hours as float
def parse_duration(s):
    if pd.isna(s):
        return None
    s = str(s).lower()
    hours = 0
    minutes = 0
    h_match = re.search(r'(\d+)h', s)
    m_match = re.search(r'(\d+)m', s)
    if h_match:
        hours = int(h_match.group(1))
    if m_match:
        minutes = int(m_match.group(1))
    return hours + minutes / 60

df['Duration'] = df['Duration'].apply(parse_duration)

# Check after parsing
print("\n👉 Duration after parsing:")
print(df['Duration'].describe())
print(f"Missing: {df['Duration'].isna().sum()}")

# Fill missing durations with median
median_duration = df['Duration'].median()
df['Duration'] = df['Duration'].fillna(median_duration)
print(f"✅ Filled missing durations with median: {median_duration} hours")

# Convert to minutes (rounded)
df['Duration'] = (df['Duration'] * 60).round().astype('Int64')

# Explode genres
df['Genre List'] = df['Genre'].str.split(',')
df_exploded = df.explode('Genre List').copy()
df_exploded['Genre'] = df_exploded['Genre List'].str.strip()
df_exploded.drop(columns=['Genre List'], inplace=True)

# Reorder columns
df_exploded = df_exploded[['Movie Name', 'Rating', 'Voting Counts', 'Duration', 'Genre']]

print(f"✅ After cleaning & exploding: {len(df_exploded)} rows")
print("Preview:\n", df_exploded.head())

# Save
df_exploded.to_csv("./data/imdb_movies_cleaned_2024.csv", index=False)
print("✅ Saved cleaned data to ./data/imdb_movies_cleaned_2024.csv")
