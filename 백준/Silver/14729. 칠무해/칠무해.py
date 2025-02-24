import sys
input = sys.stdin.readline

N = int(input())
score = [float(input()) for _ in range(N)]

score.sort()

for i in range(7):
    print('{:.3f}'.format(score[i]))