import pyperclip

print("digite o link")
link = input()
while True:
    input()
    text = pyperclip.paste()
    text = text[19:]
    text = text.split('.')[0]
    numbers = text.split(':')
    if len(numbers) == 2:
        seconds = int(numbers[0])*60+int(numbers[1])-5
    elif len(numbers) >= 3:
        seconds = int(numbers[0])*3600+int(numbers[1])*60+int(numbers[2][:2])-5
    else:
        seconds = int(numbers[0])-5
    print(numbers)
    print(seconds)
    pyperclip.copy( link+"&t=" + str(seconds) )
