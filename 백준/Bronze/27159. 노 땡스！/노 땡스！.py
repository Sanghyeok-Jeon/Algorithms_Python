N = int(input())
x = list(map(int, input().split()))
answer = x[0]

for i in range(1, N):
    if x[i] - x[i-1] != 1:
        answer += x[i]

print(answer)