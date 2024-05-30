import itertools

N, M = map(int, input().split())
lstNo = [i for i in range(1, N+1)]

for num in itertools.combinations(lstNo, M):
    for n in num:
        print(n, end=' ')
    print()