N, K, A = map(int, input().split())

minTime = 2e9
for _ in range(N):
    t, s = map(int, input().split())
    tmpTime = ((K//A)//t)*(t+s) - s if not (K//A)%t else ((K//A)//t)*(t+s) + ((K//A)%t)
    minTime = min(minTime, tmpTime)

print(minTime)