N = int(input())
ST = input()

cnt = 0
for i in range(N//2):
    if ST[i] != ST[N - 1 - i]:
        cnt += 1

print(cnt)