num = 1
while True:
    rwl = input()

    r, w, l = 0, 0, 0
    if rwl == '0':
        break
    else:
        r, w, l = map(int, rwl.split(' '))

    if r * 2 >= (w ** 2 + l ** 2) ** 0.5:
        print('Pizza {} fits on the table.'.format(num))
    else:
        print('Pizza {} does not fit on the table.'.format(num))

    num += 1