n = int(input())

dp = [0] * (abs(n)+1)

for i in range(abs(n)+1):
    if i == 0:
        dp[i] = 0
    elif i == 1:
        dp[i] = 1
    else:
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000000

if n < 0:
    if n % 2 == 0:
        print(-1)
    else:
        print(1)
elif n == 0:
    print(0)
else:
    print(1)
print(dp[abs(n)])