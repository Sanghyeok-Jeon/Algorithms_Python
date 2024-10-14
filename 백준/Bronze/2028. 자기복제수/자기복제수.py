T = int(input())
for _ in range(T):
    N = input()
    num_N = int(N)

    target = str(num_N ** 2)

    if target[-len(N):] == N:
        print('YES')
    else:
        print('NO')