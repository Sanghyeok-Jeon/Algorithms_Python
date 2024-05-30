N = int(input())
numbers = list(map(int, input().split()))

sosu = [-1, -1] + [0]*999

for i in range(2, 1001):
    if sosu[i] == 0:
        sosu[i] = 1
        for j in range(i*2, 1001, i):
            sosu[j] = -1

result = 0
for n in numbers:
    if sosu[n] == 1:
        result += 1

print(result)