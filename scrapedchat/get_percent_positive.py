import csv

with open("1_results.csv", 'r', encoding='utf8') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        streamer = row[0]
        positive = int(row[3])
        negative = int(row[4])
        result = (positive/(positive+negative))
        print(streamer)
        print(result)
        print("____")

# 