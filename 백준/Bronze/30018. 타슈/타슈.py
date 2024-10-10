N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer = 0
for i in range(N):
    if b[i] > a[i]:
        answer += b[i] - a[i]

print(answer)