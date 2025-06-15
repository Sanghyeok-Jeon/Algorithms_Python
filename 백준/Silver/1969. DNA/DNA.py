N, M = map(int, input().split())
dna = [input() for _ in range(N)]

result = ''
hamming_distance = 0

for i in range(M):
    cnt = {'A':0, 'C':0, 'G':0, 'T':0}

    for j in range(N):
        cnt[dna[j][i]] += 1

    max_cnt = max(cnt.values())

    candidates = [k for k, v in cnt.items() if v == max_cnt]
    candidates.sort()
    result += candidates[0]

    hamming_distance += N - cnt[candidates[0]]

print(result)
print(hamming_distance)