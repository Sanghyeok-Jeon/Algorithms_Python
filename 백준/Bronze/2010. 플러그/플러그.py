import sys

N = int(sys.stdin.readline())
answer = 1
for _ in range(N):
    answer += int(sys.stdin.readline())

print(answer - N)