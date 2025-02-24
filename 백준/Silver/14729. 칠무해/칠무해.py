import sys
input = sys.stdin.readline

N = int(input())
score = sorted([float(input()) for _ in range(N)])

for i in range(7):
    print('{:.3f}'.format(score[i]))