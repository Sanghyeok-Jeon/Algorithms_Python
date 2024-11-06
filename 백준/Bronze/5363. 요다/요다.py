N = int(input())
for _ in range(N):
    S = list(input().split())
    print(' '.join(S[2:] + S[:2]))