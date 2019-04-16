import csv

count = 0
with open("./training.1600000.processed.noemoticon.csv", 'r', encoding="ISO-8859-1") as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        if(count%94 == 0):
            if(row[0] == "0"):
                label = 'negative'
            if(row[0] == "4"):
                label = 'positive'
            with open('training_data.csv', mode='a' , newline='', encoding="utf-8") as csv_file:
                p_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                p_writer.writerow([label,row[5]])
        
        count = count + 1

csvFile.close()