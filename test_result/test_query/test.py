import psycopg2
from test_queries import *
import csv

def test(cur, conn):
    for index, query in enumerate(queries):
        filename = "test_query_" + str(index + 1) + ".csv"
        f = open(filename, "w")
        writer = csv.writer(f)
        cur.execute(query)
        row = cur.fetchone()
        print("Result from query {}".format(index + 1))
        while row:
            writer.writerow(row)
            print(row, "\n")
            row = cur.fetchone()
        print("--------------------------------------")
        f.close()

def main():
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=sparkifydb user=student password=student"
    )
    cur = conn.cursor()
    test(cur, conn)
    conn.close()

if __name__ == "__main__":
    main()
