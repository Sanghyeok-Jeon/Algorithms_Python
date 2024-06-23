N = int(input())
vote = list(map(int, input().split()))

a, r, i = 0, 0, 0
for v in vote:
    if v == 1:
        a += 1
    elif v == -1:
        r += 1
    else:
        i += 1

if i >= a + r:
    print('INVALID')
else:
    if a > r:
        print('APPROVED')
    else:
        print('REJECTED')