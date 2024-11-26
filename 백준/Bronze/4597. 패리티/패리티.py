while True:
    bs = input()

    if bs == '#':
        break

    if bs[-1] == 'e':
        if bs[:-1].count('1') % 2:
            print(bs[:-1] + '1')
        else:
            print(bs[:-1] + '0')
    else:
        if bs[:-1].count('1') % 2:
            print(bs[:-1] + '0')
        else:
            print(bs[:-1] + '1')