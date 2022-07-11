import csv
import requests

API = "https://www.speedrun.com/api/v1/"

print('[')

mods = [
['jnz49qqj', 'Garsh', 9083],
['1xyyq0zx', 'mossranking', 4909],
['qxkqvo9x', 'jannik323', 12067],
['dx35zg7j', 'Tron_Javolta', 4793],
['zx7gd1yx', '1', 22000]
]

with open("runners.csv", 'r') as csvfile:
    file = csv.reader(csvfile)

    for i in mods:
        if i:
            data = requests.get(f"{API}users/{i[1]}").json()
            if data["data"]["location"]:
                flag = f":flag_{data['data']['location']['country']['code']}:"
            else:
                flag = ":united_nations:"
            print(i[1])
            print(flag)
            print()
