n = int(input())

fibo = [0, 1]

mod = 1000000
period = mod // 10 * 15

for i in range(2, period):
    fibo.append(fibo[i-1] + fibo[i-2])
    fibo[i] %= mod

print(fibo[n%period])