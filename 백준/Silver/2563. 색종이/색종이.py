N = int(input())
paper = [[0]*101 for _ in range(101)]

for k in range(N):
    x, y = map(int, input().split())
    for i in range(y, y+10):
        for j in range(x, x+10):
            paper[i][j] = 1

answer = 0
for pp in paper:
    for p in pp:
        if p:
            answer += 1

print(answer)