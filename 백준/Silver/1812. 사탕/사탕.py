N = int(input())
data = [int(input()) for _ in range(N)]

candy = []

candy_1 = 0
for i in range(N):
    if not i % 2:
        candy_1 += data[i]
    else:
        candy_1 -= data[i]

candy_1 //= 2
candy.append(candy_1)

for i in range(N - 1):
    candy_next = data[i] - candy[-1]
    candy.append(candy_next)

for i in range(len(candy)):
    print(candy[i])