import csv
from time import sleep
from time import time
from textos import embelezeTempo as eT
import requests

API = "https://www.speedrun.com/api/v1/"

def doStop(term):
    with open('check.txt') as file:
        if file.readline() == "True":
            print(f"paramos em : {term}")
            return True
        else:
            return False

def anyRequests(text):
    while True:
        try:
            return requests.get(text).json()
        except:
            print("connection")

def compare(a,b):
    global ALPHA
    a = list(a.lower())
    b = list(b.lower())
    for i in range(min(len(a),len(b))):
        if a[i] not in ALPHA:
            a[i] = 'z'
        if b[i] not in ALPHA:
            b[i] = 'z'
        if ALPHA.index(a[i]) > ALPHA.index(b[i]):
            return "greater"
        elif ALPHA.index(a[i]) < ALPHA.index(b[i]):
            return "less"
    return "equal"

def goDown(term):
    global INITIAL
    if len(term) < len(INITIAL):
        if compare(term,INITIAL) in ("equal","less"):
            return True
    if len(term) >= len(INITIAL):
        if compare(term,INITIAL) == "less":
            return False
    print(f"go down on {term}?")
    lastPerson = anyRequests(f"{API}users?name={term}&max=1&offset=9800")
    if 'data' not in lastPerson:
        print("no")
        return False
    if not lastPerson['data']:
        print("no")
        return False
    lastPerson = lastPerson['data'][-1]['names']['international'].lower()
    if compare(term,lastPerson) == "less":
        print("no")
        return False
    else:
        print("yes")
        return True

def findUsers(term):
    global NAMES
    global iterations
    global INITIAL
    global BEGIN
    if compare(term,INITIAL) == "less":
        return set()
    offset = 0
    truePeople = set()
    while True:
        people = anyRequests(f"{API}users?name={term}&max=200&offset={200*offset}&order=asc")
        iterations += 1
        end = time()
        duration = (end-BEGIN)/iterations
        print(f"{iterations} {people['data'][-1]['names']['international']} {20000*iterations/1142000}% {eT(1142000/200 * duration)}")
        if 'data' not in people:
            break
        for person in people['data']:
            name = person['names']['international'].lower()
            if compare(name,term) in ("less","equal"):
                truePeople.add(person['id'])
            else:
                return truePeople
        if len(people['data'])<200:
            break
        offset += 1
    return truePeople

def loopLetters(term = ""):
    global ALPHA
    allIDS = set()
    for letter in ALPHA:
        if doStop(term):
            return allIDS
        term += letter
        if goDown(term):
            allIDS.union(loopLetters(term))
        else:
            allIDS.union(findUsers(term))
        term = term[:-1]
    return allIDS

allIDS = set()
with open("allRunners.csv",'r',newline = "") as file:
    reader = csv.reader(file,delimiter = ";")
    for i in reader:
        allIDS.add(i[0])
INITIAL = ''
ALPHA = ['_','-','.','|','@', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
iterations = len(allIDS)//200
BEGIN = time() - 15*iterations
allIDS.union(loopLetters())
with open("allRunners.csv",'w',newline = "") as file:
    writer = csv.writer(file,delimiter = ";")
    for ID in allIDS:
        writer.writerow([ID])
