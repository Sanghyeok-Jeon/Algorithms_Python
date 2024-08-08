T = int(input())
for i in range(1, T + 1):
    sides = sorted(list(map(int, input().split())))

    print('Case #{}:'.format(i), end=' ')
    A, B, C = sides
    if A == B == C:
        print('equilateral')
    elif (A == B and A + B > C) or (B == C and A + B > C):
        print('isosceles')
    elif A != B and B != C and C != A and A + B > C:
        print('scalene')
    else:
        print('invalid!')