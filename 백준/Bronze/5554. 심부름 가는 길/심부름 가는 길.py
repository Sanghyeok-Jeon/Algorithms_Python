import sys

time = sum(map(int, sys.stdin))
print(time//60)
print(time%60)