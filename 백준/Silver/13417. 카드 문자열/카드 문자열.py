from collections import deque

T = int(input())
for _ in range(T):
    N = int(input())
    cards = list(input().split())

    q = deque()
    for card in cards:
        if len(q):
            if ord(card) <= ord(q[0]):
                q.appendleft(card)
            else:
                q.append(card)
        else:
            q.append(card)

    print(''.join(q))