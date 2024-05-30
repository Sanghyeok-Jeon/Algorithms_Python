card = list(range(1, 21))

for _ in range(10):
    s, e = map(int, input().split())
    start = s - 1
    end = e

    newCard = card[:start] + card[start:end][::-1] + card[end:]
    card = newCard

print(*card)