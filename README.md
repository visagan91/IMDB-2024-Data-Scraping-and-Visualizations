# IMDB-2024-Data-Scraping-and-Visualizations


#Introduction:
The main objective of this project is to build a model to extract and analyse movie data for a particular year. The model has to effectively scrape down preferences from a webpage to be organised in the desired database for further analysis and visualisations. Adding along an attractive user interface for users to query and explore the dataset.


#Design:

1.Sraping:
The dataset is to be obtained from the IMDb 2024 Movies page through effective scrapping technique. The scrapping method used is Selenium in python. Scrapping of different genre is achieved by giving individual genre filtered URLs before the scrapping code and looped to scrap each genre into respective CSV files.

2.Data Storage:
Each CSV files are finally checked for NULL values and other metrics and then merged into a single data frame. The whole data frame is fed into a SQL database for querying and future analysis..

3.Data visualisation:
The dataset is analysed and filtered to visualise into simpler pictorial and graphic representation. The need of the business cases is understood and optimal ways to represent each case is analysed and identified for visualisation of the dataset. 

4.Interactive user tool:
A interactive streamlit application is also developed for user specific filtering and visualisation as desired. This helps in a user preferred analysis of the dataset for real-time scenarios.



#Workflow and challenges :

Scraping: 
 A python script scrapping.py in which selenium is used to scrape movies by genres. More metrics like rating, voting counts, durations are also scrapped. 
 Each scrapped data is stored in separate CSV files.
Challenges : The webpage displayed only 50 movies at once and had a 50more button at the end to load more. 
Strategy : Used a loop to load 50more and scrap until there is no 50more option.

Merging datasets:
 The python script merge.py is created to merge all the individual CSV files into s single file and keep all the relevant columns.
 Challenge : Few movies came under multiple genres 
 Strategy : Combines genres of the movies with multiple genres. 

Data cleaning :
 clean.py is scripted to clean and transform the dataset with our preferences before storing it into the database.  Challenges :
     1.Numeric prefixes in movie names
     2.Voting counts were in string (e.g. 1.4k, 2k)
     3.Duration values were in string (e.g, 2h 5m)
 Strategy:
     1.Leading numbers is removed using str.replace.
     2.Voting counts is parsed to give 1000 for k and 10000 for M. (e.g, "1.4K" → 1400, "2M" → 2,000,000, etc."1.4K" → 1400, "2M" → 2,000,000, etc.)
     3.Duration is parsed such that the hours are given in minutes. “2h 25m” → float hours (e.g., 2.42).

Database creation:
 The final cleaned CSV file is saved into a sql database for further analysis and querying. 
Challenges : Connection to an SQL database through normal workbench environment.
Strategy : Connected to MySQL using SQLAlchemy and credentials from .env after installing MySQL extension in VS code.

Streamlit app:
 This interactive app loads data directly from the database with user preferred dashboard options and visualisations.
 Challenges : The visualisations and all other data was by default.
 Strategy : Approriate side bar filters were used to optimise user preferences. 



#Structure:
.
├── scrapping.py           # Scrapes IMDB for multiple genres and stores raw CSVs
├── merge.py              # Merges genre CSVs into a single dataset
├── clean.py              # Cleans and preprocesses data
├── database_creation.py  # Stores cleaned data into MySQL database
├── streamlit_app.py      # Interactive dashboard with filters and visualizations
├── utils.py              # Database connection utility
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (DB credentials)
└── data/                 # Directory for storing CSV files



#Design Highlights :

Modularity: Each script does a clear, single task.
Reproducibility: From scraping to visualization, you can re-run the full pipeline.
Data quality: Cleaned voting counts & duration.
Exploded genres: Movies show up under each genre with correct duration.
Interactivity: Streamlit filters + “Apply” button.
Scalability: Uses SQL DB for querying; data easily expandable.



#Libararies and tools used :

| Task              | Library/Tool                 |
| ----------------- | ---------------------------- |
| Scraping          | Selenium, webdriver\_manager |
| Data manipulation | Pandas                       |
| Database ORM      | SQLAlchemy, pymysql          |
| Environment vars  | python-dotenv                |
| Visualization     | Streamlit, Plotly            |



#Running strategy :

 Creating a environment
 python3 -m venv venv
 source venv/bin/activate
 pip install -r requirements.txt

 python scrapping.py
 python merge.py
 python clean.py
 python database_creation.py

 streamlit run streamlit_app.py



#Propsed enhancements :
1. A primary key can be introduced for better joins and relationship analysis along with row wise IDs.
2. Can obtain correlation data from the dataset we have for much more insights (e.g, ratings history, revenue data.)
3. Deployment of the app with a cloud-based interface platform.



#Conclusion:
This project demonstrates a complete data engineering pipeline that includes web scraping, ETL of data, data warehousing and visualisation. The code was developed with maximum preference to modularity, maintainability and scalability for future. This makes it a full-cycle data science and engineering solution that’s ready to be deployed and extended if needed. 
