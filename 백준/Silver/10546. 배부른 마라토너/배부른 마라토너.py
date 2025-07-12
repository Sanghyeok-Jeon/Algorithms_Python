import sys
input = sys.stdin.readline

N = int(input())
runner = {}

for _ in range(N):
    name = input()
    if name in runner:
        runner[name] += 1
    else:
        runner[name] = 1

for _ in range(N - 1):
    name = input()
    runner[name] -= 1

for i, v in runner.items():
    if v != 0:
        print(i)