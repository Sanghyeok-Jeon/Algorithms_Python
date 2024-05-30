N = int(input())
data = [list(input()) for _ in range(N)]
data2 = list(zip(*data))

checkPossible = True
for i in range(N):
    if data[i] != list(data2[i]):
        checkPossible = False
        break

print('YES' if checkPossible else 'NO')