import sys

input = sys.stdin.readline
out = []

while True:
    line = input().strip()
    if not line:
        break
    n = int(line)
    if n == 0:
        break

    best = None
    cur = None
    for _ in range(n):
        x = int(input())
        if cur is None:
            cur = best = x
        else:
            cur = max(x, cur + x)
            best = max(best, cur)

    out.append(str(best))

sys.stdout.write("\n".join(out))