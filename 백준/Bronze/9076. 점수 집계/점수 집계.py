T = int(input())
for _ in range(T):
    score = sorted(list(map(int, input().split())))
    if score[3] - score[1] >= 4:
        print('KIN')
    else:
        print(sum(score[1:4]))