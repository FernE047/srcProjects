import requests

def getRuns(mod,minimo):
    offset = minimo//200
    total = offset*200
    while offset*200 < 10000:
        data = requests.get(f"{API}runs?examiner={mod}&orderby=date&direction=asc&offset={offset * 200}&max=200").json()
        if 'data' not in data:
            return 0
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

API = "https://www.speedrun.com/api/v1/"

minimo = 1500
moderators = [('v8192kpx', 'SpeedNintendo', 1552), ('jn39g1qx', 'randomidiot13', 7541), ('jmo29wy8', 'Tegron', 1720), ('5j54m68v', 'Punchy', 2293), ('y8d00plx', 'plank', 1932), ('48ge6kyj', 'maxylobes', 1753), ('kj9p77x4', 'dha', 15749), ('jnz49qqj', 'Garsh', 9083), ('y8der3mj', 'Valmerix', 1617), ('qjn1wzw8', 'Otterstone_Gamer', 14673), ('qjnqro2j', 'Cytruss', 4957), ('8qzo95o8', 'TRLittleToaster', 1898), ('qjn1mw8m', 'AprilSR', 1806), ('816q54lx', 'AslanTZ', 1504), ('68wk0748', 'HowDenKing', 5932), ('1xy3wpwj', 'Fioresa', 2489), ('48grepxp', 'seckswrecks', 2503), ('o864zm0j', 'Vapo', 4479), ('1xyk10y8', 'Marlin', 2326), ('0jm5z0ox', 'truegen', 2066), ('68wrnv3j', 'Lmjacks', 1577), ('8rpm0e3j', 'caeyo', 1701), ('98rnvp3x', 'Symystery', 3354), ('v8lyv4jm', 'MarvJungs', 6058), ('18v52d5j', 'Spaceman', 3977), ('pj0n70m8', 'FrostyZako', 3106), ('qjopronx', 'Tomatobird8', 4101), ('98rre381', 'Storster', 1935), ('18q3mnqj', 'Reverse', 2777), ('v18q90jn', 'Jumpyluff', 3994), ('48g92r2x', 'afnannen136', 5387), ('5j5rgqxv', 'Kieron', 2126), ('qjo9k3j6', 'Maximum', 6966), ('v81pk5q8', 'Tenka', 3705), ('8ge265yj', 'jackzfiml', 1894), ('qj2gv68k', 'ROMaster2', 4104), ('v81md938', 'Wipeoutjack7', 1889), ('0jml3y81', 'swordsmankirby', 6606), ('0jm0gqz8', 'Doka', 1524), ('y8dpd986', 'amyrlinn', 1853), ('5j52r5zj', 'R0main', 5192), ('kj904grj', 'Oreo321', 1995), ('18qm6oxn', 'DevilSquirrel', 2043), ('qxkvn9j0', 'Heki', 1807), ('jprme448', 'ElTreago', 1534), ('j5woeenj', 'EthaN.', 2080), ('dx3593qj', 'starsmiley', 4965), ('1xy1pmxr', '_-_STAR_fox_-_', 1910), ('qj2yyn8k', 'Deln', 5028), ('dx354ejl', 'Drakodan', 2675), ('1xy7pnxr', 'Winslinator', 2839), ('qxkvvq2j', 'relievedliberty', 2131), ('y8dg6vm8', 'hirexen', 3315), ('7j424wx1', 'authorblues', 1573), ('kj92m4r8', 'Nordanix', 3577), ('68wne448', 'FelipeNascimento83', 1659), ('v18q6wjn', 'Mhmd_FVC', 3413), ('1xyrqdwj', 'Tomppaa', 1600), ('e8e6r7j0', 'Plumato', 3024), ('5j5d73n8', 'MaxyneCash', 2742), ('kj96k7j4', 'Saradoc', 2243), ('qjnzw4jm', 'roopert83', 2203), ('5j51v3w8', 'DarQ_Massacres', 2652), ('v18qowjn', 'PeteThePlayer', 2306), ('dx3g4k8l', 'Mattmatt', 1742), ('qjo2pne8', 'Ico', 1557), ('7j4rq5v8', 'Sm_Izumi', 1816), ('1xyyq0zx', 'mossranking', 4909), ('pj062y9j', 'MaximalMegaminx', 1651), ('jp4odpkj', 'gotutiyan', 2456), ('8e913qdj', 'VyPr', 2064), ('y8dgv458', 'JokerFactor', 2030), ('61xygzxr', 'Cyberdemon531', 1597), ('98rv0dqj', 'zir0nic', 2717), ('98rk96x1', 'toca_1', 5489), ('dx3qv2jl', 'Dyceron', 1618), ('18vo5nxl', 'Californ1a', 2017), ('lv8lm4jm', 'BmanRulesYou21', 1511), ('qxk02980', 'Riekelt', 2019), ('qj2yr9n8', 'Betsruner', 1570), ('qj2gnml8', 'goadiroth', 1813), ('x7q6qy08', 'Bob-chicken', 1783), ('j4rl00w8', 'FrostySR', 4238), ('98r0z381', 'DrYoshiyahu', 1651), ('98r7g73j', 'Sayuri', 1672), ('8ge6w47j', 'Walgrey', 2701), ('0jm3r3z8', 'Mipha', 6138), ('18qwrkw8', 'bendersrus', 1611), ('1xywp9z8', 'RaggedDan', 1629), ('v8142eq8', 'NuMetalz', 1880), ('8l060pv8', 'DotALotTroller', 3284), ('86vevq5j', 'BartekIsBad', 3158), ('zx7mknvx', 'DunkelGotik', 2458), ('7j4v6dj1', 'RubberDuckyAssassin', 3964), ('1xyy7pyx', 'Motorjam', 3046), ('1xyylnyx', 'Zambrini', 1997), ('qxk6eok8', 'NihilistComedyHour', 1862), ('48ge292j', 'g0goTBC', 1585), ('68wlgyzj', 'Oxknifer', 2785), ('j2y6v5o8', 'THiEF_HD209', 3005), ('48grmrxp', 'Saiyanz', 1512), ('v814y538', 'Neural89', 1833), ('18vk6oej', 'SHiFT', 5668), ('e8e9l0pj', 'slippy318', 5360), ('1xyplgmx', 'KingSnake377', 1548), ('5j5vw1g8', 'Meep_Moop', 2447), ('y8d3z5x6', 'Dugongue', 2007), ('dx3vw68l', 'andypanther', 1875), ('dx3p0ok8', 'meauxdal', 1583), ('5j519g8v', 'loafofbread', 2124), ('qjo22ke8', 'Tech', 5335), ('qjnzo1wj', 'NerdyNester', 1973), ('1xyrp0nj', 'Penguin', 1776), ('8wk9o7q8', 'french', 3590), ('pj0g75mx', 'ffleret', 2655), ('r5j5onxv', 'Tezur0', 2672), ('qjoz6gn8', 'diggity', 1569), ('e8enep80', 'Goodigo', 2115), ('v81kdrjp', 'CaneofPacci', 1757), ('18qkovq8', 'Th3on3C', 1542), ('48gnmw2j', 'Shiven', 1919), ('48g4mnp8', 'Vakala', 1515), ('v8l03548', 'LouLouCore', 1762), ('v8ll6l28', 'Komali', 1886), ('68wl4ovj', 'Msushi', 1569), ('kjpn2lkx', 'calamity_', 1743), ('v8l0vdr8', 'Bullets', 1512), ('18qkl78n', 'Slevanas', 3501), ('x7q9g1v8', 'felipereis11011', 3549), ('0jmoeey8', 'MystwalkerMX7', 2584), ('qxko0280', 'Nimputs', 2926), ('qxkv1r6j', 'KunoDemetries', 2141), ('18qr5wjn', 'Klooger', 4286), ('8e9nz3oj', 'BOZAK_115', 2850), ('5j5dqrz8', 'Hydrus', 2771), ('o86w22qx', 'Demolition14', 2123), ('0jmvy6nj', 'Shiinyu', 2500), ('jn3k3o4x', 'RedMooschrom', 2275), ('kjp4qz2j', 'Crep', 1883), ('e8e6wdj0', 'eLmaGus', 1607), ('xy5k04w8', 'Insert', 4040), ('8l0rl9v8', 'Reni', 13702), ('o86y93wj', 'dlimes13', 2944), ('1xymkgzx', 'nhaar', 1560), ('18v7ky8l', 'AeonFrodo', 5401), ('qjn3w4xm', 'Hypnoshark', 1600), ('18qr7qjn', 'Thebpg13', 2657), ('e8ez0lp8', 'Alexo', 1982), ('pj0g27rx', 'bryonato', 1910), ('qxkqvo9x', 'jannik323', 12067), ('zx719vrx', 'Vizu', 2106), ('v8lg02jm', 'dkr_paddy', 1641), ('qj22r6jk', 'charlocharlie', 3436), ('18q0nq7j', 'luigi100', 2221), ('qxkp4d7j', 'terter', 3861), ('48grk57x', 'Kromer', 1737), ('dx35zg7j', 'Tron_Javolta', 4793), ('18venp2j', 'remotelogin', 1644), ('o867gpjz', 'Teo-', 1607), ('zx7m5yx7', 'MrsGizamaluke', 2140), ('kj9rz7j4', 'Pottoww', 1816), ('kj95ky78', 'J_duude', 1729), ('qxk1k2j0', 'PiePusher11', 1616), ('j0nvnk98', 'Rayu_', 2197), ('qxklwp68', 'TomatoTom', 1987), ('kjp6ww58', 'cestpatou', 1762), ('1xyy6vxr', 'Ewil', 3456), ('18v2v2jl', 'miniomegaking', 2024), ('kj9r9g7j', 'Zenkoina', 2180), ('48g562yj', 'WiiSuper', 4213), ('qjnzdwjm', 'PresJPolk', 2255), ('8qz33108', 'LilJapKid', 4432), ('kj9407x4', 'Fireball', 1753), ('y8dwr45j', 'Kaopoke', 2082), ('qxkge2j0', 'Valientlink', 2258), ('eo86qwxz', 'CriticalCyd', 3201), ('98rl53w8', 'eldiab', 2062), ('8l030748', 'fishes', 1577), ('dx359qjl', 'EBen', 1699), ('kjp4onyj', 'hoxi', 2529), ('j033wq3j', 'Yummy_Bacon5', 1537), ('x356nrej', 'PolariTOON', 1950), ('7j4z42wx', 'Failmore', 1676), ('zx77w50x', 'CrazyCalv', 1547), ('8e9k717j', 'Solderq35', 7545), ('x7qe61r8', 'Middzz73', 1827), ('qxkol2k8', 'Ponyah', 2594), ('v8l6lgv8', 'XeroGoFast', 2834), ('x7q663v8', 'Jaaay', 1705), ('86n409qx', 'Turtlespyder', 5037), ('kjprgok8', 'WindMark', 7051), ('1xyrv0mj', 'mobius', 1750), ('v81o6wlx', 'DylCat', 1685), ('kj9ow1wj', 'Massive', 2279), ('y8d2kqoj', 'xe', 1749), ('jo3kl6nj', 'sirtymoo', 3218), ('jo3rdplj', 'sfme', 1526), ('e8e0oqpj', 'chimkin', 1848), ('kjp4owkj', 'Quantum', 4282), ('o86pw5jz', 'HDlax', 1724), ('o86r708z', 'Riidolsk', 1518)]

offset = 61
try:
    while True:
        games = requests.get(f"{API}games?offset={offset*200}&max=200&embed=moderators").json()['data']
        for game in games:
            for moderator in game['moderators']['data']:
                idd = moderator['id']
                if idd not in [a[0] for a in moderators]:
                    names = moderator['names']
                    if 'international' in names:
                        name = names['international']
                    elif 'japanese' in names:
                        name = names['japanese']
                    elif len(names.keys()):
                        name = names[list(names.keys())[0]]
                    else:
                        name = idd
                    if name == '1':
                        continue
                    runs = getRuns(idd,minimo)
                    if runs >= minimo:
                        if len(moderators) >= 201:
                            minimo = min([mod[2] for mod in moderators])
                            moderators.pop([moderators.index(worst) for worst in moderators if worst[2]==minimo][0])
                            minimo = min([mod[2] for mod in moderators])
                        moderators.append((idd,name,runs))
                        print(f"{moderators[-1]},")
        present = 200 * offset + 200
        print(f"{present} : {int(10000*present/26300)/100}% : {minimo}")
        if len(games)<200:
            break
        offset += 1
except:
    print("BACKUP")
print(offset)
print()
print(moderators)
print()
print(minimo)
print()
