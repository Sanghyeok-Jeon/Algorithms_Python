N = int(input())
answer = 0
for i in range(1, 501):
    for j in range(i, 501):
        if j**2 == i**2 + N:
            answer += 1
print(answer)