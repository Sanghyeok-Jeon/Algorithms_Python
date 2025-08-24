n = int(input())
w = sorted(list(map(int, input().split())))

min_sum = w[-1] * w[-1] + 1
for i in range(0, n):
    tmp_sum = w[i] + w[-(i + 1)]
    min_sum = min(min_sum, tmp_sum)

print(min_sum)