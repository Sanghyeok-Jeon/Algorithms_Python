H, W = map(int, input().split())
block = list(map(int, input().split()))

rain = 0
for i in range(1, W-1):
    left_wall = max(block[:i])
    right_wall = max(block[i+1:])
    max_rainfall = min(left_wall, right_wall)

    if block[i] < max_rainfall:
        rain += max_rainfall - block[i]

print(rain)