A, B = input().split()
sumA, sumB = 0, 0

for a in A:
    sumA += int(a)
for b in B:
    sumB += int(b)

print(sumA * sumB)