from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Setup Chrome in headless mode
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Comment out if you want to see the browser

# Initialize driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# IMDb URL
url = 'https://www.imdb.com/search/title/?title_type=feature&release_date=2024-01-01,2024-12-31'
driver.get(url)

time.sleep(3)  # wait for page to load; adjust as needed

# Lists to store data
movie_names = []
genres = []
ratings = []
votes = []
durations = []

# Find all movie containers
movies = driver.find_elements(By.CSS_SELECTOR, '.lister-item.mode-advanced')

for movie in movies:
    # Movie name
    try:
        name = movie.find_element(By.CSS_SELECTOR, 'h3.lister-item-header a').text
    except:
        name = ''
    movie_names.append(name)

    # Genre
    try:
        genre = movie.find_element(By.CSS_SELECTOR, '.genre').text.strip()
    except:
        genre = ''
    genres.append(genre)

    # Rating
    try:
        rating = movie.find_element(By.CSS_SELECTOR, '.ratings-imdb-rating strong').text
    except:
        rating = ''
    ratings.append(rating)

    # Votes
    try:
        vote = movie.find_element(By.CSS_SELECTOR, 'p.sort-num_votes-visible span[name="nv"]').text
    except:
        vote = ''
    votes.append(vote)

    # Duration
    try:
        duration = movie.find_element(By.CSS_SELECTOR, '.runtime').text
    except:
        duration = ''
    durations.append(duration)

# Close driver
driver.quit()

# Create dataframe
df = pd.DataFrame({
    'Movie Name': movie_names,
    'Genre': genres,
    'Rating': ratings,
    'Voting Counts': votes,
    'Duration': durations
})

# Save to CSV
df.to_csv('imdb_movies_2024.csv', index=False)

print(df)
