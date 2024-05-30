a1, a2, a3 = map(int, input().split())
b1, b2, b3 = map(int, input().split())

type1, type2, type3 = 0, 0, 0

type3 += b1 - a1
type2 += type3 + 1
if b2 - a2 > 0:
    type1 += b1 - a1
elif b2 - a2 < 0:
    type1 += b1 - a1 - 1
else:
    if b3 - a3 >= 0:
        type1 += b1 - a1
    else:
        type1 += b1 - a1 - 1

print(type1, type2, type3, sep='\n')