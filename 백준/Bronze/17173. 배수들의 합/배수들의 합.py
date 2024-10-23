N, M = map(int, input().split())
K = list(map(int, input().split()))
sum_list = set()

for k in K:
    i = 1
    while k * i <= N:
        sum_list.add(k * i)
        i += 1

print(sum(sum_list))