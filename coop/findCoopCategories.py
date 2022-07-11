import csv
import requests

API = "https://www.speedrun.com/api/v1/"

offset = 0
with open("coopCategories.csv","w",newline="", encoding = 'utf-8') as file:
    writer = csv.writer(file,delimiter=";")
    while True:
        data = requests.get(f"{API}games?max=200&offset={offset *200}&embed=categories").json()["data"]
        for game in data:
            for category in game["categories"]["data"]:
                if category["players"]["value"] > 1:
                    writer.writerow([category["id"]])
        if len(data)<200:
            break
        offset+=1
        print(f"{offset*20000//30000}% : {offset} : {game['weblink']}")
	
