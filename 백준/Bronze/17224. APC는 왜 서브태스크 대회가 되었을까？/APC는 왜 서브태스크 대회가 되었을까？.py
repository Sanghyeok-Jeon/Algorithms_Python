N, L, K = map(int, input().split())
problems = [list(map(int, input().split())) for _ in range(N)]

problems.sort(key=lambda x:(x[1], x[0]))
score = 0
solved = 0
for i in range(N):
    if solved == K:
        break
        
    sub1, sub2 = problems[i]

    if sub1 <= L:
        score += 100
        if sub2 <= L:
            score += 40

        solved += 1

print(score)