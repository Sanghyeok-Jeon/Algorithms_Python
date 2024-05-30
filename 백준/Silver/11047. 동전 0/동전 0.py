import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
coins = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
coins.sort(reverse=True)

cntCoin = 0
for coin in coins:
    if coin <= K:
        cntCoin += K // coin
        K -= (K // coin) * coin
print(cntCoin)