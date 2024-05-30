n = int(input())
N = n % 8

if N == 1:
    print(1)
elif N == 2 or N == 0:
    print(2)
elif N == 3 or N == 7:
    print(3)
elif N == 4 or N == 6:
    print(4)
else:
    print(5)