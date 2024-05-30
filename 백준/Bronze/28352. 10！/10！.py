N = int(input())
factorial_N = 1
for i in range(1, N+1):
    factorial_N *= i

print(factorial_N // 7 // 24 // 60 // 60)