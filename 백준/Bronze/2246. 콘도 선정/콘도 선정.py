N = int(input())
condos = [list(map(int, input().split())) for _ in range(N)]
condos.sort()

answer = 0
cost = 10001
for condo in condos:
    tmp_cost = condo[1]
    if tmp_cost < cost:
        cost = tmp_cost
        answer += 1

print(answer)