import requests
import csv

API = "https://www.speedrun.com/api/v1/"

def guestRuns(mod,guest):
    offset = 0
    total = 0
    while offset*200 < 10000:
        data = requests.get(f"{API}runs?examiner={mod}&guest={guest}&orderby=date&direction=asc&offset={offset * 200}&max=200").json()
        if 'data' not in data:
            print('a')
            continue
        else:
            data = data["data"]
        total += len(data)
        offset += 1
        if len(data) < 200:
            return total
    return total

def getRuns(mod,minimo):
    offset = minimo//200
    while offset*200 >= 10000:
        offset = 49
    total = offset*200
    while offset*200 < 10000:
        data = requests.get(f"{API}runs?examiner={mod}&orderby=date&direction=asc&offset={offset * 200}&max=200").json()
        if 'data' not in data:
            offset = 0
            continue
        else:
            data = data["data"]
        total += len(data)
        offset += 1
        if len(data) < 200:
            return total
    lastRuns = data.copy()
    offset = 0
    while True:
        data = requests.get(f"{API}runs?examiner={mod}&orderby=date&direction=desc&offset={offset * 200}&max=200").json()["data"]
        offset += 1
        for run in data:
            if run in lastRuns:
                return total
            else:
                total += 1
    return total

moderators = [['kj9p77x4', 'dha', 29502,":flag_it:",guestRuns('kj9p77x4','n/a')],
              ['8l0rl9v8', 'Reni', 21361,":flag_gb:",guestRuns('8l0rl9v8','n/a')]]
with open('moderators.csv','r') as file:
    reader = csv.reader(file,delimiter = ',')
    for moderator in reader:
        if moderator[1].lower() in ['dha','reni']:
            continue
        moderator[2] = int(moderator[2])
        print(moderator[1] + ', ')
        data = requests.get(f"{API}users/{moderator[0]}").json()["data"]
        if data["location"]:
            flag = f":flag_{data['location']['country']['code']}:"
        else:
            flag = ":united_nations:"
        if flag == ":flag_ca/qc:":
            flag = ":flag_ca:"
        elif flag == ":flag_gb/eng:":
            flag = ":flag_gb:"
        moderator.append(flag)
        moderator.append(guestRuns(moderator[0],'n/a'))
        moderator[2] = getRuns(moderator[0],moderator[2])
        moderators.append(moderator)
moderators.sort(
    key=lambda x: x[2] - x[4], reverse=True
)

import datetime

print(moderators)

print(datetime.datetime.now().date())

position = 0
lastValue = float('inf')

for n, i in enumerate(moderators):
    value = i[2] - i[4]
    if value != lastValue:
        position = n + 1
    lastValue = value
    print(
        f"`{position}.`{i[3]}`{i[1]} {' ' * (22-len(str(n+1))-len(i[1]))} {value}`"
    )
