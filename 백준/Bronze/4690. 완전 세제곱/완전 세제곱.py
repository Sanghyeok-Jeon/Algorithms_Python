for a in range(2, 101):
    for b in range(2, a-2):
        for c in range(b, a-1):
            for d in range(c, a):
                if a ** 3 == b ** 3 + c ** 3 + d ** 3:
                    print('Cube = {}, Triple = ({},{},{})'.format(a, b, c, d))