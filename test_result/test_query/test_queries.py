"""
    Get the list of cities which have most paid users (for business strategies)
"""

query_1 = ("""
    SELECT location AS city, COUNT(location) AS listener_count 
    FROM songplays 
    WHERE level = 'paid' 
    GROUP BY city 
    ORDER by listener_count DESC 
""")

"""
    Get the average play per city
"""
query_2 = ("""
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
""")

queries = [query_1, query_2]