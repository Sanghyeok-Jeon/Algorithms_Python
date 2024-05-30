import sys
import collections

N = int(sys.stdin.readline())
data = sorted([int(sys.stdin.readline()) for _ in range(N)])

print(round(sum(data)/N))
print(data[N//2])

cntData = collections.Counter(data).most_common()
if len(cntData) > 1:
    if cntData[0][1] == cntData[1][1]:
        print(cntData[1][0])
    else:
        print(cntData[0][0])
else:
    print(cntData[0][0])

print(data[-1] - data[0])