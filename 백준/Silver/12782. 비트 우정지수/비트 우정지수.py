T = int(input())
for _ in range(T):
    N, M = input().split()

    cnt_1_to_0 = 0
    cnt_0_to_1 = 0

    for bit_n, bit_m in zip(N, M):
        if bit_n == '1' and bit_m == '0':
            cnt_1_to_0 += 1
        elif bit_n == '0' and bit_m == '1':
            cnt_0_to_1 += 1

    print(max(cnt_1_to_0, cnt_0_to_1))