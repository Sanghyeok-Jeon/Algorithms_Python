N = int(input())
A = list(map(int, input().split()))

answer = 'YES'
preHeight = 0
updown = False
for i in range(N):
    if preHeight < A[i] and not updown:
        preHeight = A[i]
        continue
    elif preHeight > A[i] and updown:
        preHeight = A[i]
        continue
    elif preHeight > A[i] and not updown:
        preHeight = A[i]
        updown = True
        continue
    else:
        answer = 'NO'
        break

print(answer)