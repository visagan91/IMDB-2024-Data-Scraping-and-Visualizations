# IMDB-2024-Data-Scraping-and-Visualizations


Introduction:
The main objective of this project is to build a model to extract and analyse movie data for a particular year. The model has to effectively scrape down preferences from a webpage to be organised in the desired database for further analysis and visualisations. Adding along an attractive user interface for users to query and explore the dataset.


Design:

1.Sraping:
The dataset is to be obtained from the IMDb 2024 Movies page through effective scrapping technique. The scrapping method used is Selenium in python. Scrapping of different genre is achieved by giving individual genre filtered URLs before the scrapping code and looped to scrap each genre into respective CSV files.

2.Data Storage:
Each CSV files are finally checked for NULL values and other metrics and then merged into a single data frame. The whole data frame is fed into a SQL database for querying and future analysis..

3.Data visualisation:
The dataset is analysed and filtered to visualise into simpler pictorial and graphic representation. The need of the business cases is understood and optimal ways to represent each case is analysed and identified for visualisation of the dataset. 

4.Interactive user tool:
A interactive streamlit application is also developed for user specific filtering and visualisation as desired. This helps in a user preferred analysis of the dataset for real-time scenarios.



# Creating a environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
