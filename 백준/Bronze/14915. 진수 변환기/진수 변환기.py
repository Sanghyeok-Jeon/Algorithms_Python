m, n = map(int, input().split())
formation = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

data = []
while m >= n:
    tmp = m % n

    data.append(formation[tmp])

    m //= n

data.append(formation[m])

print(''.join(data[::-1]))