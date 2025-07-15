import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

even_start = 0
odd_move = 0
for x in A:
    if x % 2 != 0:
        odd_move += 1
    else:
        even_start += odd_move

odd_start = 0
even_move = 0
for x in A:
    if x % 2 == 0:
        even_move += 1
    else:
        odd_start += even_move

print(min(even_start, odd_start))