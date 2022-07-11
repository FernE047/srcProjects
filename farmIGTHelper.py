import pyperclip

print("digite o link")
link = input()
seconds = 0
while True:
    input()
    text = pyperclip.paste()
    for line in text.split('\n')[1:-1]:
        a = line.split('": ')
        a[0] = a[0][3:]
        if a[0] == 'vct':
            a[1] = a[1][1:]
            while not a[1][-1].isnumeric():
                a[1] = a[1][:-1]
            seconds = int(float(a[1]))-30
            print(seconds)
            break
    pyperclip.copy( link+"&t=" + str(seconds) )
