N, B = input().split()

B = int(B)
newNum = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

answer = 0
for idx, var in enumerate(N[::-1]):
    answer += newNum.index(var) * (int(B) ** idx)

print(answer)