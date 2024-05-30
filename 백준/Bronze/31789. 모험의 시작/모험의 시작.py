N = int(input())
X, S = map(int, input().split())

result = 'NO'
for _ in range(N):
    c, p = map(int, input().split())
    if c <= X and p > S:
        result = 'YES'

print(result)