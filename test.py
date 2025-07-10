import pandas as pd
from utils import get_engine

engine = get_engine()

# Load full table
df = pd.read_sql_table("movies_2024", con=engine)
print("\n✅ Loaded table:")
print(df.head())
print("\nColumns:", df.columns)
print("\nShape:", df.shape)

# Convert numeric columns safely
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
df['Voting Counts'] = pd.to_numeric(df['Voting Counts'], errors='coerce')
df['Duration'] = pd.to_numeric(df['Duration'], errors='coerce')

print("\n✅ After type conversion:")
print(df.dtypes)

# 1️⃣ Top 10 Movies by Rating & Voting Counts
top_movies = df.sort_values(by=['Rating', 'Voting Counts'], ascending=[False, False]).head(10)
print("\n🏆 Top 10 Movies by Rating & Voting Counts:")
print(top_movies[['Movie Name', 'Rating', 'Voting Counts']])

# 2️⃣ Genre Distribution
genre_counts = df['Genre'].value_counts().reset_index()
genre_counts.columns = ['Genre', 'Count']
print("\n📊 Genre Distribution:")
print(genre_counts)

# 3️⃣ Average Duration by Genre
avg_duration = df.groupby('Genre')['Duration'].mean().reset_index()
print("\n⏱️ Average Duration by Genre:")
print(avg_duration)

# 4️⃣ Average Voting Counts by Genre
avg_votes = df.groupby('Genre')['Voting Counts'].mean().reset_index()
print("\n🗳️ Average Voting Counts by Genre:")
print(avg_votes)

# 5️⃣ Rating Distribution stats
print("\n⭐ Rating distribution:")
print(df['Rating'].describe())

# 6️⃣ Top rated movie per genre
top_per_genre = df.sort_values('Rating', ascending=False).drop_duplicates('Genre')
print("\n🏅 Top Rated Movie per Genre:")
print(top_per_genre[['Genre', 'Movie Name', 'Rating']])

# 7️⃣ Most Popular Genres by total Voting Counts
votes_by_genre = df.groupby('Genre')['Voting Counts'].sum().reset_index()
print("\n🔥 Most Popular Genres by Voting Counts:")
print(votes_by_genre)

# 8️⃣ Duration extremes
shortest = df.nsmallest(1, 'Duration')
longest = df.nlargest(1, 'Duration')
print("\n🎬 Shortest Movie:")
print(shortest[['Movie Name', 'Duration']])
print("\n🎬 Longest Movie:")
print(longest[['Movie Name', 'Duration']])

# 9️⃣ Ratings by Genre (average)
ratings_by_genre = df.groupby('Genre')['Rating'].mean().reset_index()
print("\n📊 Average Ratings by Genre:")
print(ratings_by_genre)

# 🔟 Correlation check
print("\n📈 Correlation between Ratings and Voting Counts:")
print(df[['Rating', 'Voting Counts']].corr())
