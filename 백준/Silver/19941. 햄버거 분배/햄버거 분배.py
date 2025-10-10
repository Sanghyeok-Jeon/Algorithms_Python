n, k = map(int, input().split())
s = list(input())

cnt = 0
for i in range(n):
    if s[i] == 'P':
        # 사람 위치에서 양쪽 K범위 탐색
        for j in range(max(i-k, 0), min(i+k+1, n)):
            if s[j] == 'H':
                s[j] = 'X'
                cnt += 1
                break

print(cnt)