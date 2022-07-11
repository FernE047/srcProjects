import requests
from textos import embelezeTempo as eT

def getGameID(gameName):
    return requests.get(f"{API}games?name={gameName}").json()["data"][0]['id']
    

API = "https://www.speedrun.com/api/v1/"

gameID = getGameID("dadish")

pendingRuns = requests.get(f"{API}runs?game={gameID}&status=new&max=200").json()["data"]

total = 0

for run in pendingRuns:
    total += run['times']['primary_t']

print(total)
print(eT(total))
