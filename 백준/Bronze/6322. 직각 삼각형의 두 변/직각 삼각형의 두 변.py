n = 1
while True:
    a, b, c = map(int, input().split())

    if a == b == c == 0:
        break

    print('Triangle #{}'.format(n))

    if a == -1:
        if b >= c:
            print('Impossible.')
        else:
            answer = round((c ** 2 - b ** 2) ** 0.5, 3)
            if answer + b >= c:
                print('a = {:.3f}'.format(answer))
            else:
                print('Impossible.')
    elif b == -1:
        if a >= c:
            print('Impossible.')
        else:
            answer = round((c ** 2 - a ** 2) ** 0.5, 3)
            if a + answer >= c:
                print('b = {:.3f}'.format(answer))
            else:
                print('Impossible.')
    else:
        answer = round((a ** 2 + b ** 2) ** 0.5, 3)
        if a + b >= answer:
            print('c = {:.3f}'.format(answer))
        else:
            print('Impossible.')

    print()
    n += 1