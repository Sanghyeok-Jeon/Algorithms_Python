M, N = map(int, input().split())
num_origin = list(range(M, N + 1))

num_to_alpha = []
alpha = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
for n in num_origin:
    origin_n = n
    new_n = ''
    while True:
        if n < 10:
            new_n += alpha[n]
            break

        new_n += alpha[n // 10]
        new_n += ' '
        n %= 10

    num_to_alpha.append((origin_n, new_n))

num_to_alpha.sort(key=lambda x:x[1])

for i in range(len(num_to_alpha)):
    if i != 0 and not i % 10:
        print()
    print(num_to_alpha[i][0], end=' ')

