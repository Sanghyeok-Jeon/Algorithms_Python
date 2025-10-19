from collections import deque

N, K, M = map(int, input().split())

q = deque(range(1, N + 1))
direction = 1
cnt = 0
while len(q):
    if direction == 1:
        q.rotate(-(K-1))
        print(q.popleft())
    else:
        q.rotate(K-1)
        print(q.pop())

    cnt += 1

    if cnt == M:
        cnt = 0
        direction *= -1