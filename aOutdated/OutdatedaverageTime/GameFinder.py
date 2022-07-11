import csv
import requests

def timefy(time):
    minutes = time/60
    hours = minutes/60
    hours = int(hours)
    minutes = int(minutes)%60
    seconds = int(time)%60 + time - int(time)
    hours = str(hours)
    while len(hours) < 3:
        hours = '0' + hours
    minutes = str(minutes)
    seconds = str(seconds)
    while len(minutes) < 2:
        minutes = '0' + minutes
    if seconds.find('.') == -1:
        seconds += '.000'
    if seconds.find('.') == 1:
        seconds = '0' + seconds
    while len(seconds) < 6:
        seconds += '0'
    return ":".join((hours,minutes,seconds[0:6]))

API = "https://www.speedrun.com/api/v1/"

PLATS = {'o064vv63' : '2DS XL','8gejmne3' : '3DO Interactive Multiplayer','vm9vw163' : '3DS Backwards Compatibility','mx6pow93' : 'Acorn Archimedes','o7e2dj6w' : 'Advanced Pico Beena','mr6ko5ez' : 'Amazon Fire TV','gde32g6k' : 'Amiga','wxeo0der' : 'Amiga CD32','5negykey' : 'Amstrad CPC','gde3vw9k' : 'Amstrad PCW','3167pk6q' : 'Analogue Nt','kz9wlm6p' : 'Analogue Nt Mini','gz9qg3e0' : 'Analogue Super Nt','lq60nl94' : 'Android','n5e15292' : 'AndroidTV','w89ryw6l' : 'Apple II','7g6mom9r' : 'Apple IIGS','vm9vz163' : 'Apple TV','vm9vn63k' : 'Arcade','mr6k206z' : 'Arduboy','o0644863' : 'Atari 2600','lq60ol64' : 'Atari 5200','gde33gek' : 'Atari 7800','n5e1m7e2' : 'Atari 8-bit family (400/800/XL/XE)','jm9577eo' : 'Atari Flashback','jm95oz6o' : 'Atari Jaguar','kz9wzm9p' : 'Atari Jaguar CD','o0641163' : 'Atari Lynx','n5e1g7e2' : 'Atari ST','v06dvz64' : 'backwards-compatible PlayStation 3','gz9q2390' : 'BBC Micro','n5685z6v' : 'Binary Runtime Environment for Wireless','wxeo8d6r' : 'ColecoVision','gz9qox60' : 'Commodore 64','p36n4x98' : 'Commodore CDTV','w89ryd6l' : 'Commodore VIC-20','gz9qv3e0' : 'Delta Aircraft Seats','lq60rd64' : 'Dragon 32/64','v06d394z' : 'Dreamcast','wxeo3zer' : 'DSi','gde31w9k' : 'Fairchild Channel F','gde3owek' : 'Famicom','mr6k409z' : 'Famicom Disk System','jm95k79o' : 'FM Towns','gz9qkx90' : 'Game & Watch','n5683oev' : 'Game Boy','3167d6q2' : 'Game Boy Advance','gde3g9k1' : 'Game Boy Color','vm9v3ne3' : 'Game Boy Interface','7m6yvw6p' : 'Game Boy Player','31672keq' : 'Game.Com','4p9z06rn' : 'GameCube','5neg076y' : 'Gizmondo','o064z1e3' : 'Google Stadia','gz9qwx90' : 'Graphing Calculator','w89rwwel' : 'HTC Vive','jm9517eo' : 'Hyperscan','o0643893' : 'Intellivision','gde3xgek' : 'iOS','mr6k159z' : 'iPod','p36nd598' : 'iQue Player','nzel5r6q' : 'Java Phone','nzel3veq' : 'Leapfrog Didj','7m6ypz6p' : 'Leapster Learning Game System','n5e1n292' : 'Leapster TV','5neg7key' : 'Linux','mx6ppw63' : 'Macintosh','p36npx98' : 'Magnavox Odyssey','w89rqdel' : 'Magnavox Odyssey 2','5negp7ey' : 'Mega Sg','mx6px493' : 'MegaNet','gde3rwek' : 'MiSTer','mr6km09z' : 'MS-DOS','jm950z6o' : 'MSX','83exkk6l' : 'MSX2','83exlkel' : 'N-Gage','7g6mw8er' : 'NEC PC-88 series','o064r893' : 'NEC PC-98 series','mx6p4w63' : 'Neo Geo AES','kz9w7mep' : 'Neo Geo CD','n5e1z292' : 'Neo Geo Mini','7m6ydw6p' : 'Neo Geo Pocket Color','o7e2lj9w' : 'Neo Geo X','kz9wynep' : 'NES Classic Mini','kz9wqn9p' : 'New Nintendo 3DS','v06do394' : 'New Nintendo 3DS Virtual Console','gz9qx60q' : 'Nintendo 3DS','7g6mx89r' : 'Nintendo 3DS Virtual Console','w89rwelk' : 'Nintendo 64','83ex5v6l' : 'Nintendo 64 Disk Drive','7g6m8erk' : 'Nintendo DS','jm95z9ol' : 'Nintendo Entertainment System','kz9wdmep' : 'Nintendo Switch Lite','p36nyx98' : 'Nt Mini Noir','o064v163' : 'Nuon','v06dmz64' : 'Nvidia Shield','o064o193' : 'Oculus Quest','4p9zq09r' : 'Oculus VR','8gej5193' : 'Oric','nzeloreq' : 'Ouya','nzelrveq' : 'Palm OS','8gej2n93' : 'PC','p36n8568' : 'PC-FX','w89rjw6l' : 'Philips CD-i','n568qz6v' : 'PICO-8','wxeod9rn' : 'PlayStation','n5e17e27' : 'PlayStation 2','mx6pwe3g' : 'PlayStation 3','nzelkr6q' : 'PlayStation 4','nzeljv9q' : 'PlayStation 4 Pro','4p9zjrer' : 'PlayStation 5','o7e2vj6w' : 'Playstation Classic','wxeo5z6r' : 'Playstation Now','5negk9y7' : 'PlayStation Portable','lq60gle4' : 'Playstation TV','4p9z70er' : 'PlayStation Vita','3167od9q' : 'Plug & Play','vm9vr1e3' : 'Pokémon Mini','v06dpz64' : 'PS5 for backward compatible games','wxeo2d6r' : 'PSN Download','7g6mym6r' : 'retroUSB AVS','jm95l76o' : 'Roku','83exokel' : 'Satellaview','kz9wrn6p' : 'Sega 32X','31670d9q' : 'Sega CD','w89r3w9l' : 'Sega Game Gear','mr6k0ezw' : 'Sega Genesis','mx6p3493' : 'Sega Genesis Mini','83exwk6l' : 'Sega Master System','7m6yjz6p' : 'Sega Pico','lq60l642' : 'Sega Saturn','83expv9l' : 'SG-1000','o0641863' : 'Sharp X1','83exovel' : 'SNES Classic Mini','5negr76y' : 'Super Cassette Vision','31677k6q' : 'Super Famicom','3167jd6q' : 'Super Game Boy','n5e147e2' : 'Super Game Boy 2','83exk6l5' : 'Super Nintendo','7m6ylw9p' : 'Switch','mx6p1463' : 'Switch Virtual Console','wxeogz9r' : 'SwitchOLED','vm9vkn63' : 'Tabletop','8gejn193' : 'Tamagotchi','mx6pq4e3' : 'Tapwave Zodiac','5nego76y' : 'Texas Instruments TI-99/4A','lq604de4' : 'TI-84','4p9zprer' : 'TIC-80','3167qkeq' : 'Tiger','p36nlxe8' : 'TurboGrafx-16 CD-ROM','jm95w79o' : 'TurboGrafx-16 Mini','5negxk6y' : 'TurboGrafx-16/PC Engine','8gej8n93' : 'V.Smile','83exvv9l' : 'Valve Index','7g6m1m6r' : 'Vectrex','7g6mk8er' : 'Virtual Boy','o7e25xew' : 'Web','v06dk3e4' : 'Wii','w89rdd6l' : 'Wii Mini','8gejn93d' : 'Wii U','v06dr394' : 'Wii U Virtual Console','nzelreqp' : 'Wii Virtual Console','lq60mde4' : 'WiiU Backwards Compatibility','w89r4d6l' : 'Windows Mixed Reality','p36no5e8' : 'Windows Phone','vm9v8n63' : 'WonderSwan','n568kz6v' : 'Wonderswan Colour','n5681o9v' : 'X68000','jm95zz9o' : 'Xbox','n568oevp' : 'Xbox 360','lq60vde4' : 'Xbox 360 Arcade','o7e2mx6w' : 'Xbox One','o064j163' : 'Xbox One S','4p9z0r6r' : 'Xbox One X','o7e2xj9w' : 'Xbox Series S','nzelyv9q' : 'Xbox Series X','7m6y2zep' : 'Zeebo','n568zo6v' : 'ZX Spectrum'}

offset = 0
UNIFORME = []
with open('newyear.csv','w', newline='',encoding = 'utf-8') as file:
    writer = csv.writer(file,delimiter=';')
    writer.writerow(['name','platforms','url','IL categories','IL average time','Complete IL','FG categories','FG average time','Complete FG','Time to Complete Game'])
    while True:
        games = requests.get(f"{API}games?offset={offset*200}&max=200&embed=categories,levels,variables").json()['data']
        for game in games:
            gameID = game['id']
            row = []
            names = game['names']
            if 'international' in names:
                name = names['international']
            elif 'japanese' in names:
                name = names['japanese']
            elif 'twitch' in names:
                name = names['twitch']
            elif len(names.keys()):
                name = names[list(names.keys())[0]]
            else:
                name = game['id']
            weblink = game['weblink']
            platforms = [PLATS[a] for a in game['platforms']]
            categoriesIL = [category for category in game['categories']['data'] if category['type'] != 'per-game']
            categoriesFG = [category for category in game['categories']['data'] if category['type'] == 'per-game']
            levels = game['levels']['data']
            variables = game['variables']['data']
            totalFG = 0
            for categoria in categoriesFG:
                category = 1
                for variable in variables:
                    if variable['is-subcategory']:
                        if variable['scope']['type'] in ('global','full-game'):
                            multiplica = True
                            if 'category' in variable:
                                if variable['category']:
                                    if categoria['id'] != variable['category']:
                                        multiplica = False
                            if multiplica:
                                category *= len(variable['values']['values'])
                totalFG += category
            totalIL = 0
            for level in levels:
                for categoria in categoriesIL:
                    category = 1
                    for variable in variables:
                        if variable['is-subcategory']:
                            if variable['scope']['type'] in ('global','all-levels','single-level'):
                                multiplica = True
                                if 'category' in variable:
                                    if variable['category']:
                                        if categoria['id'] != variable['category']:
                                            multiplica = False
                                if 'level' in variable['scope']:
                                    if variable['scope']['level']:
                                        if level['id'] != variable['scope']['level']:
                                            multiplica = False
                                if multiplica:
                                    category *= len(variable['values']['values'])
                    totalIL += category
            offset2 = 0
            timesIL = []
            timesFG = []
            while True:
                bestRuns = requests.get(f"{API}games/{gameID}/records?top=1&max=200&offset={200 * offset2}").json()['data']
                for category in bestRuns:
                    isLevel = category['level']
                    if isLevel:
                        for data in category['runs']:
                            if 'run' in data:
                                run = data['run']
                                if 'times' in run:
                                    if 'primary_t' in run['times']:
                                        timesIL.append(run['times']['primary_t'])
                    else:
                        for data in category['runs']:
                            if 'run' in data:
                                run = data['run']
                                if 'times' in run:
                                    if 'primary_t' in run['times']:
                                        timesFG.append(run['times']['primary_t'])
                if not timesIL:
                    timesIL = [0]
                if not timesFG:
                    timesFG = [0]
                if len(bestRuns) < 200:
                    break
                offset2 += 1
            avgTimeIL = sum(timesIL)/len(timesIL)
            avgTimeFG = sum(timesFG)/len(timesFG)
            timeIL = totalIL * avgTimeIL
            timeFG = totalFG * avgTimeFG
            row.append(name)
            row.append(", ".join(platforms))
            row.append(weblink)
            row.append(totalIL)
            if avgTimeIL:
                row.append(timefy(avgTimeIL))
                row.append(timefy(timeIL))
            else:
                row.append('')
                row.append('')
            row.append(totalFG)
            if avgTimeFG:
                row.append(timefy(avgTimeFG))
                row.append(timefy(timeFG))
            else:
                row.append('')
                row.append('')
            time = timeFG + timeIL
            if time:
                row.append(timefy(time))
            else:
                row.append('')
            writer.writerow(row)
        present = 200 * offset + 200
        print(f"{present} : {int(10000*present/26207)}% : {name}")
        if len(games)<200:
            break
        offset += 1
