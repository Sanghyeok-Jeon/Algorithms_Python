N = int(input())

fibo = [0, 1, 1]
for i in range(3, N + 1):
    fibo.append(fibo[i - 1] + fibo[i - 2])

print(fibo[N])