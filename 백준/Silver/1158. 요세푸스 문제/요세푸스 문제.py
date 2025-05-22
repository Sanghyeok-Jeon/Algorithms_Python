from collections import deque

N, K = map(int, input().split())

answer = '<'
q = deque([n for n in range(1, N + 1)])

while True:
    if len(q) == 1:
        answer += str(q.popleft()) + '>'
        break

    for _ in range(K - 1):
        q.append(q.popleft())

    answer += str(q.popleft()) + ', '

print(answer)