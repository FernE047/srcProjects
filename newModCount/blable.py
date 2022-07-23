with open("bbb.txt",'r') as file:
    line = file.readline()
    mods = line.split(")")
    mods.pop(-1)
    print(len(mods))
    for i in range(len(mods)):
        try:
            mods[i] = int(mods[i][mods[i].rfind(",")+1:])
        except:
            print(mods[i])
            print(i)
    
