N = int(input())

for _ in range(2 * N):
    print('@' * N + ' ' * 3 * N + '@' * N)
for _ in range(N):
    print('@' * N * 5)
for _ in range(N):
    print('@' * N + ' ' * 3 * N + '@' * N)
for _ in range(N):
    print('@' * N * 5)