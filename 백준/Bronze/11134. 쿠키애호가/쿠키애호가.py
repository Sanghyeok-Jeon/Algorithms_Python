T = int(input())
for _ in range(T):
    N, C = map(int, input().split())
    print(N // C + 1 if N % C else N // C)