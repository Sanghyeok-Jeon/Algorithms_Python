N = int(input())
sumNormal = 0
sumCubic = 0
for i in range(1, N+1):
    sumNormal += i
    sumCubic += i ** 3

print(sumNormal)
print(sumNormal ** 2)
print(sumCubic)