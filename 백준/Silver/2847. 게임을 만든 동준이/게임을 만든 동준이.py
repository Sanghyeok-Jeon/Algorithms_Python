N = int(input())
difficult = [int(input()) for _ in range(N)][::-1]

cnt = 0
for i in range(1, N):
    if difficult[i] > difficult[i - 1] - 1:
        diff = difficult[i] - (difficult[i - 1] - 1)

        cnt  += diff
        difficult[i] -= diff

print(cnt)