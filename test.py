import pandas as pd

# Load merged dataframe
df = pd.read_csv('imdb_movies_merged_with_multiple_genres_2024.csv')

print("🎬 DataFrame loaded successfully!\n")

# Show first few rows
print("👉 First 5 rows:")
print(df.head())

# Show basic shape and columns
print("\n✅ Shape:", df.shape)
print("\n📝 Columns and data types:")
print(df.dtypes)

# Check missing values
print("\n🔍 Missing values per column:")
print(df.isna().sum())

# See top 10 most common genre combinations
print("\n🎭 Top 10 genre combinations:")
print(df['Genre'].value_counts().head(10))

# Check how many movies have multiple genres (comma separated)
multiple_genres = df[df['Genre'].str.contains(',')]
print(f"\n📦 Movies with multiple genres: {len(multiple_genres)}")
print(multiple_genres.head())
