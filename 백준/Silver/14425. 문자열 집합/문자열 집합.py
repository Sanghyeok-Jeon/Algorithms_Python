N, M = map(int, input().split())
S = set(input() for _ in range(N))

answer = 0
for _ in range(M):
    if input() in S:
        answer += 1

print(answer)