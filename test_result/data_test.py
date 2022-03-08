import pandas

song_df = pandas.read_csv('songdata.csv', usecols=[
                          "song_id", "artist_id", "name", "title", "duration"])
log_df = pandas.read_csv('logdata.csv', usecols=["name", "title", "duration"])

songdata = []
logdata = []

for index, row in song_df.iterrows():
    songdata.append((row['name'], row['title'], row['duration']))

for index, row in log_df.iterrows():
    logdata.append((row['name'], row['title'], row['duration']))


def check(t1, t2):
    return list(map(lambda x, y: x == y, t1, t2))


result = []
other_result = []
for song_row in songdata:
    for log_row in logdata:
        check_value = check(song_row, log_row)
        if all(check_value):
            result.append(song_row)
        if any(check_value):
            other_result.append(
                {"result": check_value, "song": song_row, "log": log_row})


with open('test_result.txt', "w") as f:
    for index, row in enumerate(other_result):
        f.write(str(row) + "\n")

f.close()

print("Result:\nIndex\tMatching data\n")
for index, res in enumerate(result):
    print("{}\t{}\n".format(index + 1, res))

