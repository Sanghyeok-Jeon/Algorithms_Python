targetN = int(input())
n = targetN

if n < 10:
    tmpStrN = str(n) + str(n)
    n = int(tmpStrN)
else:
    n1, n2 = str(n)[0], str(n)[1]
    tmpStrN = str(n)[1] + (str(int(n1)+int(n2))[1] if int(n1)+int(n2) > 9 else str(int(n1)+int(n2)))
    n = int(tmpStrN)
cnt = 1

while True:
    if n == targetN:
        break

    if n < 10:
        tmpStrN = str(n) + str(n)
        n = int(tmpStrN)
    else:
        n1, n2 = str(n)[0], str(n)[1]
        tmpStrN = str(n)[1] + (str(int(n1)+int(n2))[1] if int(n1)+int(n2) > 9 else str(int(n1)+int(n2)))
        n = int(tmpStrN)

    cnt += 1

print(cnt)