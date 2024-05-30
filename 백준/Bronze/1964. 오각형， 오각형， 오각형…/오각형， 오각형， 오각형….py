N = int(input())

sumDot = 0
for i in range(1, N+1):
    if i == 1:
        sumDot += 5
    else:
        sumDot += i*3 + 1

print(sumDot % 45678)