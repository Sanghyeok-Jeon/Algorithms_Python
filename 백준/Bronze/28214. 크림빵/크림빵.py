N, K, P = map(int, input().split())
breads = list(map(int, input().split()))

cnt = 0
for i in range(0, len(breads), K):
    if breads[i:i + K].count(0) < P:
        cnt += 1

print(cnt)