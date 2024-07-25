N = int(input())

for i in range(N+2):
    if 1 <= i <= N:
        print('@' + ' ' * N + '@')
    else:
        print('@' * (N + 2))