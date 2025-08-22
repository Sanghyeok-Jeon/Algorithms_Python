import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    origin = input()
    target = input()

    b_cnt = 0
    w_cnt = 0
    for i in range(N):
        if origin[i] != target[i]:
            if origin[i] == 'B':
                b_cnt += 1
            else:
                w_cnt += 1

    print(max(b_cnt, w_cnt))