N = int(input())
data = []
for _ in range(N):
    x, y = map(int, input().split())
    data.append((x, y))

ans = sorted(data, key=lambda x : (x[0], x[1]))
for i in range(N):
    print('{} {}'.format(ans[i][0], ans[i][1]))