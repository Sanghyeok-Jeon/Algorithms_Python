T = int(input())
for tc in range(T):
    A, B = map(int, input().split())
    print('Case #{}: {} + {} = {}'.format(tc+1, A, B, A+B))