N = int(input())
checkpoints = [tuple(map(int, input().split())) for _ in range(N)]

total = 0
for i in range(N - 1):
    total += abs(checkpoints[i + 1][0] - checkpoints[i][0]) + abs(checkpoints[i + 1][1] - checkpoints[i][1])

max_reduce = 0
for i in range(1, N - 1):
    skip = abs(checkpoints[i + 1][0] - checkpoints[i - 1][0]) + abs(checkpoints[i + 1][1] - checkpoints[i - 1][1])
    normal = (abs(checkpoints[i + 1][0] - checkpoints[i][0]) + abs(checkpoints[i + 1][1] - checkpoints[i][1])
              + abs(checkpoints[i - 1][0] - checkpoints[i][0]) + abs(checkpoints[i - 1][1] - checkpoints[i][1]))

    max_reduce = max(max_reduce, normal - skip)

print(total - max_reduce)