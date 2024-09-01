N, M = map(int, input().split())

friends = [[] for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    friends[A - 1].append(B)
    friends[B - 1].append(A)

for i in range(N):
    print(len(friends[i]))