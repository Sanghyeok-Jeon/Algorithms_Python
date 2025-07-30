N = int(input())
M, K = map(int, input().split())
pens = list(map(int, input().split()))

pens.sort(reverse=True)

total_need = M * K
answer = 0
for pen in pens:
    if total_need <= 0:
        break
    else:
        total_need -= pen
        answer += 1

if total_need > 0:
    print('STRESS')
else:
    print(answer)