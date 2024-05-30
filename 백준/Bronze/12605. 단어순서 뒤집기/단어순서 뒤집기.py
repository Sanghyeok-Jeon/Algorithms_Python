N = int(input())
for tc in range(N):
    data = list(input().split())
    print('Case #{}: {}'.format(tc+1, ' '.join(data[::-1])))