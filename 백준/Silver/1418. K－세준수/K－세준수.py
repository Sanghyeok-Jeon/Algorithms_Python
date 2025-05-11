N = int(input())
K = int(input())

cnt = 0
for n in range(2, N + 1):
    i = 2
    flag_k_num = True
    while i <= n:
        if i > K:
            flag_k_num = False
            break

        if n % i == 0:
            n //= i
        else:
            i += 1

    if flag_k_num:
        cnt += 1

print(cnt + 1)