import sys
N = int(sys.stdin.readline())
member = []
idx = 0
for m in sys.stdin:
    member.append((m.split(), idx))
    idx += 1

member.sort(key=lambda x : (int(x[0][0]), x[1]))

for m in member:
    print(m[0][0], m[0][1])