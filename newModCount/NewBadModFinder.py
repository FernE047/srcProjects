import requests
import csv
import datetime
from time import time
from textos import embelezeTempo as eT

API = "https://www.speedrun.com/api/v1/"
moderators = []
offset = 0
begin = time()
while True:
    games = requests.get(f"{API}games?offset={offset*200}&max=200").json()['data']
    for game in games:
        for moderator in game['moderators']:
            moderators.append(moderator)
    present = 200 * offset + 200
    end = time()
    duration = (end-begin)/present
    missing = duration * (30000-present)
    print(f"{present} : {int(10000*present/30000)/100}% : {eT(missing)}")
    if len(games)<200:
        break
    offset += 1
uniqueMod = set(moderators)
lb = []
for mod in uniqueMod:
    lb.append((mod,moderators.count(mod)))

lb.sort(key=lambda x: x[1], reverse=True)

print(lb)

print(datetime.datetime.now().date())

position = 0
lastValue = float('inf')

for n, i in enumerate(lb):
    value = i[1]
    if value != lastValue:
        position = n + 1
    lastValue = value
    name = requests.get(f"{API}users/{i[0]}").json()["data"]['names']['international']
    print(
        f"`{position}.{name} {' ' * (22-len(str(n+1))-len(name))} {value}`"
    )
    if position >= 200:
        break
