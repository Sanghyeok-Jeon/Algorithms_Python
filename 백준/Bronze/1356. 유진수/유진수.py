N = input()
l = len(N)

answer = 'NO'
for i in range(l-1):
    left = right = 1

    for j in range(i+1):
        left *= int(N[j])

    for k in range(i+1, l):
        right *= int(N[k])

    if left == right:
        answer = 'YES'
        break

print(answer)