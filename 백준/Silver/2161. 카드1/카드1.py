from collections import deque

N = int(input())
card = deque(list(range(1, N + 1)))

answer = []
while True:
    if len(card) == 1:
        answer.append(card[0])
        break

    first = card.popleft()
    answer.append(first)

    second = card.popleft()
    card.append(second)

print(*answer)