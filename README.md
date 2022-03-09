
# SPARKIFY ETL Pipeline

## Project description

A startup named Sparkify released their music streaming app not long ago, and they now want to analyze the data they have been collecting on songs and user activity. Their main goal is an insight to what their users are listening to, however they cannot find an easy way to query those data. Therefore, they brought me in, an data engineer, in order to create a Postgre database with tables for optiziming the queries on song play analysis.

In this project, I've implemented an ETL pipeline using Python to process the data from the 2 sources: song data and log data, under the format of *[JSON](https://en.wikipedia.org/wiki/JSON)* files.

## How to run the project
- Prequisite
   - Have *[newest Python](https://www.python.org/)* (or at least 3.7) installed in your system (you can download it *[here](https://www.python.org/downloads/)*)
   - Install psycogs2 and pandas libraries of Python
   - Have a local instance of *[PostgreSQL](https://www.postgresql.org/)* database 
   - Being able to use Jupyter Notebook
- Steps:
  - Open the folder `source`
  - Open terminal in that folder
  - Run `python create_tables.py`
  - Run `python etl.py`
- Optional steps:
  - Open the folder `source`
  - Open `test_query`
  - Run `python test.py`
  - Open `test_query_1.csv` and `test_query_2.csv` to see the results

> Run python `create_tables.py` first of all. If you are running .ipynb files and want to drop and create tables again, you have to close the connection to the database since `create_tables.py` doesn't allow other connections to interfere.

## Sources

`sql_queries.py`: contain all the query commands used in `create_tables.py` and `etl.py` 
`create_tables.py`: contain all the scripts used to drop and create tables
`etl.py`: contains all the scripts for extracting - transforming - loading data into the database
`etl.ipynb`: guidance on ETL pipelining
`test.ipynb`: initially used to make the code foolproof

> **Note**: Other `.py` files are for **debugging** purposes and completely **optional**

## Database schema design

Regarding the choice of schema, I chose the *[Star schema](https://en.wikipedia.org/wiki/Star_schema)* due to the fact that I want my queries to be simplier with fewer JOIN operations. Furthermore, aggregation can also benefit from it which might help Sparkify's analysts a lot.

There lies the `songplay` fact table in the center of the schema surrounded by 4 dimension tables: `users`, `time`, `artists` and `songs`. Each of the 4 has its primary key acting as the foreign keys of `songplays`. Furthermore, there is the foreign key `artist_id` in relation `songs` which references the primary key of relation `artists`, this forms a star-like schema, just like its name.


![Sparkify Database Schema](/schema/schema.png "Sparkify Database Schema")

This kind of schema allows the analysts to easily query the data directly from the `songplays` table, and for ad-hoc queries (queries that cannot be determined prior to the moment the query is issued), they simply just perform `JOIN` and some optional aggregation functions.

## ETL Pipeline
### Data type
Here is a sample of 2 kinds of data that this database will perform ETL on, you can take a peek if you are interested as they are located in the subfolder `data` in `sources`

```
{
   data/song_data/../../*.json
   {
      "num_songs": 1,
      "artist_id": "ARJIE2Y1187B994AB7", 
      "artist_latitude": null, 
      "artist_longitude": null, 
      "artist_location": "", 
      "artist_name": "Line Renaud", 
      "song_id": "SOUPIRU12A6D4FA1E1", 
      "title": "Der Kleine Dompfaff", 
      "duration": 152.92036, 
      "year": 0
   }
   ...
   data/log_data/../../*.json
   {
      {
         "artist":"N.E.R.D. FEATURING MALICE",
         "auth":"Logged In",
         "firstName":"Jayden",
         "gender":"M",
         "itemInSession":0,
         "lastName":"Fox",
         "length":288.9922,
         "level":"free",
         "location":"New Orleans-Metairie, LA",
         "method":"PUT",
         "page":"NextSong",
         "registration":1541033612796.0,
         "sessionId":184,
         "song":"Am I High (Feat. Malice)",
         "status":200,
         "ts":1541121934796,
         "userAgent":"\"Mozilla\/5.0 (Windows NT 6.3; WOW64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/36.0.1985.143 Safari\/537.36\"",
         "userId":"101"
      }
   }
}
```

### The ETL process:
  - Get all the filepaths in a directory using `os.walk` with the constraint of getting only JSON files and process them:
```
   def process_data(cur, conn, filepath, func):
      # get all files matching extension from directory
      all_files = []
      ... # -> put into all_files
      
      print('{} files found in {}'.format(num_files, filepath))
      # iterate over files and process
      for i, datafile in enumerate(all_files, 1):
         func(cur, datafile) # -> process function
         conn.commit()
         print('{}/{} files processed.'.format(i, num_files))
```
   - Perform transforming & loading data into the database:
```
def process_song_file(cur, filepath):
   # open file
   df = pd.read_json(filepath, lines=True)
   
   # insert artist record
   artist_data = ...
   cur.execute(artist_table_insert, artist_data) # -> loading artistdata into database
   
   # insert song record
   song_data = ...
   cur.execute(song_table_insert, song_data) # -> loading songdata into database
    

def process_log_file(cur, filepath):
   # open file
   df = pd.read_json(filepath, lines=True)

   # filter by NextSong action
   df = ... # -> transforming (data cleaning)

   time_df = ...
   ...

   for i, row in time_df.iterrows():
      cur.execute(time_table_insert, list(row)) # -> loading timedata into database

   # load user table
   user_df = ...

   # insert user records
   for i, row in user_df.iterrows():
      cur.execute(user_table_insert, row) # -> loading userdata into database

   # insert songplay records
   for index, row in df.iterrows():

      ...
      if results:
         songid, artistid = results
         # print("result found: {} vs {}".format(results, row))
      else:
         songid, artistid = None, None
      ...
      cur.execute(songplay_table_insert, songplay_data) # -> loading songplaydata into database
```
## Example queries

1) Get the list of cities which have most **paid** users (for business strategies)

```
   SELECT location AS city, COUNT(location) AS listener_count 
      FROM songplays 
      WHERE level = 'paid' 
      GROUP BY city 
      ORDER by listener_count DESC 
```

<img src="/test_result/test_query/test_query-1.png" width="300" height="450"/>

2) From the results of the query above, let's find the average play per city

```
    SELECT (query_2.total_play / query_2.number_of_city) AS avg_play_each_city 
    FROM (
        SELECT SUM(query_1.listener_count) AS total_play, COUNT(city) AS number_of_city FROM (
            SELECT location AS city, COUNT(location) AS listener_count 
            FROM songplays 
            WHERE level = 'paid' 
            GROUP BY city 
            ORDER by listener_count DESC
            ) query_1
        ) query_2
```
<img src="/test_result/test_query/test_query-2.png" width="200" height="60"/>

