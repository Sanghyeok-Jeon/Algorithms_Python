import sys

N, M = map(int, sys.stdin.readline().split())
setN = set()
setM = set()

for _ in range(N):
    setN.add(sys.stdin.readline().rstrip())
for _ in range(M):
    setM.add(sys.stdin.readline().rstrip())

answer = sorted(list(setN & setM))
print(len(answer))
for ans in answer:
    print(ans)