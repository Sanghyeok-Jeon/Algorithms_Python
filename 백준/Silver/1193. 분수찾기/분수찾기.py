X = int(input())

i = 1
while True:
    if (i * (i+1)) // 2 >= X:
        if i % 2:
            print('{}/{}'.format(1 + ((i * (i+1)) // 2 - X), i - ((i * (i+1)) // 2 - X)))
        else:
            print('{}/{}'.format(i - ((i * (i + 1)) // 2 - X), 1 + ((i * (i + 1)) // 2 - X)))
        break
    else:
        i += 1