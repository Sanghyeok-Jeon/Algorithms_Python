while True:
    abc = sorted(list(map(int, input().split())))
    if abc == [0, 0, 0]:
        break

    if abc[2] >= abc[0] + abc[1]:
        print('Invalid')
    else:
        set_abc = set(abc)
        if len(set_abc) == 1:
            print('Equilateral')
        elif len(set_abc) == 2:
            print('Isosceles')
        else:
            print('Scalene')