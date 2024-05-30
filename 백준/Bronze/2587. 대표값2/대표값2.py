import sys
data = sorted(list(map(int, sys.stdin.readlines())))
print(sum(data)//5)
print(data[2])