T = int(input())
for _ in range(T):
    creditNumber = list(map(int, input()))
    for i in range(0, 16, 2):
        creditNumber[i] = creditNumber[i]*2 if creditNumber[i]*2 < 10 else (creditNumber[i]*2)%10 + 1

    if sum(creditNumber) % 10:
        print('F')
    else:
        print('T')