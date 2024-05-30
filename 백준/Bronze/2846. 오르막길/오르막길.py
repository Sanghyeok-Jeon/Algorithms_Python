N = int(input())
load = list(map(int, input().split()))

maxUphill = 0
tmpUphill = 0
for i in range(1, N):
    if load[i] > load[i-1]:
        tmpUphill += load[i] - load[i-1]
    else:
        tmpUphill = 0
    maxUphill = max(maxUphill, tmpUphill)

print(maxUphill)