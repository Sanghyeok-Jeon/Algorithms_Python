M, N = map(int, input().split())

visited = [0] * (N+1)

for i in range(1, N+1):
    if i < 2:
        continue

    if not visited[i]:
        if i >= M:
            print(i)

        for j in range(i*2, N+1, i):
            visited[j] = 1