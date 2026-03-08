import sys
input = sys.stdin.readline

S, K = map(int, input().split())

q, r = divmod(S, K)

ans = pow(q, K - r) * pow(q + 1, r)

print(ans)