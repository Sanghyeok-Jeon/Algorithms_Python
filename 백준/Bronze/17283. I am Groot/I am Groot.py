L = int(input())
R = int(input())

totalLength = 0
depth = 2
while True:
    tmp = L * R // 100
    if tmp <= 5:
        break

    totalLength += depth * tmp
    L = tmp
    depth *= 2

print(totalLength)