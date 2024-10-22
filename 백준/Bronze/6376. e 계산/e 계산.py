print('n', 'e')
print('- -----------')
print(0, 1)

factorial = 1
sum_factorial = 1
for n in range(1, 10):
    factorial *= n
    sum_factorial += 1 / factorial
    if n == 1:
        print(n, int(sum_factorial))
    elif n == 2:
        print(n, round(sum_factorial, 9))
    else:
        print(n, "{:.9f}".format(sum_factorial, 9))