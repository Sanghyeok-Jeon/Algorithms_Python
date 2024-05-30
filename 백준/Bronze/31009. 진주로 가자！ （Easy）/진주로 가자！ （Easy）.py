N = int(input())
data = []
fare_jinju = 0
for _ in range(N):
    dest, str_fare = input().split()
    fare = int(str_fare)
    data.append([dest, fare])
    if dest == 'jinju':
        fare_jinju = fare

over_jinju = 0
for i in range(N):
    if data[i][0] != 'jinju':
        if data[i][1] > fare_jinju:
            over_jinju += 1

print(fare_jinju)
print(over_jinju)