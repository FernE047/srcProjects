import csv

with open("allModerators.csv",'r') as file:
    csvReader = csv.reader(file)
    everyMod = set()
    with open("moderatorsNotDuplicate.csv",'w',newline='') as fileOutput:
        csvWriter = csv.writer(fileOutput)
        for row in csvReader:
            iD = row[0]
            if iD not in everyMod:
                csvWriter.writerow([iD])
                everyMod.add(iD)
