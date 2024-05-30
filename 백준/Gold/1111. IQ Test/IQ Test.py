N = int(input())
numbers = list(map(int, input().split()))

if N == 1:
    print('A')
elif N == 2:
    if numbers[0] == numbers[1]:
        print(numbers[0])
    else:
        print('A')
else:
    a = (numbers[1] - numbers[2]) // (numbers[0] - numbers[1]) if (numbers[0] - numbers[1]) else 0
    b = numbers[1] - numbers[0] * a

    for i in range(N - 1):
        if numbers[i + 1] != numbers[i] * a + b:
            print('B')
            exit()

    print(numbers[-1] * a + b)