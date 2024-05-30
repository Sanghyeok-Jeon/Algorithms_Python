data = input()
happy = 0
sad = 0

i = 0
while i < len(data):
    if data[i] == ':':
        if data[i+1] == '-' and i < len(data):
            if data[i+2] == ')' and i < len(data):
                happy += 1
                i += 3
            elif data[i+2] == '(' and i < len(data):
                sad += 1
                i += 3
        else:
            i += 2
    else:
        i += 1

if happy == 0 and sad == 0:
    print('none')
elif happy == sad:
    print('unsure')
else:
    print('happy' if happy > sad else 'sad')