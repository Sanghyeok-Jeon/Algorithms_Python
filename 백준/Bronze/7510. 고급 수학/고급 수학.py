n = int(input())
for i in range(1, n+1):
    abc = sorted(list(map(int, input().split())))

    print('Scenario #{}:'.format(i))
    if abc[0]**2 + abc[1]**2 == abc[2]**2:
        print('yes')
    else:
        print('no')
    print()