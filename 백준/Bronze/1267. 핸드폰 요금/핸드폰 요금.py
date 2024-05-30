N = int(input())
time = list(map(int, input().split()))
y, m = 0, 0
for i in range(N):
    y += (time[i]//30 + 1) * 10
    m += (time[i]//60 + 1) * 15

if y < m:
    print('Y {}'.format(y))
elif m < y:
    print('M {}'.format(m))
else:
    print('Y M {}'.format(y))