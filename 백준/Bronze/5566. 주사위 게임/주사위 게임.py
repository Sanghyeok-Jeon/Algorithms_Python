N, M = map(int, input().split())
orders = [int(input()) for _ in range(N)]
dice = [int(input()) for _ in range(M)]
cnt = 0

now = 0
idxDice = 0
while now < N-1:
    cnt += 1
    now += dice[idxDice]
    idxDice += 1
    if now >= N-1:
        break
    else:
        now += orders[now]

print(cnt)