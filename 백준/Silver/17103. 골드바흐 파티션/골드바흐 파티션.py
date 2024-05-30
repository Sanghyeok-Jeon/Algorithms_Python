maxNum = 1000000 + 1
prime = [1] * maxNum
for i in range(maxNum):
    if i < 2:
        prime[i] = 0
    else:
        if prime[i]:
            for j in range(i*i, maxNum, i):
                prime[j] = 0

T = int(input())
for _ in range(T):
    N = int(input())

    result = 0
    for i in range(2, N//2+1):
        if prime[i] and prime[N-i] and i <= N-i:
            result += 1

    print(result)