N = int(input())
mirror = [input() for _ in range(N)]
K = int(input())

if K == 1:
    print('\n'.join(mirror))
elif K == 2:
    for i in range(N):
        print(mirror[i][::-1])
else:
    for i in range(N-1, -1, -1):
        print(mirror[i])