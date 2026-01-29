import sys

INF = 10**30

input = sys.stdin.readline
N = int(input().strip())
X = [0] + list(map(int, input().split()))
T = [0] + list(map(int, input().split()))

dpL = [INF] * (N + 2)
dpR = [INF] * (N + 2)
for i in range(1, N + 1):
    v = max(T[i], X[i])
    dpL[i] = v
    dpR[i] = v

for length in range(2, N + 1):
    newL = [INF] * (N + 2)
    newR = [INF] * (N + 2)
    for l in range(1, N - length + 2):
        r = l + length - 1

        t1 = dpL[l + 1] + (X[l + 1]- X[l])
        t1 = max(t1, T[l])
        t2 = dpR[l + 1] + (X[r]- X[l])
        t2 = max(t2, T[l])
        newL[l]= min(t1, t2)

        t3 = dpL[l] + (X[r]- X[l])
        t3 = max(t3, T[r])
        t4 = dpR[l] + (X[r]- X[r - 1])
        t4 = max(t4, T[r])
        newR[l]= min(t3, t4)

    dpL, dpR = newL, newR

ans = min(dpL[1] + X[1], dpR[1] + X[N])
print(ans)