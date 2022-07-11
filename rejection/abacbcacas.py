import requests
from time import sleep
from time import time

def apiSleep(text): #to make sure less than 100 request will be made per minute
    begin = time()
    data = requests.get("https://www.speedrun.com/api/v1/" + text).json()["data"]
    end = time()
    timeElapsed = end-begin
    if timeElapsed < 0.6:
        sleep(0.6-timeElapsed)
    return data

def getIDs():
    with open(DIRECTORY + "\\runners.csv",'r') as file:
        data = {}
        line = file.readline()[:-1]
        while line:
            runner,Id,_ = line[:-1].split(",")
            data[runner] = Id
            line = file.readline()
    return data

DIRECTORY = "C:\\Users\\Programador\\Documents\\GitHub\\SrcLbMaker\\SrcLbMaker"
runnerIDs = getIDs()
total = 0
categoriesDeleted = []
categoriesNotDeleted = []
for runner in runnerIDs:
    runnerID = runnerIDs[runner]
    runs = []
    offset = 0
    while offset*200 < 10000:
        d = apiSleep("runs?user={0}&offset={1}&max=200&status=rejected".format(runnerID,offset*200))
        for run in d:
            category = run["category"]
            if category in categoriesDeleted:
                runs.append(run['weblink'])
            elif category in categoriesNotDeleted:
                pass
            else:
                d = requests.get("https://www.speedrun.com/api/v1/categories/{}".format(category)).json()
                if 'data' in d:
                    categoriesNotDeleted.append(category)
                else:
                    categoriesDeleted.append(category)
                    runs.append(run['weblink'])
        offset += 1
        if len(d)<200:
            break
    if runs:
        print(runner)
        for run in runs:
            print(run)
        print()
        total += len(runs)
print(total)
