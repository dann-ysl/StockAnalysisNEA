import os
import csv
import datetime as dt


filename = "recordCache/test.csv"



def check():
    if os.path.exists(filename):
        lastDate = []
    with open(filename, "r", newline = "") as readfile:
        reader = csv.reader(readfile)
        for row in reader:
            lastDate.append(row)
    
    print (lastDate)

    if lastDate[0] != dt.date.today():
        #os.remove(filename)
        with open(filename, "w", newline = "") as writefile:
            writer = csv.writer(writefile)
            writer.writerow([dt.date.today()])

    else:#will never be executed once the file has been created
        with open(filename, "w", newline = "") as writefile:
            writer = csv.writer(writefile)
            writer.writerow([dt.date.today()])

header = ["stock","location","close"]

data = [["TSLA","TSLA.png","420.50"],
        ["AAPL","AAPL.png","354.34"],
        ["MSFT","MSFT.png","1200.01"]
        ]

#with open(filename,"w", newline = "") as writefile:
    #writer = csv.writer(writefile)
    #writer.writerow(header)
    #writer.writerows(data)

fields = []
rows = []

with open(filename, "r") as readfile:
    reader = csv.reader(readfile)
    fields = next(reader)

    for row in reader:
        rows.append(row)

print (fields)
print (rows)