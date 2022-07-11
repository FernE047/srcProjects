import requests

runners = [
{'id': 'qjn1wzw8', 'name': 'Otterstone_Gamer', 'flag': ':flag_us:'},
{'id': '8qzo95o8', 'name': 'TRLittleToaster', 'flag': ':flag_us:'},
{'id': '98rv0dqj', 'name': 'zir0nic', 'flag': ':flag_vh:'},
{'id': 'x35yq46j', 'name': '4d9r', 'flag': ':flag_ca:'},
{'id': 'jn36q61x', 'name': 'stathx', 'flag': ':flag_ao:'},
{'id': 'xz7m6knj', 'name': 'KkSpeed', 'flag': ':flag_us:'},
{'id': 'j0n55mr8', 'name': 'Astrolite', 'flag': ':flag_no:'},
{'id': 'x7q9g1v8', 'name': 'felipereis11011', 'flag': ':flag_br:'},
{'id': 'qjoqz4e8', 'name': 'Elims', 'flag': ':flag_gb:'},
{'id': '68wvldlx', 'name': 'ComicBlue', 'flag': ':flag_ca:'},
{'id': 'xz79gdej', 'name': 'Wrap', 'flag': ':flag_us:'},
{'id': '8qr5kvwj', 'name': 'killerkun...', 'flag': ':flag_jp:'},
{'id': '8grm677x', 'name': 'daff', 'flag': ':flag_ru:'},
{'id': 'y8dz629j', 'name': 'sWinTuZ', 'flag': ':flag_ru:'},
{'id': 'jpre35y8', 'name': 'JeelSpeed', 'flag': ':flag_zw:'},
{'id': 'j51p0268', 'name': 'Act_', 'flag': ':flag_us:'},
{'id': '8l4p3prj', 'name': 'notitsam', 'flag': ':flag_us:'},
{'id': 'j92266v8', 'name': 'JDMI', 'flag': ':flag_us:'},
{'id': '8l0rl9v8', 'name': 'Reni', 'flag': ':flag_pl:'},
{'id': 'xz9nv648', 'name': 'Kkntucara', 'flag': ':flag_es:'},
{'id': 'xk49l57j', 'name': 'Colors', 'flag': ':flag_vh:'}
]

API = "https://www.speedrun.com/api/v1/"

def getRuns(runner):
    offset = 0
    gamesNew = {}
    gamesOld = {}
    lastRuns = []
    while True:
        data = requests.get(
            f"{API}runs?user={runner['id']}&max=200&offset={offset * 200}&orderby=date&direction=desc"
        ).json()
        offset += 1
        for run in data['data']:
            if run['date'] in (['2022-03-' + a for a in ('06','07','08','09','10','11','12','13')]):
                if run['game'] in gamesNew:
                    gamesNew[run['game']] += 1
                else:
                    gamesNew[run['game']] = 1
            else:
                if run['game'] in gamesOld:
                    gamesOld[run['game']] += 1
                else:
                    gamesOld[run['game']] = 1
        if data["pagination"]["size"] < 200:
            break
        if offset * 200 == 10000:
            lastRuns = data['data'].copy()
            break
    offset = 0
    if lastRuns:
        while True:
            data = requests.get(
                f"{API}runs?user={runner['id']}&max=200&offset={offset * 200}&orderby=date&direction=asc"
            ).json()
            offset += 1
            for run in data['data']:
                if run in lastRuns:
                    break
                if run['date'] in (['2022-03-' + a for a in ('06','07','08','09','10','11','12','13')]):
                    if run['game'] in gamesNew:
                        gamesNew[run['game']] += 1
                    else:
                        gamesNew[run['game']] = 1
                else:
                    if run['game'] in gamesOld:
                        gamesOld[run['game']] += 1
                    else:
                        gamesOld[run['game']] = 1
            if run in lastRuns:
                break
    gamesNewests = {}
    for game in gamesNew:
        if game not in gamesOld:
            gamesNewests[game] = gamesNew[game]
    print(runner['name'])
    print(len(gamesOld))
    print(len(gamesNew))
    print(len(gamesNewests))
    return (gamesNew,gamesNewests)

def doLb(index,runners):
    runners.sort(key=lambda x: len(x[index]), reverse=True)
    print(index)
    position = 0
    lastValue = float('inf')
    text0 = ''
    text1 = ''
    text2 = ''
    for n, i in enumerate(runners):
        if len(i[index]) != lastValue:
            position = n+1
        lastValue = len(i[index])
        print(f"`{position}.{i['name']} {' ' * (23-len(str(n+1))-len(i['name']))} {len(i[index])}`")
        text0 += f"#{position}\n"
        text1 += f"{i['name']}\n"
        text2 += f"{len(i[index])}\n"
    print(text0)
    print(text1)
    print(text2)

allGames = {}

for runner in runners:
    data = getRuns(runner)
    runner['official'] = data[1]
    runner['side'] = data[0]
    for game in runner['side']:
        if game in allGames:
            allGames[game] += 1
        else:
            allGames[game] = 1
    print()

import datetime

doLb('official',runners)
doLb('side',runners)

text0 = ""
text1 = ""

print(len(allGames))

for game in allGames:
    data = requests.get(
            f"{API}games/{game}"
        ).json()
    text0 += f"{data['data']['names']['international']}\n"
    text1 += f"{allGames[game]}\n"
print(text0)
print(text1)
