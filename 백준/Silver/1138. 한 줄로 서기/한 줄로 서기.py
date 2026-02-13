import sys

input = sys.stdin.readline
n = int(input().strip())
a = list(map(int, input().split()))

line = [0] * n 

for person in range(1, n + 1):
    need = a[person - 1]
    for i in range(n):
        if line[i] == 0:
            if need == 0:
                line[i] = person
                break
            need -= 1

print(*line)
