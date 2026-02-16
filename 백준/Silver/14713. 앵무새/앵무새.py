import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
parrots = []
for _ in range(N):
    parrots.append(deque(input().strip().split()))

target = input().strip().split()

for word in target:
    found = False
    for q in parrots:
        if q and q[0] == word:
            q.popleft()
            found = True
            break
    if not found:
        print("Impossible")
        sys.exit(0)

# target을 다 만들었는데도 남은 말이 있으면 안 됨
if any(q for q in parrots):
    print("Impossible")
else:
    print("Possible")