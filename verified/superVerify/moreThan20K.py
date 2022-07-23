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
        platforms += [{p['name'],p['id']} for p in data]
        offset += 1
        if len(data) < 200:
            return platforms
    return platforms

def getRuns(mod,p):
    offset = 0
    modGames = {}
    total = 0
    while offset*200 < 10000:
        data = anyRequests(f"{API}runs?platform={p}&examiner={mod}&orderby=date&direction=asc&offset={offset * 200}&max=200&status=verified&embed=game")["data"]
        total += len(data)
        print(total)
        for run in data:
            MOD[mod].add(run['game']['data']['names']['international'])
            if run['game']['data']['id'] in modGames:
                modGames[run['game']['data']['id']] += 1
            else:
                modGames[run['game']['data']['id']] = 1
        offset += 1
        if len(data) < 200:
            with open('mod20KGames.csv',newline = '',mode = 'a') as file:
                writer = csv.writer(file)
                for a in modGames.items():
                    writer.writerow(tuple([mod]) + a)
            print(MOD)
            return total
    lastRuns = data.copy()
    offset = 0
    while True:
        data = anyRequests(f"{API}runs?platform={p}&examiner={mod}&orderby=date&direction=desc&offset={offset * 200}&max=200&status=verified&embed=game")["data"]
        offset += 1
        for run in data:
            if run['game']['data']['id'] in modGames:
                modGames[run['game']['data']['id']] += 1
            else:
                modGames[run['game']['data']['id']] = 1
            if run in lastRuns:
                print(total)
                with open('mod20KGames.csv',newline = '',mode = 'a') as file:
                    writer = csv.writer(file)
                    for a in modGames.items():
                        writer.writerow(tuple([mod]) + a)
                print(MOD)
                return total
            else:
                total += 1
        print(total)
    with open('mod20KGames.csv',newline = '',mode = 'a') as file:
        writer = csv.writer(file)
        for a in modGames.items():
            writer.writerow(tuple([mod]) + a)
    return total

idd = ['8l0rl9v8','kj9p77x4']
platforms = getAllPlatforms()
Total = [0,0]
MOD = {'8l0rl9v8': set(),'kj9p77x4': set()}
for p in platforms:
    print(p)
    Total[0] += getRuns(idd[0],p)
    print(Total[0])
    Total[1] += getRuns(idd[1],p)
    print(Total[1])
for i in range(2):
    print(f"{idd[i]} : {Total[i]}")
