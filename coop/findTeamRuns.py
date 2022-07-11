import csv
import requests
from time import time
from utils import prettifyTime as pT

guests = set()

API = "https://www.speedrun.com/api/v1/"

CSVROWS = 6712 #how many lines the coopCategories.csv has. To make better time predictions

print("percentage : line n : last cat : runs total : time to end")
offset = 0
r = 0
with open("coopCategories.csv","r", encoding = 'utf-8') as file:
    reader = csv.reader(file,delimiter=";")
    with open("allRuns.csv","w",newline = "", encoding = 'utf-8') as file2:
        writer = csv.writer(file2,delimiter = ';')
        with open("guests.csv","w",newline = "", encoding = 'utf-8') as file3:
            writerGuests = csv.writer(file3,delimiter = ';')
            n = 0
            begin = time()
            for categoryID in reader:
                n += 1
                offset = 0
                lastRuns = None
                while True:
                    data = requests.get(f"{API}runs?category={categoryID}&max=200&offset={offset * 200}&orderby=date&direction=asc").json()['data']
                    if data:
                        runsCoop = [run for run in data if len(run['players'])>1]
                        if runsCoop:
                            for run in runsCoop:
                                players = []
                                for player in run['players']:
                                    if 'id' in player:
                                        players.append(player['id'])
                                    else:
                                        players.append(player['name'])
                                        if len(player['name']) == 8:
                                            guests.add(player['name'])
                                            writerGuests.writerow([player['name']])
                                r += 1
                                writer.writerow(players)
                        if offset==49:
                            lastRuns = data.copy()
                            break
                    if len(data)<200:
                        break
                    offset += 1
                if lastRuns:
                    while True:
                        data = requests.get(f"{API}runs?category={categoryID}&max=200&offset={offset * 200}&orderby=date&direction=desc").json()['data']
                        if data:
                            for run in data:
                                if run in lastRuns:
                                    offset = 49
                                    break
                                if len(run['players']) > 1:
                                    players = []
                                    for player in run['players']:
                                        if 'id' in player:
                                            players.append(player['id'])
                                        else:
                                            players.append(player['name'])
                                            if len(player['name']) == 8:
                                                guests.add(player['name'])
                                                writerGuests.writerow([player['name']])
                                    r += 1
                                    writer.writerow(players)
                            if offset==49:
                                break
                        offset += 1
                end = time()
                singleDuration =  (end - begin)/n
                duration = (CSVROWS-n) * singleDuration
                print(f"{n*100//CSVROWS}% : {n} : {categoryID} : {r} : {pT(duration)}")
