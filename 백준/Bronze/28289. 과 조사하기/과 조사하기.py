P = int(input())

class12, class3, class4 = 0, 0, 0
newbi = 0
for _ in range(P):
    g, c, n = map(int, input().split())
    if g == 1:
        newbi += 1
    else:
        if c == 1 or c == 2:
            class12 += 1
        elif c == 3:
            class3 += 1
        elif c == 4:
            class4 += 1

print(class12)
print(class3)
print(class4)
print(newbi)