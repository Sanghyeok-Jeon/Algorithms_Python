N = int(input())
numList = list(input())

ans = 0
for i in range(N):
    ans += int(numList[i])

print(ans)