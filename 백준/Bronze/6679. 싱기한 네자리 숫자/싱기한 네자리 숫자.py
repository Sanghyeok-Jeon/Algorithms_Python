def cal(a, b):
    sum = 0
    while a > 0:
        sum += a % b
        a //= b
    return sum

for i in range(1000, 10000):
    jinsu10 = cal(i, 10)
    jinsu12 = cal(i, 12)
    jinsu16 = cal(i, 16)

    if jinsu16 == jinsu12 and jinsu10 == jinsu16:
        print(i)