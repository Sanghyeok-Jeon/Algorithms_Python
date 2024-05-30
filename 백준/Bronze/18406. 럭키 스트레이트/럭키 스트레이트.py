N = input()

left = 0
for n in N[:len(N)//2]:
    left += int(n)

right = 0
for n in N[len(N)//2:]:
    right += int(n)

if left == right:
    print('LUCKY')
else:
    print('READY')