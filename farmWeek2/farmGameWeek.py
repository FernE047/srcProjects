import requests

runners = [
{'id': 'xk49l57j', 'name': 'Hades', 'flag': ':flag_vh:'},
{'id': '8l0rl9v8', 'name': 'Reni', 'flag': ':flag_pl:'},
{'id': 'xko2g798', 'name': 'Akuretaki', 'flag': ':flag_ru:'},
{'id': '8q32emwj', 'name': 'Daxzz', 'flag': ':flag_es:'},
{'id': 'jn39e4dx', 'name': 'Merl_', 'flag': ':flag_sc:'},
{'id': '68wvldlx', 'name': 'Comical_', 'flag': ':flag_ca:'},
{'id': 'qxkpvo7j', 'name': 'McThumbs', 'flag': ':flag_us:'},
{'id': '8qzo95o8', 'name': 'TRLittleToaster', 'flag': ':flag_us:'},
{'id': 'x7q9g1v8', 'name': 'felipereis11011', 'flag': ':flag_br:'},
{'id': 'jn36q61x', 'name': 'stathx', 'flag': ':flag_ao:'},
{'id': 'x35yq46j', 'name': '4d9r', 'flag': ':flag_ca:'},
{'id': 'j4qrqlvx', 'name': 'pocogamer', 'flag': ':flag_gr:'},
{'id': '8grm677x', 'name': 'daff', 'flag': ':flag_ru:'},
{'id': 'jn36qqqx', 'name': 'Toxcien', 'flag': ':flag_fi:'},
{'id': '8e6rpq7j', 'name': 'LordParoah', 'flag': ':flag_br:'},
{'id': 'xz79gdej', 'name': 'Wrap', 'flag': ':flag_vh:'},
{'id': '8e913qdj', 'name': 'VyPr', 'flag': ':flag_us:'},
{'id': '816q54lx', 'name': 'AslanTZ', 'flag': ':flag_tr:'},
{'id': 'j0n55mr8', 'name': 'astrolite', 'flag': ':flag_no:'},
{'id': 'qjoqz4e8', 'name': 'Elims', 'flag': ':flag_gb:'},
{'id': 'x3qmp56j', 'name': 'Bluestonex64', 'flag': ':flag_pt:'},
{'id': 'j26g4pnx', 'name': 'Zalex', 'flag': ':flag_gr:'},
{'id': '98rv0dqj', 'name': 'zir0nic', 'flag': ':flag_vh:'},
{'id': '8r72pyqj', 'name': 'Teoinator', 'flag': ':flag_dj:'},
{'id': 'v8lqkv7x', 'name': 'Ivory', 'flag': ':flag_us:'},
{'id': '86313ep8', 'name': 'WookiesLA420', 'flag': ':flag_us:'},
{'id': 'j92266v8', 'name': 'JDMI', 'flag': ':flag_us:'},
{'id': '8en6edo8', 'name': 'HenryNutsy', 'flag': ':flag_pl:'},
{'id': 'x7mz16rx', 'name': 'MagikBased', 'flag': ':flag_us:'},
{'id': 'jmo66dn8', 'name': 'MechanicalSnail', 'flag': ':flag_us:'},
{'id': 'x35q3nqj', 'name': 'Aiivan', 'flag': ':flag_ru:'}
]

API = "https://www.speedrun.com/api/v1/"

def getRuns(runner):
    print(runner)
    global GAMES
    offset = 0
    runsNew = 0
    runsFGNew = 0
    lastRuns = []
    while True:
        data = requests.get(
            f"{API}runs?user={runner['id']}&max=200&offset={offset * 200}&orderby=date&direction=desc&embed=game"
        ).json()
        offset += 1
        for run in data['data']:
            if run['date'] in (['2022-07-' + a for a in ('17','18','19','20','21','22','23','24')]):
                runsNew += 1
                if run['level'] is None:
                    runsFGNew +=1
                game = run['game']['data']['names']['international']
                if game in GAMES:
                    GAMES[game] += 1
                else:
                    GAMES[game] = 1
            else:
                return [runsNew,runsFGNew]
        if data["pagination"]["size"] < 200:
            break
        if offset * 200 == 10000:
            lastRuns = data['data'].copy()
            break
    return [runsNew,runsFGNew]

def doLb(index,runners):
    runners.sort(key=lambda x: x[index], reverse=True)
    print(index)
    position = 0
    lastValue = float('inf')
    text0 = ''
    text1 = ''
    text2 = ''
    for n, i in enumerate(runners):
        if i[index] != lastValue:
            position = n+1
        lastValue = i[index]
        print(f"`{position}.{i['name']} {' ' * (23-len(str(n+1))-len(i['name']))} {i[index]}`")
        text0 += f"#{position}\n"
        text1 += f"{i['name']}\n"
        text2 += f"{i[index]}\n"
    print(text0)
    print(text1)
    print(text2)

GAMES = {}

for runner in runners:
    data = getRuns(runner)
    runner['official'] = data[1]
    runner['side'] = data[0]
import datetime

runners[2]['official'] -= 33
runners[2]['side'] -= 33

doLb('official',runners)
doLb('side',runners)

text0 = ""
text1 = ""

GAMES = list(GAMES.items())
GAMES.sort(key=lambda x: x[1], reverse=True)

for game in GAMES:
    text0 += f"{game[0]}\n"
    text1 += f"{game[1]}\n"
print(text0)
print(text1)
