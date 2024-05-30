A, B = input().split()
a = list(A)
b = list(B)

maxSum, minSum = 0, 0

for i in range(len(a)):
    if a[i] == '6':
        a[i] = '5'
minSum += int(''.join(a))
for i in range(len(a)):
    if a[i] == '5':
        a[i] = '6'
maxSum += int(''.join(a))

for i in range(len(b)):
    if b[i] == '6':
        b[i] = '5'
minSum += int(''.join(b))
for i in range(len(b)):
    if b[i] == '5':
        b[i] = '6'
maxSum += int(''.join(b))

print('{} {}'.format(minSum, maxSum))