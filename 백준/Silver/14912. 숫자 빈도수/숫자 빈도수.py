n, d = input().split()

data = ''
for i in range(1, int(n) + 1):
    data += str(i)

print(data.count(d))