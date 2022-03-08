
# SPARKIFY ETL Pipeline

## Project description

A startup named Sparkify released their music streaming app not long ago, and they now want to analyze the data they have been collecting on songs and user activity. Their main goal is an insight to what their users are listening to, however they cannot find an easy way to query those data. Therefore, they brought me in, an data engineer, in order to create a Postgre database with tables for optiziming the queries on song play analysis.

In this project, I've implemented an ETL pipeline using Python to process the data from the 2 sources: song data and log data, under the format of *[JSON](https://en.wikipedia.org/wiki/JSON)* files.

## How to run the project
- Prequisite
   - Have *[Python 3](https://www.python.org/)* installed in your system (you can download it *[here](https://www.python.org/downloads/)*)
   - Install psycogs2 and pandas libraries of Python
   - Have a local instance of *[PostgreSQL](https://www.postgresql.org/)* database 
- Run these following scripts:
`python create_tables.py`
`python etl.py`

## Sources
`sql_queries.py`: contain all the query commands used in `create_tables.py` and `etl.py` 
`create_tables.py`: 
`etl.py`:
`test.ipynb`: use this to

## Database schema design

Regarding the choice of schema, I chose the *[Star schema](https://en.wikipedia.org/wiki/Star_schema)* due to the fact that I want my queries to be simplier with fewer JOIN operations. Furthermore, aggregation can also benefit from it which might help Sparkify's analysts a lot.


Do the following steps in your README.md file.
Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.
How to run the Python scripts
An explanation of the files in the repository
State and justify your database schema design and ETL pipeline.
[Optional] Provide example queries and results for song play analysis.
Here's a https://www.markdownguide.org/basic-syntax/guide on Markdown Syntax.*
Provide DOCSTRING statement in each function implementation to describe what each function does.