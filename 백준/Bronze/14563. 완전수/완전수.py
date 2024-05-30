T = int(input())
N = list(map(int, input().split()))
for n in N:
    is_perfect = 0
    for i in range(1, int(n**0.5)+1):
        if not n % i:
            is_perfect += i + n//i if i != n//i else i

    if is_perfect - n == n:
        print('Perfect')
    elif is_perfect - n < n:
        print('Deficient')
    else:
        print('Abundant')