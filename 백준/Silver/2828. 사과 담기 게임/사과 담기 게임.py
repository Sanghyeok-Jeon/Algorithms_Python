N, M = map(int, input().split())
J = int(input())
apple = [int(input()) for _ in range(J)]

basket = M - 1
left = 1
right = left + basket

answer = 0
for ap in apple:
    if ap < left:
       answer +=  left - ap
       left, right = ap, ap + basket
    elif ap > right:
        answer += ap - right
        left, right = ap - basket, ap

print(answer)