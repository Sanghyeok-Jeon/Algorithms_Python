X = input()

cnt = 0
Y = X
while True:
    if len(Y) == 1:
        break

    cnt += 1
    Y = str(sum([int(n) for n in Y]))

print(cnt)
if Y in ('3', '6', '9'):
    print('YES')
else:
    print('NO')