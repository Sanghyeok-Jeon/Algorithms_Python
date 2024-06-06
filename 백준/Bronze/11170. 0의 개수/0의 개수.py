T = int(input())
for _ in range(T):
    N, M = input().split()

    cnt_zero = 0
    for i in range(int(N), int(M) + 1):
        for n in str(i):
            if n == '0':
                cnt_zero += 1

    print(cnt_zero)