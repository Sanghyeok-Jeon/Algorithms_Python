a, d, k = map(int, input().split())
result = k - a
if result%d or result//d < 0:
    print('X')
else:
    print(result//d + 1)