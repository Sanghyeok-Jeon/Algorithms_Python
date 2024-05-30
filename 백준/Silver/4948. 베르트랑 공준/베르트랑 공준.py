maxNum = 123456 * 2 + 1

prime = [1] * maxNum
for i in range(maxNum):
    if i < 2:
        prime[i] = 0
    else:
        if prime[i]:
            for j in range(i*i, maxNum, i):
                prime[j] = 0

while True:
    n = int(input())

    if not n:
        break

    print(sum(prime[n+1:2*n+1]))