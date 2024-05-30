N, C = map(int, input().split())

firework = [0] * (C+1)
answer = 0
for _ in range(N):
    period = int(input())
    for i in range(period, C+1, period):
        if not firework[i]:
            firework[i] = 1
            answer += 1
            
print(answer)