import sys

N = int(sys.stdin.readline())
cnt = 1
while N > 1:
    N -= cnt * 6
    cnt += 1
print(cnt)
