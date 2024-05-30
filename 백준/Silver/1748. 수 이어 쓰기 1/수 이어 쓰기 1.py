N = int(input())

lenNum = 0
i = 10
j = 1
while True:
    if N < i:
        break

    lenNum += 9 * i//10 * j

    i *= 10
    j += 1

lenNum += (N - i//10 + 1) * len(str(N))

print(lenNum)