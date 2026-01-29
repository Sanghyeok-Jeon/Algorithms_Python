N = int(input())
X = list(map(int, input().split()))
T = list(map(int, input().split()))

answer = 2 * X[N - 1]
for i in range(N):
    answer = max(answer, X[i] + T[i])

print(answer)