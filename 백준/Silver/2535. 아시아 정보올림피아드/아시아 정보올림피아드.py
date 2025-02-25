import sys
input = sys.stdin.readline

N = int(input())
score = [list(map(int, input().split())) for _ in range(N)]

score.sort(key=lambda x: -x[2])

win_nation = []
cnt_win = 0
for i in range(N):
    nation, studentNo = score[i][0], score[i][1]

    if win_nation.count(nation) == 2:
        continue

    win_nation.append(nation)
    print(nation, studentNo)
    cnt_win += 1

    if cnt_win == 3:
        break