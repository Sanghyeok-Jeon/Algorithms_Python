import sys
input = sys.stdin.readline

N = int(input())
numbers = sorted(list(map(int, input().split())))
print(numbers[(N - 1) // 2])