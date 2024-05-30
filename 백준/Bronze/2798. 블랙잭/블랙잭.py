N, M = map(int, input().split())
num = list(map(int, input().split()))

near500 = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum = num[i] + num[j] + num[k]
            if sum <= M:
                near500 = max(near500, sum)

print(near500)