import sys
input = sys.stdin.readline

N, K, Q, M = map(int, input().split())

sleep = [False] * (N + 3)   # 졸고 있는 학생
check = [False] * (N + 3)   # 출석 처리된 학생

if K > 0:
    for num in map(int, input().split()):
        sleep[num] = True
else:
    _ = input().strip()

attenders = list(map(int, input().split()))

for s in attenders:
    if sleep[s]:
        continue
    for j in range(s, N + 3, s):
        if not sleep[j]:
            check[j] = True

prefix = [0] * (N + 3)
for i in range(3, N + 3):
    prefix[i] = prefix[i - 1] + (0 if check[i] else 1)

out_lines = []
for _ in range(M):
    S, E = map(int, input().split())
    out_lines.append(str(prefix[E] - prefix[S - 1]))

print("\n".join(out_lines))