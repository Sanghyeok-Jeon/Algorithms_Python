tc = 1
while True:
    o, w = map(int, input().split())
    result = ''

    if (o, w) == (0, 0):
        break

    while True:
        ef, n = input().split()

        if (ef, n) == ('#', '0'):
            if w <= 0:
                result = 'RIP'
            elif o // 2 < w < o * 2:
                result = ':-)'
            else:
                result = ':-('

            print('{} {}'.format(tc, result))

            break

        if result == 'RIP':
            continue

        if ef == 'E':
            w = 0 if w - int(n) < 0 else w - int(n)
            if w == 0:
                result = 'RIP'
        elif ef == 'F':
            w += int(n)

    tc += 1