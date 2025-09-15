N, L = map(int, input().split())
leaked = sorted(list(map(int, input().split())))
taped = [False] * 1001

cnt = 0
for i in range(N):
    if not taped[leaked[i]]:
        for j in range(leaked[i], leaked[i] + L):
            if j <= 1000:
                taped[j] = True

        cnt += 1

print(cnt)