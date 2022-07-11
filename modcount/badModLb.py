import requests
import string
import csv
import os
from time import sleep
from time import time
from textos import embelezeTempo as eT

# Util Section #

def apiSleep(text): #to make sure less than 100 request will be made per minute
    begin = time()
    data = requests.get("https://www.speedrun.com/api/v1/" + text).json()["data"]
    end = time()
    timeElapsed = end-begin
    if timeElapsed < 1:
        sleep(1-timeElapsed)
    return data

def getName(iD):
    return apiSleep('users/{}'.format(iD))["names"]["international"]

def lbOrder(moderators):
    numbers = {}
    for moderator in moderators:
        if moderators[moderator] not in numbers:
            numbers[moderators[moderator]] = [moderator]
        else:
            numbers[moderators[moderator]].append(moderator)
    lbNumbers = list(numbers.keys())
    lbNumbers.sort()
    lbNumbers = list(reversed(lbNumbers))
    lbModerators = []
    for indice in range(len(lbNumbers)):
        lbModerators += numbers[lbNumbers[indice]]
        if len(lbModerators)>=200:
            break
    lb = []
    for moderator in lbModerators:
        lb.append({"id":moderator,"number":moderators[moderator]})
    return lb

def makeLb(moderators):
    lbRunners = lbOrder(moderators)
    position = 1
    tiedPos = 0
    for i in range(len(lbRunners)):
        runner = lbRunners[i]
        runner['name'] = getName(runner['id'])
        if i != 0:
            if runner['number'] == lbRunners[i-1]['number']:
                tiedPos += 1
            else:
                tiedPos = 0
        line = "`{0: 4d}.{1} -{2: 5d}`".format(position - tiedPos,
                                               " "*(20-len(runner['name'])) + runner['name'],
                                               runner['number'])
        position += 1
        print(line)

def isDuplicate(platforms,platformsUsed):
    for platform in platforms:
        if platform in platformsUsed:
            return True
    return False

def modCount(idd): #ReeledWarrior14
    offset = 0
    total = 0
    search = 'games?moderator={0}&offset={1}&max=200'
    while offset*200 < 10000:
        data = apiSleep(search.format(idd,offset*200))
        total += len(data)
        offset += 1
        if len(data) < 200:
            return total
    return total

moderators = {}
platformsUsed = []
for platID in ('8gejmne3', 'vm9vw163', 'mx6pow93', 'o7e2dj6w', 'mr6ko5ez', 'gde32g6k', 'wxeo0der', '5negykey', 'gde3vw9k', '3167pk6q', 'kz9wlm6p', 'gz9qg3e0', 'lq60nl94', 'n5e15292', 'w89ryw6l', '7g6mom9r', 'vm9vz163', 'vm9vn63k', 'mr6k206z', 'o0644863', 'lq60ol64', 'gde33gek', 'n5e1m7e2', 'jm9577eo', 'jm95oz6o', 'kz9wzm9p', 'o0641163', 'n5e1g7e2', 'v06dvz64', 'gz9q2390', 'n5685z6v', 'wxeo8d6r', 'gz9qox60', 'p36n4x98', 'w89ryd6l', 'gz9qv3e0', 'lq60rd64', 'v06d394z', 'wxeo3zer', 'gde31w9k', 'gde3owek', 'mr6k409z', 'jm95k79o', 'gz9qkx90', 'n5683oev', '3167d6q2', 'gde3g9k1', 'vm9v3ne3', '7m6yvw6p', '31672keq', '4p9z06rn', '5neg076y', 'o064z1e3', 'gz9qwx90', 'w89rwwel', 'o0643893', 'gde3xgek', 'mr6k159z', 'p36nd598', 'nzel5r6q', 'nzel3veq', '7m6ypz6p', 'n5e1n292', '5neg7key', 'mx6ppw63', 'p36npx98', '5negp7ey', 'mx6px493', 'gde3rwek', 'mr6km09z', 'jm950z6o', '83exkk6l', '83exlkel', '7g6mw8er', 'o064r893', 'mx6p4w63', 'kz9w7mep', 'n5e1z292', '7m6ydw6p', 'o7e2lj9w', 'kz9wynep', 'kz9wqn9p', 'v06do394', 'gz9qx60q', '7g6mx89r', 'w89rwelk', '7g6m8erk', 'jm95z9ol', 'kz9wdmep', 'p36nyx98', 'v06dmz64', 'o064o193', '4p9zq09r', '8gej5193', 'nzeloreq', 'nzelrveq', '8gej2n93', 'p36n8568', 'w89rjw6l', 'n568qz6v', 'wxeod9rn', 'n5e17e27', 'mx6pwe3g', 'nzelkr6q', 'nzeljv9q', '4p9zjrer', 'o7e2vj6w', 'wxeo5z6r', '5negk9y7', 'lq60gle4', '4p9z70er', '3167od9q', 'vm9vr1e3', 'v06dpz64', 'wxeo2d6r', '7g6mym6r', 'jm95l76o', '83exokel', 'kz9wrn6p', '31670d9q', 'w89r3w9l', 'mr6k0ezw', 'mx6p3493', '83exwk6l', '7m6yjz6p', 'lq60l642', '83expv9l', 'o0641863', '83exovel', '5negr76y', '31677k6q', '3167jd6q', 'n5e147e2', '83exk6l5', '7m6ylw9p', 'mx6p1463', 'wxeogz9r', 'vm9vkn63', '8gejn193', 'mx6pq4e3', '5nego76y', 'lq604de4', '4p9zprer', '3167qkeq', 'p36nlxe8', 'jm95w79o', '5negxk6y', '8gej8n93', '83exvv9l', '7g6m1m6r', '7g6mk8er', 'o7e25xew', 'v06dk3e4', 'w89rdd6l', '8gejn93d', 'v06dr394', 'nzelreqp', 'lq60mde4', 'w89r4d6l', 'p36no5e8', 'vm9v8n63', 'n568kz6v', 'n5681o9v', 'jm95zz9o', 'n568oevp', 'lq60vde4', 'o7e2mx6w', 'o064j163', '4p9z0r6r', 'o7e2xj9w', 'nzelyv9q', '7m6y2zep', 'n568zo6v'):
    print(platID)
    offset = 0
    search = 'games?platform={0}&offset={1}&max=200'
    while offset*200 < 10000:
        games = apiSleep(search.format(platID,offset*200))
        for game in games:
            if not isDuplicate(game["platforms"],platformsUsed):
                for moderator in game["moderators"]:
                    if moderator not in moderators:
                        moderators[moderator] = 1
                    else:
                        moderators[moderator] += 1
        if len(games) < 200:
            break
        offset += 1
    platformsUsed.append(platID)
mods = lbOrder(moderators)
moderators = {}
for mod in mods:
    moderators[mod['id']] = modCount(mod['id'])
makeLb(moderators)
