a, b = input().split()
A = a[::-1]
B = b[::-1]

numList_A = [0] * 7
numList_B = [0] * 7

for i in range(len(A)):
    numList_A[i] = int(A[i])

for i in range(len(B)):
    numList_B[i] = int(B[i])

tmp = []
for i in range(max(len(A), len(B))):
    tmp.append(str(numList_A[i] + numList_B[i]))

print(''.join(tmp[::-1]))