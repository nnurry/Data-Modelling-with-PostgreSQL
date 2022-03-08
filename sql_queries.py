# DROP TABLES

songplay_table_drop = "DROP table IF EXISTS songplays"
user_table_drop = "DROP table IF EXISTS users"
song_table_drop = "DROP table IF EXISTS songs"
artist_table_drop = "DROP table IF EXISTS artists"
time_table_drop = "DROP table IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
            songplay_id SERIAL PRIMARY KEY, 
            start_time timestamp NOT NULL,
            user_id integer NOT NULL, 
            level varchar NOT NULL, 
            song_id varchar, 
            artist_id varchar, 
            session_id varchar, 
            location varchar, 
            user_agent varchar
        );
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
            user_id integer PRIMARY KEY, 
            first_name varchar NOT NULL, 
            last_name varchar NOT NULL, 
            gender varchar NOT NULL, 
            level varchar NOT NULL
        );
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
            song_id varchar PRIMARY KEY, 
            title varchar NOT NULL, 
            artist_id varchar NOT NULL, 
            year integer, 
            duration numeric NOT NULL
        );
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
            artist_id varchar PRIMARY KEY, 
            name varchar NOT NULL, 
            location varchar, 
            latitude double precision, 
            longitude double precision
        );
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
            start_time timestamp PRIMARY KEY, 
            hour integer, 
            day integer, 
            week integer, 
            month integer, 
            year integer, 
            weekday integer
        );
""")

log_table_create = ("""
    CREATE TABLE IF NOT EXISTS logs (
            artist_name varchar,
            auth varchar,
            firstName varchar,
            gender varchar,
            itemInSession integer,
            lastName varchar,
            length numeric,
            level varchar,
            location varchar,
            method varchar,
            page varchar,
            registration numeric,
            sessionId varchar,
            song varchar,
            status integer,
            ts bigint,
            userAgent varchar,
            userId varchar
    )
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays (
            start_time,
            user_id, 
            level, 
            song_id, 
            artist_id, 
            session_id, 
            location, 
            user_agent
        ) VALUES (to_timestamp(%s / 1000.0),%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING;
""")

user_table_insert = ("""
    INSERT INTO users (
            user_id, 
            first_name, 
            last_name, 
            gender, 
            level
        ) VALUES (%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING;
""")

song_table_insert = ("""
    INSERT INTO songs (
            song_id, 
            title, 
            artist_id, 
            year, 
            duration
        ) VALUES (%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING;
""")

artist_table_insert = ("""
    INSERT INTO artists (
            artist_id, 
            name, 
            location, 
            latitude, 
            longitude
        ) VALUES (%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING;
""")


time_table_insert = ("""
    INSERT INTO time (
            start_time, 
            hour, 
            day, 
            week, 
            month, 
            year, 
            weekday
        ) VALUES (to_timestamp(%s / 1000.0),%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING;
""")

log_table_insert = ("""
    INSERT INTO logs (
            artist_name,
            auth,
            firstName,
            gender,
            itemInSession,
            lastName,
            length,
            level,
            location,
            method,
            page,
            registration,
            sessionId,
            song,
            status,
            ts,
            userAgent,
            userId
        ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING;
""")

# FIND SONGS

song_select = ("""
    SELECT songs.song_id, artists.artist_id
        FROM (songs JOIN artists ON songs.artist_id = artists.artist_id)
        WHERE title = %s AND name = %s AND duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create,
                        song_table_create, artist_table_create, time_table_create, log_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop,
                      song_table_drop, artist_table_drop, time_table_drop]
