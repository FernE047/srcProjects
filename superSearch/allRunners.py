from textos import embelezeTempo as eT
from time import time
import requests
import csv

def searchAllStarted(prefix):
    offset = 0
    truePeople = []
    valuesA = [ALPHA.index(c) for c in prefix]
    foundFirst = False
    foundLast = False
    while True:
        people = requests.get(f"{API}users?name={prefix}&max=200&offset={200*offset}").json()
        if 'data' not in people:
            break
        for person in people['data']:
            name = person['names']['international']
            if not foundFirst:
                if name.find(prefix) == 0:
                    foundFirst = True
                    truePeople.append(person)
                else:
                    if len(name)>=3:
                        valuesB = [ALPHA.index(c) for c in name.lower() if c in ALPHA]
                        if valuesB[0] < valuesA[0]:
                            continue
                        elif valuesB[0] == valuesA[0]:
                            if valuesB[1] < valuesA[1]:
                                continue
                            elif valuesB[1] == valuesA[1]:
                                if valuesB[2] <= valuesA[2]:
                                    continue
                                else:
                                    foundLast = True
                                    break
                            else:
                                foundLast = True
                                break
                        else:
                            foundLast = True
                            break
                    else:
                        continue
            else:
                if name.find(prefix) != 0:
                    foundLast = True
                    break
                else:
                    truePeople.append(person)
        if foundLast:
            break
        if len(people['data'])<200:
            break
        offset += 1
    return truePeople

API = "https://www.speedrun.com/api/v1/"

alphaFirst = ''
notFound = False 

begin = time()
ALPHA = ['_','-','.','|','@', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
with open('allRunners.csv','w',newline='',encoding = 'utf-8') as file:
    writer = csv.writer(file,delimiter = ';')
    for a in ALPHA:
        for b in ALPHA:
            for c in ALPHA:
                prefix = a + b + c
                if notFound:
                    if prefix == alphaFirst:
                        notFound = False
                    continue
                people = searchAllStarted(prefix)
                for person in people:
                    runner = []
                    runner.append(person['names']['international'])
                    runner.append(person['id'])
                    if person["location"]:
                        flag = f":flag_{person['location']['country']['code']}:"
                    else:
                        flag = ":united_nations:"
                    runner.append(flag)
                    runner.append(person['role'] == 'banned')
                    writer.writerow(runner)
                print(prefix)
end = time()
print(eT(end-begin))

