S = input()

ucpc = 0
for s in S:
    if ucpc == 0:
        if s == 'U':
            ucpc += 1
    elif ucpc == 1:
        if s == 'C':
            ucpc += 1
    elif ucpc == 2:
        if s == 'P':
            ucpc += 1
    elif ucpc == 3:
        if s == 'C':
            ucpc += 1

if ucpc == 4:
    print('I love UCPC')
else:
    print('I hate UCPC')