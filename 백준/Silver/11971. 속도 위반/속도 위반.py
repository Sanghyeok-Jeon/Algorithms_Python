N, M = map(int, input().split())

limit = []
for _ in range(N):
    d, v = map(int, input().split())
    for _ in range(d):
        limit.append(v)

actual = []
max_over = 0
km = 0
for _ in range(M):
    d, v = map(int, input().split())
    for _ in range(d):
        max_over = max(max_over, v - limit[km])
        km += 1

print(max_over)