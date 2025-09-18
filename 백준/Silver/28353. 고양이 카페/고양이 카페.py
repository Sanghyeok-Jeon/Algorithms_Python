N, K = map(int, input().split())
weights = sorted(list(map(int, input().split())))

result = 0
left = 0
right = N - 1
while True:
    if left >= right:
        break

    weight_left = weights[left]
    weight_right = weights[right]
    if weight_left + weight_right <= K:
        result += 1
        left = left + 1
        right = right - 1
    else:
        right = right - 1

print(result)