k = int(input())
a, b, c, d = map(int, input().split())

ax_b = a * k + b
cx_d = c * k + d
if ax_b == cx_d:
    print('Yes {}'.format(ax_b))
else:
    print('No')