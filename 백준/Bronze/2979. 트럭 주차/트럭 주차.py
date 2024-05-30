A, B, C = map(int, input().split())

parking = [0] * 101
for _ in range(3):
    i, o = map(int, input().split())
    for t in range(i, o):
        parking[t] += 1

totalFee = 0
for p in parking:
    if p:
        if p == 1:
            totalFee += A
        elif p == 2:
            totalFee += B * 2
        else:
            totalFee += C * 3

print(totalFee)