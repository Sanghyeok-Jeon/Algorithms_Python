P, K = map(int, input().split())

prime_num = [False, False] + [True] * (K - 2)
for i in range(2, int(K ** 0.5) + 1):
    if prime_num[i]:
        for j in range(i + i, K, i):
            if prime_num[j]:
                prime_num[j] = False

answer = 'GOOD'
for i in range(2, K):
    if prime_num[i]:
        if not P % i:
            answer = 'BAD' + ' ' + str(i)
            break

print(answer)