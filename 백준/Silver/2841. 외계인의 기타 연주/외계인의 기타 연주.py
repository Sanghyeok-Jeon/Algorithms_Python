import sys

input = sys.stdin.readline

N, P = map(int, input().split())
stacks = [[] for _ in range(7)]
answer = 0

for _ in range(N):
    line, fret = map(int, input().split())

    while stacks[line] and stacks[line][-1] > fret:
        stacks[line].pop()
        answer += 1

    if stacks[line] and stacks[line][-1] == fret:
        continue

    stacks[line].append(fret)
    answer += 1

print(answer)