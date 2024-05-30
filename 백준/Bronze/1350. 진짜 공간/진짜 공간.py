N = int(input())
fileSize = list(map(int, input().split()))
cluster = int(input())

needDisk = 0
for f in fileSize:
    needDisk += (f // cluster + 1) * cluster if f % cluster else (f // cluster) * cluster

print(needDisk)