N = int(input())
heights = list(map(int, input().split()))

answer = 0
height_max = 0
cnt = 0
for i in range(N):
    if height_max < heights[i]:
        height_max = heights[i]
        cnt = 0
    else:
        cnt += 1

    answer = max(cnt, answer)

print(answer)