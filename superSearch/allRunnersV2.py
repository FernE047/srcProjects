from random import randint
from random import choices
import requests

def findUsers(term):
    if len(term) < 2:
        return [[] for a in range(20)]
    global NAMES
    global iterations
    iterations += 1
    print(f"{iterations} {term}")
    total = []
    total = requests.get(f"{ajax}{term}").json()
    return total

def loopLetters(term = ""):
    global ALPHA
    allNames = []
    for letter in ALPHA:
        term += letter
        search = findUsers(term)
        if len(search) >= 20:
            allNames += loopLetters(term)
        else:
            for name in allNames:
                print(name)
                if name["category"] == "Users":
                    allNames.append(name['label'])
        term = term[:-1]
    return allNames

ajax = "https://www.speedrun.com/ajax_search.php?term="
ALPHA = ['_','-','.','|','@', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
iterations = 0
total = loopLetters()
