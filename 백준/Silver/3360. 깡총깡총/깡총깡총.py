n = int(input())

cnt = 0
for i in range(n // 3 + 1):
    cnt += (n - 3*i) // 2 + 1

print(cnt % 1000000)