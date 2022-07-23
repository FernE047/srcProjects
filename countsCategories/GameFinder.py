import csv
import requests

API = "https://www.speedrun.com/api/v1/"

def anyRequests(text):
    while True:
        try:
            return requests.get(text).json()['data']
        except:
            print("connection")

def getAllPlatforms():
    offset = 0
    platforms = {}
    while offset*200 < 10000:
        data = anyRequests(f"{API}platforms?offset={offset * 200}&max=200")
        platforms = {p['id'] : p['name'] for p in data}
        offset += 1
        if len(data) < 200:
            return platforms
    return platforms

PLATS = getAllPlatforms()

offset = 0
with open('christmas.csv','w', newline='',encoding = 'utf-8') as file:
    writer = csv.writer(file,delimiter=';')
    writer.writerow(['name','platforms','url','categories FG','levels','categories IL','total'])
    while True:
        games = anyRequests(f"{API}games?offset={offset*200}&max=200&embed=categories,levels,variables")
        for game in games:
            row = []
            names = game['names']
            if 'international' in names:
                name = names['international']
            elif 'japanese' in names:
                name = names['japanese']
            elif 'twitch' in names:
                name = names['twitch']
            elif len(names.keys()):
                name = names[list(names.keys())[0]]
            else:
                name = game['id']
            weblink = game['weblink']
            platforms = [PLATS[a] for a in game['platforms']]
            categoriesIL = []
            categoriesFG = []
            for category in game['categories']['data']:
                if category['type'] == 'per-game':
                    categoriesFG.append(category)
                else:
                    categoriesIL.append(category)
            levels = game['levels']['data']
            variables = game['variables']['data']
            totalFG = 0
            for categoria in categoriesFG:
                category = 1
                for variable in variables:
                    if variable['is-subcategory']:
                        if variable['scope']['type'] in ('global','full-game'):
                            multiplica = True
                            if 'category' in variable:
                                if variable['category']:
                                    if categoria['id'] != variable['category']:
                                        multiplica = False
                            if multiplica:
                                category *= len(variable['values']['values'])
                totalFG += category
            totalIL = 0
            for level in levels:
                for categoria in categoriesIL:
                    category = 1
                    for variable in variables:
                        if variable['is-subcategory']:
                            if variable['scope']['type'] in ('global','all-levels','single-level'):
                                multiplica = True
                                if 'category' in variable:
                                    if variable['category']:
                                        if categoria['id'] != variable['category']:
                                            multiplica = False
                                if 'level' in variable['scope']:
                                    if variable['scope']['level']:
                                        if level['id'] != variable['scope']['level']:
                                            multiplica = False
                                if multiplica:
                                    category *= len(variable['values']['values'])
                    totalIL += category
            row.append(name)
            row.append(", ".join(platforms))
            row.append(weblink)
            row.append(totalFG)
            row.append(len(levels))
            row.append(totalIL)
            row.append(' ')
            writer.writerow(row)
            print(row)
        present = 200 * offset + 200
        print(f"{present} : {int(10000*present/29500)}% : {weblink}")
        if len(games)<200:
            break
        offset += 1
