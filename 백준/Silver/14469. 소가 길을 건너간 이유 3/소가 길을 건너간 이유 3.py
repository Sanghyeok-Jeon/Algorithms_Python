N = int(input())
data = [tuple(map(int, input().split())) for _ in range(N)]

data.sort(key=lambda x:x[0])

total_time = 0
for i in range(N):
    if data[i][0] > total_time:
        total_time += data[i][0] - total_time
    total_time += data[i][1]

print(total_time)