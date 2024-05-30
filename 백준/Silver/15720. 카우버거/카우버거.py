B, C, D = map(int, input().split())
burger = sorted(list(map(int, input().split())), reverse=True)
sidemenu = sorted(list(map(int, input().split())), reverse=True)
drink = sorted(list(map(int, input().split())), reverse=True)

totalPrice = sum(burger) + sum(sidemenu) + sum(drink)
totalDCPrice = 0

lenB = len(burger)
lenC = len(sidemenu)
lenD = len(drink)
idxB, idxC, idxD = 0, 0, 0
while True:
    b, c, d = 0, 0, 0
    if idxB < lenB:
        b = burger[idxB]
    if idxC < lenC:
        c = sidemenu[idxC]
    if idxD < lenD:
        d = drink[idxD]

    if b != 0 and c != 0 and d != 0:
        totalDCPrice += (b+c+d) * 0.9
    else:
        totalDCPrice += b + c + d

    idxB += 1
    idxC += 1
    idxD += 1

    if b == 0 and c == 0 and d == 0:
        break

print(totalPrice)
print(int(totalDCPrice))