import requests

API = "https://www.speedrun.com/api/v1/"

def anyRequests(text):
    while True:
        try:
            return requests.get(text).json()
        except:
            print("connection")

def getAllPlatforms():
    offset = 0
    platforms = []
    while offset*200 < 10000:
        data = anyRequests(f"{API}platforms?offset={offset * 200}&max=200")
        if 'data' not in data:
            print('a')
            continue
        else:
            data = data["data"]
        platforms += [p['id'] for p in data]
        offset += 1
        if len(data) < 200:
            return platforms
    return platforms

def getRuns(mod,p):
    offset = 0
    total = offset*200
    while offset*200 < 10000:
        data = anyRequests(f"{API}runs?platform={p}&examiner={mod}&orderby=date&direction=asc&offset={offset * 200}&max=200")
        if 'data' not in data:
            offset = 0
            continue
        else:
            data = data["data"]
        total += len(data)
        print(total)
        offset += 1
        if len(data) < 200:
            return total
    lastRuns = data.copy()
    offset = 0
    while True:
        data = anyRequests(f"{API}runs?platform={p}&examiner={mod}&orderby=date&direction=desc&offset={offset * 200}&max=200")["data"]
        offset += 1
        for run in data:
            if run in lastRuns:
                print(total)
                return total
            else:
                total += 1
        print(total)
    return total

idd = '8l0rl9v8'
platforms = getAllPlatforms()
Total = 0
for p in platforms:
    print(p)
    Total += getRuns(idd,p)
    print(Total)
print(f"{idd} : {Total}")
