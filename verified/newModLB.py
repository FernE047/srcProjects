import requests
import csv

API = "https://www.speedrun.com/api/v1/"
FEDATA = "https://ds.speedrun.com/_fedata/user/stats?"

modGames = {}
with open('moderators.csv','r') as file:
    reader = csv.reader(file,delimiter = ',')
    for moderator in reader:
        modGames[moderator[0]] = {}
with open('modGames.csv','r') as file:
    reader = csv.reader(file)
    for line in reader:
        modGames[line[0]][line[1]] = int(line[2])
