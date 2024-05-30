N = int(input())
total = 0
x1, y1 = 0, 0
x0, y0 = x1, y1
for i in range(N):
    if i == 0:
        x1, y1 = map(int, input().split())
        x0, y0 = x1, y1
    else:
        x2, y2 = map(int, input().split())
        total += abs(x1-x2) + abs(y1-y2)
        x1, y1 = x2, y2
total += abs(x1-x0) + abs(y1-y0)
print(total)