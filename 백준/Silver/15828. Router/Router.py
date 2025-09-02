from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
q = deque()
while True:
    num = int(input())

    if num == -1:
        break

    if num == 0:
        q.popleft()
    else:
        if len(q) < N:
            q.append(num)

if len(q):
    print(*q)
else:
    print('empty')