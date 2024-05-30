T = int(input())

for tc in range(T):
    N = int(input())
    sumNum = N
    sumNum += int(str(N)[::-1])

    if str(sumNum) == str(sumNum)[::-1]:
        print('YES')
    else:
        print('NO')