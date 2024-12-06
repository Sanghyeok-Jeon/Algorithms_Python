N, K = map(int, input().split())

cnt = 0
for a in range(0, N + 1):
    for b in range(0, 60):
        for c in range(0, 60):
            tmp_a = str(a) if a > 9 else '0' + str(a)
            tmp_b = str(b) if b > 9 else '0' + str(b)
            tmp_c = str(c) if c > 9 else '0' + str(c)

            tmp = tmp_a + tmp_b + tmp_c
            if str(K) in str(tmp):
                cnt += 1

print(cnt)