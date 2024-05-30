N = int(input())

minX = minY = 10001
maxX = maxY = -10001
for _ in range(N):
    x, y = map(int, input().split())

    minX = min(minX, x)
    minY = min(minY, y)
    maxX = max(maxX, x)
    maxY = max(maxY, y)

print((maxX - minX) * (maxY - minY))