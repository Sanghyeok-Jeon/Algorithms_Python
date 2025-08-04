from collections import deque

N = int(input())
cards = deque()

for i in range(N, 0, -1):
    cards.appendleft(i)

    for _ in range(i):
        cards.appendleft(cards.pop())

print(*cards)