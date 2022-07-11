import csv
import requests
from itertools import combinations as cb

API = "https://www.speedrun.com/api/v1/"

def findNames(runners):
    global DB
    runners = runners.split("+,+")
    runnersStr = ""
    for runner in runners:
        if len(runner)==8:
            if runner not in guests:
                if runner not in DB:
                    data = requests.get(f"{API}users/{runner}").json()["data"]
                    name = data['names']['international']
                    if data["location"]:
                        flag = f":flag_{data['location']['country']['code']}:"
                    else:
                        flag = ":united_nations:"
                    DB[runner] = flag+name
                runnersStr += f"; {DB[runner]}"
            else:
                runnersStr += f"; (guest){runner}"
        else:
            runnersStr += f"; (guest){runner}"
    return runnersStr[2:]

def leaderboard(result,title):
    print("\n"+title+"\n")
    
    result.sort(
        key=lambda x: x[1], reverse=True
    )

    position = 0
    lastValue = float('inf')
    with open("IDS" + title + ".csv","w",newline="", encoding = 'utf-8') as file:
        with open(title + ".csv","w",newline="", encoding = 'utf-8') as file2:
            writer = csv.writer(file,delimiter=";")
            writer2 = csv.writer(file2,delimiter=";")
            for n, i in enumerate(result):
                runners,number = i
                if number != lastValue:
                    position = n + 1
                writer.writerow([position,number,";".join(runners.split("+,+"))])
                if position <= LIMIT:
                    runners = findNames(runners)
                    print(f"{position}:{number} `{runners}`")
                    writer2.writerow([position,number,runners])
                lastValue = number

def singleRunners(runs):
    dicionario = {}
    n = 0
    for run in runs:
        for runner in run:
            if runner in dicionario:
                dicionario[runner] += 1
            else:
                dicionario[runner] = 1
                if len(runner) == 8 and runner not in guests:
                    n += 1
    result = [(runner,dicionario[runner]) for runner in dicionario]
    print(n)
    return result

def nRunners(runs,n):
    dicionario = {}
    for run in runs:
        if len(run) == n:
            run = "+,+".join(run)
            if run in dicionario:
                dicionario[run] += 1
            else:
                dicionario[run] = 1
    result = [(runner,dicionario[runner]) for runner in dicionario]
    print(len(dicionario))
    print(sum(list(dicionario.values())))
    return result

def teams(runs):
    dicionario = {}
    for run in runs:
        run = "+,+".join(run)
        if run in dicionario:
            dicionario[run] += 1
        else:
            dicionario[run] = 1
    result = [(runner,dicionario[runner]) for runner in dicionario]
    print(len(dicionario))
    print(sum(list(dicionario.values())))
    return result

def formations(runs):
    dicionario = {}
    for run in runs:
        for l in range(2,len(run)+1):
            for runners in cb(run,l):
                runners = "+,+".join(runners)
                if runners in dicionario:
                    dicionario[runners] += 1
                else:
                    dicionario[runners] = 1
    result = [(runner,dicionario[runner]) for runner in dicionario if runner in dicionario]
    print(len(dicionario))
    return result

guests = []
with open('guests.csv','r') as file:
    reader = csv.reader(file)
    for guest in reader:
        guests.append(guest)
DB = {}
LIMIT = 50
runs = []
with open("allRuns.csv","r", encoding = 'utf-8') as file:
    reader = csv.reader(file,delimiter=";")
    for run in reader:
        while not run[-1]:
            run.pop(-1)
        run.sort()
        runs.append(run)
leaderboard(singleRunners(runs),"One Person")
leaderboard(nRunners(runs,2),'Duos')
leaderboard(nRunners(runs,3),'Trios')
leaderboard(nRunners(runs,4),'Quartet')
leaderboard(nRunners(runs,5),'Quintet')
leaderboard(nRunners(runs,6),'Sextet')
leaderboard(nRunners(runs,7),'Septet')
leaderboard(nRunners(runs,8),'Eight')
leaderboard(nRunners(runs,9),'Nine')
leaderboard(nRunners(runs,10),'Ten')
leaderboard(nRunners(runs,11),'Eleven')
leaderboard(nRunners(runs,12),'Twelve')
leaderboard(nRunners(runs,13),'Thirteen')
leaderboard(nRunners(runs,14),'Fourteen')
leaderboard(nRunners(runs,15),'Fiveteen')
leaderboard(nRunners(runs,16),'Sixteen')
leaderboard(teams(runs),'Teams')
leaderboard(formations(runs),'Formations')
