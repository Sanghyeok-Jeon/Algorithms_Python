message = input()

N = len(message)
R = 0
C = 0
for c in range(int(N ** 0.5), -1, -1):
    if N % c == 0:
        C = c
        R = N // C
        break

for c in range(C):
    for r in range(R):
        print(message[r * C + c], end='')