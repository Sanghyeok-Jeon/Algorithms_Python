def fib(n):
    global cntFib
    if n == 1 or n == 2:
        cntFib += 1
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibonacci(n):
    global cntFibonacci

    if n < 3:
        dpFibonacci[n] = 1
    else:
        for i in range(3, n+1):
            cntFibonacci += 1
            dpFibonacci[i] = dpFibonacci[i-1] + dpFibonacci[i-2]

    return dpFibonacci[n]


n = int(input())
dpFibonacci = [0] * (n+1)
cntFib, cntFibonacci = 0, 0
fib(n)
fibonacci(n)
print(cntFib, cntFibonacci)