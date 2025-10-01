N, K = map(int, input().split())
friends = [int(input()) for _ in range(N)]

visited = [False] * N
current = 0
steps = 0

is_possible = False
while not visited[current]:
    if current == K:
        is_possible = True
        break

    visited[current] = True
    current = friends[current]
    steps += 1

if is_possible:
    print(steps)
else:
    print(-1)