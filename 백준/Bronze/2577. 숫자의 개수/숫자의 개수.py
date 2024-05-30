A, B, C = int(input()), int(input()), int(input())
data = str(A * B * C)
num = [0] * 10
for i in range(len(data)):
    num[int(data[i])] += 1

for i in range(10):
    print(num[i])