import csv

import requests

API = "https://www.speedrun.com/api/v1/"

def banned(idd):
    data = requests.get(f"{API}users/{idd}").json()['data']
    return data['role'] == 'banned'

if __name__ == "__main__":
    with open("runners.csv", 'r') as csvfile:
        with open('new.csv','w') as csvfileOutput:
            filereader = csv.reader(csvfile)
            filewriter = csv.writer(csvfileOutput)
            for name,idd,flag,_ in filereader:
                print(f"`{name}` - {flag}")
                data = [name,idd,flag,banned(idd)]
                if data[3]:
                    print("BANNED")
                print(data)
                filewriter.writerow(data)
                
