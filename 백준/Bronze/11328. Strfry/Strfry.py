N = int(input())
for _ in range(N):
    s1, s2 = input().split()

    if sorted(s1) == sorted(s2):
        print('Possible')
    else:
        print('Impossible')