jinho_MBTI = input()
N = int(input())
others_MBTI = [input() for _ in range(N)]

cnt = 0
for n in range(N):
    if jinho_MBTI == others_MBTI[n]:
        cnt += 1

print(cnt)