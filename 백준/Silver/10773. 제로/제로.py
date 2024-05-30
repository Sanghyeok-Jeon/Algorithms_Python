import sys
K = int(sys.stdin.readline())

jangbu = []
for n in map(int, sys.stdin):
    if not n:
        jangbu.pop()
    else:
        jangbu.append(n)

print(sum(jangbu))