n = int(input())
L = sorted(list(map(int, input().split())), reverse=True)

answer = 0
for i in range(1, n):
    answer += L[0] + L[i]

print(answer)