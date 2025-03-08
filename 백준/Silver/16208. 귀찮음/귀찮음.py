n = int(input())
list_a = sorted(list(map(int, input().split())))

sum_tmp = sum(list_a)
answer = 0
for i in range(n):
    sum_tmp -= list_a[i]
    answer += list_a[i] * sum_tmp

print(answer)