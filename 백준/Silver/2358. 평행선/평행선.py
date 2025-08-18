n = int(input())

x_count = {}
y_count = {}
for _ in range(n):
    x, y = map(int, input().split())
    x_count[x] = x_count.get(x, 0) + 1
    y_count[y] = y_count.get(y, 0) + 1

answer = 0
for cnt in x_count.values():
    if cnt >= 2:
        answer += 1
for cnt in y_count.values():
    if cnt >= 2:
        answer += 1

print(answer)