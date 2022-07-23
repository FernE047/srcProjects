import requests

API = "https://www.speedrun.com/api/v1/"

def getUser(nickname):
    data = requests.get(f"{API}users?lookup={nickname}").json()

    if not data:
        return click.echo(
            f"{nickname} could not be found."
        )

    if data["data"][0]["location"]:
        flag = f":flag_{data['data'][0]['location']['country']['code']}:"
    else:
        flag = ":united_nations:"

    return {'id':data["data"][0]["id"],
            'name':data["data"][0]["names"]["international"],
            'flag':flag}

runners = ["MechanicalSnail"]
print(len(runners))
for r in runners:
    print(getUser(r))
