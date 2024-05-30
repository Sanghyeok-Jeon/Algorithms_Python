N, X = map(int, input().split())
data = list(map(int, input().split()))

for i in range(N):
    if data[i] < X:
        print(data[i], end=' ')