import streamlit as st
import pandas as pd
import plotly.express as px
from utils import get_engine

st.set_page_config(page_title="🎬 IMDB Movies Dashboard", layout="wide")

st.title("🎥 IMDB Movies 2024 Dashboard")

# Connect to DB and load data
engine = get_engine()
df = pd.read_sql_table("movies_2024", con=engine)

# Convert columns to numeric (important!)
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
df['Voting Counts'] = pd.to_numeric(df['Voting Counts'], errors='coerce')
df['Duration'] = pd.to_numeric(df['Duration'], errors='coerce')

# Sidebar filters
st.sidebar.header("📊 Filters")

min_duration = st.sidebar.slider("Duration (Hours)", 0, int(df['Duration'].max()), (0, int(df['Duration'].max())))
min_rating = st.sidebar.slider("Minimum Rating", 0.0, 10.0, 0.0, step=0.1)
min_votes = st.sidebar.number_input("Minimum Voting Counts", min_value=0, value=0)
genres = st.sidebar.multiselect("Genres", df['Genre'].unique(), default=list(df['Genre'].unique()))

# Apply filters
filtered_df = df[
    (df['Duration'] >= min_duration[0]) & (df['Duration'] <= min_duration[1]) &
    (df['Rating'] >= min_rating) &
    (df['Voting Counts'] >= min_votes) &
    (df['Genre'].isin(genres))
]

# Display filtered data
st.subheader("🎬 Filtered Movies")
st.dataframe(filtered_df)

# Top 10 Movies by Rating and Voting Counts
st.subheader("🏆 Top 10 Movies by Rating & Voting Counts")
top_movies = filtered_df.sort_values(by=['Rating', 'Voting Counts'], ascending=[False, False]).head(10)
st.dataframe(top_movies)

# Genre Distribution
st.subheader("📊 Genre Distribution")
genre_counts = filtered_df['Genre'].value_counts().reset_index()
genre_counts.columns = ['Genre', 'Count']

fig1 = px.bar(genre_counts,
              x='Genre', y='Count',
              labels={'Genre': 'Genre', 'Count': 'Number of Movies'})

st.plotly_chart(fig1, use_container_width=True)

# Average Duration by Genre
st.subheader("⏱️ Average Duration by Genre")
avg_duration = filtered_df.groupby('Genre')['Duration'].mean().reset_index()
fig2 = px.bar(avg_duration, y='Genre', x='Duration', orientation='h')
st.plotly_chart(fig2, use_container_width=True)

# Voting Trends by Genre
st.subheader("🗳️ Average Voting Counts by Genre")
avg_votes = filtered_df.groupby('Genre')['Voting Counts'].mean().reset_index()
fig3 = px.bar(avg_votes, x='Genre', y='Voting Counts')
st.plotly_chart(fig3, use_container_width=True)

# Rating Distribution
st.subheader("⭐ Rating Distribution")
fig4 = px.histogram(filtered_df, x='Rating')
st.plotly_chart(fig4, use_container_width=True)

# Genre-Based Rating Leaders
st.subheader("🏅 Top Rated Movie per Genre")
top_per_genre = filtered_df.sort_values('Rating', ascending=False).drop_duplicates('Genre')
st.dataframe(top_per_genre[['Genre', 'Movie Name', 'Rating']])

# Most Popular Genres by Voting
st.subheader("🔥 Most Popular Genres by Voting Counts")
votes_by_genre = filtered_df.groupby('Genre')['Voting Counts'].sum().reset_index()
fig5 = px.pie(votes_by_genre, names='Genre', values='Voting Counts')
st.plotly_chart(fig5, use_container_width=True)

# Duration Extremes
st.subheader("🎬 Duration Extremes")
shortest = filtered_df.nsmallest(1, 'Duration')
longest = filtered_df.nlargest(1, 'Duration')
st.write("Shortest Movie:")
st.dataframe(shortest[['Movie Name', 'Duration']])
st.write("Longest Movie:")
st.dataframe(longest[['Movie Name', 'Duration']])

# Ratings by Genre (Heatmap)
st.subheader("📊 Average Ratings by Genre (Heatmap)")
ratings_by_genre = filtered_df.groupby('Genre')['Rating'].mean().reset_index()
fig6 = px.density_heatmap(ratings_by_genre, x='Genre', y='Rating')
st.plotly_chart(fig6, use_container_width=True)

# Correlation Analysis
st.subheader("📈 Correlation between Ratings and Voting Counts")
fig7 = px.scatter(filtered_df, x='Rating', y='Voting Counts', size='Duration', color='Genre',
                  hover_data=['Movie Name'])
st.plotly_chart(fig7, use_container_width=True)
