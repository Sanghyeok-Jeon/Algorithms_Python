a, b = map(int, input().split())

pre_sum = 0
for i in range(1, a):
    pre_sum += i

answer = 1
for j in range(a, b + 1):
    pre_sum += j
    answer *= pre_sum

print(answer % 14579)