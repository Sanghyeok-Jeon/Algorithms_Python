import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    num = input().rstrip()

    cnt = 0
    while num != '6174':
        cnt += 1

        num_tmp_max = int(''.join(sorted(num, reverse=True)))
        num_tmp_min = int(''.join(sorted(num)))

        num = str(num_tmp_max - num_tmp_min)

        if len(num) < 4:
            for _ in range(4 - len(num)):
                num += '0'

    print(cnt)