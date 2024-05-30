A, B = map(int, input().split())
answer = 0

data = [0] * (B+1)
d = 1
i = 1
while i <= B:
    for j in range(i, i+d):
        if j <= B:
            data[j] = d
    d += 1
    i += d-1

for i in range(A, B+1):
    answer += data[i]

print(answer)