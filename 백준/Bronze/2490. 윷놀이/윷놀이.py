for _ in range(3):
    yoot = list(map(int, input().split()))

    if yoot.count(1) == 0:
        print('D')
    elif yoot.count(1) == 1:
        print('C')
    elif yoot.count(1) == 2:
        print('B')
    elif yoot.count(1) == 3:
        print('A')
    else:
        print('E')