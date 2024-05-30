N = int(input())
find = 0
for n in range(N-len(str(N))*9, N):
    ans = tmp = n
    while tmp > 0:
        ans += tmp % 10
        tmp //= 10
    if ans == N:
        print(n)
        find = 1
        break

if find == 0:
    print('0')