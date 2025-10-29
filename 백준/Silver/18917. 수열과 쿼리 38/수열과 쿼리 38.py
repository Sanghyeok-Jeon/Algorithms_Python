import sys
input = sys.stdin.readline

n = int(input())
sum_ = 0
xor_ = 0

for _ in range(n):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        sum_ += cmd[1]
        xor_ ^= cmd[1]
    elif cmd[0] == 2:
        sum_ -= cmd[1]
        xor_ ^= cmd[1]
    elif cmd[0] == 3:
        print(sum_)
    elif cmd[0] == 4:
        print(xor_)