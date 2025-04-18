data = []
n = 0
first_data = list(input().split())
for i in range(len(first_data)):
    if i == 0:
        n = int(first_data[i])
    else:
        data.append(int(first_data[i][::-1]))

while True:
    if len(data) == n:
        break

    tmp_data = list(input().split())

    for td in tmp_data:
        data.append(int(td[::-1]))

data.sort()

for i in range(n):
    print(data[i])