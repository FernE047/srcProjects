import csv
import requests
from time import time
from textos import embelezeTempo as eT

API = "https://www.speedrun.com/api/v1/"

offset = 0
begin = time()
with open('fullGameCheck.csv','w', newline='',encoding = 'utf-8') as file:
    writer = csv.writer(file,delimiter=';')
    while True:
        games = requests.get(f"{API}games?offset={offset*200}&max=200&embed=categories,variables").json()['data']
        for game in games:
            idGame = game['id']
            categoriesFG = [category['id'] for category in game['categories']['data'] if category['type'] == 'per-game']
            variables = [var for var in game['variables']['data'] if (var['is-subcategory'] and var['scope']['type'] in ('global','full-game'))]
            totalFG = 0
            for idCat in categoriesFG:
                if variables:
                    for variable in variables:
                        idVar = variable['id']
                        for value in variable['values']['values']:
                            data = requests.get(f"{API}leaderboards/{idGame}/category/{idCat}?var-{idVar}={value}&top=1&max=200").json()
                            if 'data' in data:
                                data = data['data']
                            else:
                                print(data)
                                print(f"{API}leaderboards/{idGame}/category/{idCat}?var-{idVar}={value}&top=1&max=200")
                                continue
                            if data['runs']:
                                for run in data['runs']:
                                    players = [p['id'] for p in run['run']['players'] if 'id' in p]
                                    players = []
                                    for p in run['run']['players']:
                                        if 'id' in p:
                                            players.append(p['id'])
                                        else:
                                            players.append(p['name'] + " (guest)")
                                    writer.writerow(players)
                else:
                    data = requests.get(f"{API}leaderboards/{idGame}/category/{idCat}?top=1&max=200").json()
                    if 'data' in data:
                        data = data['data']
                    else:
                        print(data)
                        print(f"{API}leaderboards/{idGame}/category/{idCat}?top=1&max=200")
                        continue
                    if data['runs']:
                        for run in data['runs']:
                            players = [p['id'] for p in run['run']['players'] if 'id' in p]
                            players = []
                            for p in run['run']['players']:
                                if 'id' in p:
                                    players.append(p['id'])
                                else:
                                    players.append(p['name'] + " (guest)")
                            writer.writerow(players)
        present = 200 * offset + 200
        end = time()
        duration = end - begin
        begin = time()
        if len(games)<200:
            break
        offset += 1
        print(f"{present} : {int(10000*present/27000)}% : {eT(duration*(135-offset))}")
