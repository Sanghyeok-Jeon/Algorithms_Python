N = int(input())
line = [int(input()) for _ in range(N)]
line.sort(reverse=True)

tip = 0
for i in range(N):
    tmp_tip = line[i] - i
    tip += tmp_tip if tmp_tip > 0 else 0

print(tip)
