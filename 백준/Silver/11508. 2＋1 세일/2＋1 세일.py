N = int(input())
C = sorted([int(input()) for _ in range(N)],reverse=True)

total = 0
for i in range(N):
    if i % 3 != 2:
        total += C[i]

print(total)