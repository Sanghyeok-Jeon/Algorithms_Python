N, L = input().split()
N = int(N)
cnt = 0
n = 0
while cnt < N:
    n += 1
    if L not in str(n):
        cnt += 1

print(n)