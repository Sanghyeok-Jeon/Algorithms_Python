T = int(input())
for _ in range(T):
    n = int(input())
    answer = sum([k * ((k + 2) * (k + 1) // 2) for k in range(1, n + 1)])
    print(answer)