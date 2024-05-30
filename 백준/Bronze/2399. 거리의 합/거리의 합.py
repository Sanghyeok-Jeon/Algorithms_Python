n = int(input())
x = list(map(int, input().split()))

answer = 0
for i in range(n):
    for j in range(n):
        answer += abs(x[i]-x[j])
        
print(answer)