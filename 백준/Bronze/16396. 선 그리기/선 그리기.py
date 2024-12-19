N = int(input())
projection = [0] * 10001
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, y):
        projection[i] = 1

print(projection.count(1))