import requests

API = "https://www.speedrun.com/api/v1/"

def getRuns(runner,status):
    offset = 0
    while True:
        data = requests.get(
            f"{API}runs?user={runner['id']}&max=200&offset={offset * 200}&status={status}"
        ).json()
        offset += 1
        if data["pagination"]["size"] < 200:
            break
    return data["pagination"]["offset"] + data["pagination"]["size"]

def getRunnerID(username):
    """Check if the user exists, return his data if any, otherwise False."""
    data = requests.get(
        f"{API}users?lookup={username}"
    ).json()
    return data['data'][0]['id']

runnersNames = ['4d9r','zir0nic','stathx','Astrolite','Otterstone_Gamer',
'felipereis11011','felipenascimento83','JDMI','ComicBlue','reni',
'Kkntucara','VyPr','killerkun...','Toxcien','JeelSpeed','AslanTZ',
'Elims','Merl_','Walgrey','hahhah42','Zambrini','Kkspeed',
'Ivory','Bob-chicken','wrap','Act7','Fioresa','TRlittleToaster','daff',
'Slothboy78YT','jackzfiml','shinboy'
]

print('{')

runners = {"4d9r" : {'name': '4d9r', 'id': 'x35yq46j', 'runs': {'initial': {'verified': 634, 'rejected': 14, 'new': 243}, 'today': {'verified': 0, 'rejected': 0, 'new': 0}, 'total': 0}, 'wrs': {'initial': 449, 'today': 0, 'total': 0}, 'games': {'initial': 30, 'today': 0, 'total': 0}},
"zir0nic" : {'name': 'zir0nic', 'id': '98rv0dqj', 'runs': {'initial': {'verified': 998, 'rejected': 36, 'new': 1}, 'today': {'verified': 0, 'rejected': 0, 'new': 0}, 'total': 0}, 'wrs': {'initial': 334, 'today': 0, 'total': 0}, 'games': {'initial': 208, 'today': 0, 'total': 0}},
"stathx" : {'name': 'stathx', 'id': 'jn36q61x', 'runs': {'initial': {'verified': 1439, 'rejected': 21, 'new': 0}, 'today': {'verified': 0, 'rejected': 0, 'new': 0}, 'total': 0}, 'wrs': {'initial': 914, 'today': 0, 'total': 0}, 'games': {'initial': 44, 'today': 0, 'total': 0}},
"Astrolite" : {'name': 'Astrolite', 'id': 'j0n55mr8', 'runs': {'initial': {'verified': 1205, 'rejected': 162, 'new': 86}, 'today': {'verified': 0, 'rejected': 0, 'new': 0}, 'total': 0}, 'wrs': {'initial': 703, 'today': 0, 'total': 0}, 'games': {'initial': 60, 'today': 0, 'total': 0}},
"Otterstone_Gamer" : {'name': 'Otterstone_Gamer', 'id': 'qjn1wzw8', 'runs': {'initial': {'verified': 8240, 'rejected': 454, 'new': 615}, 'today': {'verified': 0, 'rejected': 0, 'new': 0}, 'total': 0}, 'wrs': {'initial': 4058, 'today': 0, 'total': 0}, 'games': {'initial': 439, 'today': 0, 'total': 0}},
"felipereis11011" : {'name': 'felipereis11011', 'id': 'x7q9g1v8', 'runs': {'initial': {'verified': 1216, 'rejected': 1, 'new': 0}, 'today': {'verified': 0, 'rejected': 0, 'new': 0}, 'total': 0}, 'wrs': {'initial': 689, 'today': 0, 'total': 0}, 'games': {'initial': 38, 'today': 0, 'total': 0}},
"felipenascimento83" : {'name': 'felipenascimento83', 'id': '68wne448', 'runs': {'initial': {'verified': 2019, 'rejected': 0, 'new': 3}, 'today': {'verified': 0, 'rejected': 0, 'new': 0}, 'total': 0}, 'wrs': {'initial': 1519, 'today': 0, 'total': 0}, 'games': {'initial': 453, 'today': 0, 'total': 0}},
"JDMI" : {'name': 'JDMI', 'id': 'j92266v8', 'runs': {'initial': {'verified': 997, 'rejected': 18, 'new': 0}, 'today': {'verified': 0, 'rejected': 0, 'new': 0}, 'total': 0}, 'wrs': {'initial': 664, 'today': 0, 'total': 0}, 'games': {'initial': 44, 'today': 0, 'total': 0}},
"ComicBlue" : {'name': 'ComicBlue', 'id': '68wvldlx', 'runs': {'initial': {'verified': 2356, 'rejected': 59, 'new': 3}, 'today': {'verified': 0, 'rejected': 0, 'new': 0}, 'total': 0}, 'wrs': {'initial': 1299, 'today': 0, 'total': 0}, 'games': {'initial': 219, 'today': 0, 'total': 0}},
"reni" : {'name': 'reni', 'id': '8l0rl9v8', 'runs': {'initial': {'verified': 1540, 'rejected': 2, 'new': 0}, 'today': {'verified': 0, 'rejected': 0, 'new': 0}, 'total': 0}, 'wrs': {'initial': 362, 'today': 0, 'total': 0}, 'games': {'initial': 170, 'today': 0, 'total': 0}},
"Kkntucara" : {'name': 'Kkntucara', 'id': 'xz9nv648', 'runs': {'initial': {'verified': 1379, 'rejected': 52, 'new': 12}, 'today': {'verified': 0, 'rejected': 0, 'new': 0}, 'total': 0}, 'wrs': {'initial': 683, 'today': 0, 'total': 0}, 'games': {'initial': 60, 'today': 0, 'total': 0}},
"VyPr" : {'name': 'VyPr', 'id': '8e913qdj', 'runs': {'initial': {'verified': 1634, 'rejected': 2, 'new': 22}, 'today': {'verified': 0, 'rejected': 0, 'new': 0}, 'total': 0}, 'wrs': {'initial': 769, 'today': 0, 'total': 0}, 'games': {'initial': 99, 'today': 0, 'total': 0}},
"killerkun..." : {'name': 'killerkun...', 'id': '8qr5kvwj', 'runs': {'initial': {'verified': 1978, 'rejected': 0, 'new': 6}, 'today': {'verified': 0, 'rejected': 0, 'new': 0}, 'total': 0}, 'wrs': {'initial': 1413, 'today': 0, 'total': 0}, 'games': {'initial': 71, 'today': 0, 'total': 0}},
"Toxcien" : {'name': 'Toxcien', 'id': 'jn36qqqx', 'runs': {'initial': {'verified': 430, 'rejected': 4, 'new': 1}, 'today': {'verified': 0, 'rejected': 0, 'new': 0}, 'total': 0}, 'wrs': {'initial': 367, 'today': 0, 'total': 0}, 'games': {'initial': 16, 'today': 0, 'total': 0}},
"JeelSpeed" : {'name': 'JeelSpeed', 'id': 'jpre35y8', 'runs': {'initial': {'verified': 893, 'rejected': 24, 'new': 23}, 'today': {'verified': 0, 'rejected': 0, 'new': 0}, 'total': 0}, 'wrs': {'initial': 199, 'today': 0, 'total': 0}, 'games': {'initial': 17, 'today': 0, 'total': 0}},
"AslanTZ" : {'name': 'AslanTZ', 'id': '816q54lx', 'runs': {'initial': {'verified': 1447, 'rejected': 24, 'new': 0}, 'today': {'verified': 0, 'rejected': 0, 'new': 0}, 'total': 0}, 'wrs': {'initial': 527, 'today': 0, 'total': 0}, 'games': {'initial': 178, 'today': 0, 'total': 0}},
"Elims" : {'name': 'Elims', 'id': 'qjoqz4e8', 'runs': {'initial': {'verified': 1282, 'rejected': 86, 'new': 1}, 'today': {'verified': 0, 'rejected': 0, 'new': 0}, 'total': 0}, 'wrs': {'initial': 213, 'today': 0, 'total': 0}, 'games': {'initial': 141, 'today': 0, 'total': 0}},
"Merl_" : {'name': 'Merl_', 'id': 'jn39e4dx', 'runs': {'initial': {'verified': 248, 'rejected': 1, 'new': 0}, 'today': {'verified': 0, 'rejected': 0, 'new': 0}, 'total': 0}, 'wrs': {'initial': 85, 'today': 0, 'total': 0}, 'games': {'initial': 37, 'today': 0, 'total': 0}},
"Walgrey" : {'name': 'Walgrey', 'id': '8ge6w47j', 'runs': {'initial': {'verified': 661, 'rejected': 2, 'new': 0}, 'today': {'verified': 0, 'rejected': 0, 'new': 0}, 'total': 0}, 'wrs': {'initial': 235, 'today': 0, 'total': 0}, 'games': {'initial': 66, 'today': 0, 'total': 0}},
"hahhah42" : {'name': 'hahhah42', 'id': 'jmoqknn8', 'runs': {'initial': {'verified': 285, 'rejected': 1, 'new': 0}, 'today': {'verified': 0, 'rejected': 0, 'new': 0}, 'total': 0}, 'wrs': {'initial': 52, 'today': 0, 'total': 0}, 'games': {'initial': 27, 'today': 0, 'total': 0}},
"Zambrini" : {'name': 'Zambrini', 'id': '1xyylnyx', 'runs': {'initial': {'verified': 1670, 'rejected': 8, 'new': 20}, 'today': {'verified': 0, 'rejected': 0, 'new': 0}, 'total': 0}, 'wrs': {'initial': 1089, 'today': 0, 'total': 0}, 'games': {'initial': 164, 'today': 0, 'total': 0}},
"Kkspeed" : {'name': 'Kkspeed', 'id': 'xz7m6knj', 'runs': {'initial': {'verified': 157, 'rejected': 17, 'new': 32}, 'today': {'verified': 0, 'rejected': 0, 'new': 0}, 'total': 0}, 'wrs': {'initial': 43, 'today': 0, 'total': 0}, 'games': {'initial': 12, 'today': 0, 'total': 0}},
"Ivory" : {'name': 'Ivory', 'id': 'v8lqkv7x', 'runs': {'initial': {'verified': 38, 'rejected': 31, 'new': 1}, 'today': {'verified': 0, 'rejected': 0, 'new': 0}, 'total': 0}, 'wrs': {'initial': 0, 'today': 0, 'total': 0}, 'games': {'initial': 15, 'today': 0, 'total': 0}},
"Bob-chicken" : {'name': 'Bob-chicken', 'id': 'x7q6qy08', 'runs': {'initial': {'verified': 380, 'rejected': 28, 'new': 1}, 'today': {'verified': 0, 'rejected': 0, 'new': 0}, 'total': 0}, 'wrs': {'initial': 77, 'today': 0, 'total': 0}, 'games': {'initial': 62, 'today': 0, 'total': 0}},
"wrap" : {'name': 'wrap', 'id': 'xz79gdej', 'runs': {'initial': {'verified': 81, 'rejected': 10, 'new': 0}, 'today': {'verified': 0, 'rejected': 0, 'new': 0}, 'total': 0}, 'wrs': {'initial': 44, 'today': 0, 'total': 0}, 'games': {'initial': 16, 'today': 0, 'total': 0}},
"Act7" : {'name': 'Act7', 'id': 'j51p0268', 'runs': {'initial': {'verified': 856, 'rejected': 100, 'new': 8}, 'today': {'verified': 0, 'rejected': 0, 'new': 0}, 'total': 0}, 'wrs': {'initial': 316, 'today': 0, 'total': 0}, 'games': {'initial': 148, 'today': 0, 'total': 0}},
"Fioresa" : {'name': 'Fioresa', 'id': '1xy3wpwj', 'runs': {'initial': {'verified': 5269, 'rejected': 16, 'new': 58}, 'today': {'verified': 0, 'rejected': 0, 'new': 0}, 'total': 0}, 'wrs': {'initial': 3460, 'today': 0, 'total': 0}, 'games': {'initial': 90, 'today': 0, 'total': 0}},
"daff" : {'name': 'daff', 'id': '8grm677x', 'runs': {'initial': {'verified': 3508, 'rejected': 45, 'new': 57}, 'today': {'verified': 0, 'rejected': 0, 'new': 0}, 'total': 0}, 'wrs': {'initial': 2305, 'today': 0, 'total': 0}, 'games': {'initial': 48, 'today': 0, 'total': 0}},
"Slothboy78YT" : {'name': 'Slothboy78YT', 'id': '8grk0zyx', 'runs': {'initial': {'verified': 152, 'rejected': 35, 'new': 62}, 'today': {'verified': 0, 'rejected': 0, 'new': 0}, 'total': 0}, 'wrs': {'initial': 46, 'today': 0, 'total': 0}, 'games': {'initial': 18, 'today': 0, 'total': 0}},
"TRlittleToaster" : {'name': 'TRlittleToaster', 'id': '8qzo95o8', 'runs': {'initial': {'verified': 1971, 'rejected': 1, 'new': 10}, 'today': {'verified': 0, 'rejected': 0, 'new': 0}, 'total': 0}, 'wrs': {'initial': 283, 'today': 0, 'total': 0}, 'games': {'initial': 1338, 'today': 0, 'total': 0}},
"jackzfiml" : {'name': 'jackzfiml', 'id': '8ge265yj', 'runs': {'initial': {'verified': 463, 'rejected': 3, 'new': 0}, 'today': {'verified': 0, 'rejected': 0, 'new': 0}, 'total': 0}, 'wrs': {'initial': 124, 'today': 0, 'total': 0}, 'games': {'initial': 63, 'today': 0, 'total': 0}},
"shinboy" : {'name': 'shinboy', 'id': '8wl7yovj', 'runs': {'initial': {'verified': 1736, 'rejected': 0, 'new': 0}, 'today': {'verified': 0, 'rejected': 0, 'new': 0}, 'total': 0}, 'wrs': {'initial': 1343, 'today': 0, 'total': 0}, 'games': {'initial': 7, 'today': 0, 'total': 0}}}

for runner in runners:
    runnersNames.remove(runner)

for name in runnersNames:
    runner = {}
    runner['name'] = name
    runner['id'] = getRunnerID(name)
    runner['runs'] = {'initial' : {},'today' : {},'total' : 0}
    runner['runs']['initial'] = {'verified': 0, 'rejected': 0, 'new': 0}
    for status in runner['runs']['initial']:
        runner['runs']['initial'][status] = getRuns(runner,status)
    runner['runs']['today'] = {'verified': 0, 'rejected': 0, 'new': 0}
    personalBests = requests.get(f"{API}users/{runner['id']}/personal-bests").json()["data"]
    runner['wrs'] = {'initial' : len([run for run in personalBests if run['place'] == 1]),'today' : 0,'total' : 0}
    runner['games'] = {'initial' : len(set([run["run"]["game"] for run in personalBests])),'today' : 0,'total' : 0}
    print("\"" + name + "\" : " + str(runner) + ",")
    runners[name] = runner
for name in runners:
    print(name + " : " + str(runners[name]['runs']['initial']['new'] + runners[name]['runs']['initial']['verified']))
