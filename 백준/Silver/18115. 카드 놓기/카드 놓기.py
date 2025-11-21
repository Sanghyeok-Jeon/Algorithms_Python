from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
operations = list(map(int, input().split()))

q = deque()
for i in range(N):
    card = i + 1
    operation = operations[N - 1 - i]

    if operation == 1:
        q.appendleft(card)
    elif operation == 2:
        first_card = q.popleft()
        q.appendleft(card)
        q.appendleft(first_card)
    elif operation == 3:
        q.append(card)

print(*q)