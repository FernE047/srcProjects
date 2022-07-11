import requests

API = 'https://www.speedrun.com/api/v1/'

def runsVerified(idd):
    offset = 0
    total = 0
    while offset*200 < 10000:
        data = requests.get(f"{API}runs?examiner={idd}&status=verified&orderby=date&direction=asc&offset={offset * 200}&max=200").json()["data"]
        total += len(data)
        offset += 1
        if len(data) < 200:
            return total
    lastRuns = data.copy()
    offset = 0
    while True:
        data = requests.get(f"{API}runs?examiner={idd}&status=verified&orderby=date&direction=desc&offset={offset * 200}&max=200").json()["data"]
        offset += 1
        for run in data:
            if run in lastRuns:
                return total
            else:
                total += 1
    return total

def runsRejected(idd):
    offset = 0
    total = 0
    while offset*200 < 10000:
        data = requests.get(f"{API}runs?examiner={idd}&status=rejected&offset={offset * 200}&max=200").json()["data"]
        total += len(data)
        offset += 1
        if len(data) < 200:
            return total
    return total

def getRuns(idd,name):
    v = runsVerified(idd)
    r = runsRejected(idd)
    t = v + r
    line = name
    line += "\n```total     : " + str(t)
    line += "\nverifieds : " + str(v)
    line += "\nrejecteds : " + str(r) + "```"
    print(line)

def getRunner(username):
    """Check if the user exists, return his data if any, otherwise False."""
    data = requests.get(
        f"{API}users?lookup={username}"
    ).json()
    print(data['data'][0]['names'])
    return data['data'][0]['id'] if data["pagination"]["size"] > 0 else False

name = '1'
runnerId = getRunner(name)
print(runnerId)
#getRuns(runnerId,name)
