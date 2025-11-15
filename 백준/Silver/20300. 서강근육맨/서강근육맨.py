n = int(input())
loss = list(map(int, input().split()))
loss.sort()

result = 0

if n % 2 == 1:
    result = loss[-1]
    loss = loss[:-1]
    for i in range(len(loss) // 2):
        temp = loss[i] + loss[len(loss) - 1 - i]
        if result < temp:
            result = temp
else:
    for i in range(n // 2):
        temp = loss[i] + loss[n - 1 - i]
        if result < temp:
            result = temp

print(result)