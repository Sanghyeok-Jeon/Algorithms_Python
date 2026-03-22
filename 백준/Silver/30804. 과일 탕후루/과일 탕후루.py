import sys

input = sys.stdin.readline

n = int(input())
fruits = list(map(int, input().split()))

count = [0] * 10
left = 0
kind = 0
answer = 0

for right in range(n):
    fruit = fruits[right]
    if count[fruit] == 0:
        kind += 1
    count[fruit] += 1

    while kind > 2:
        left_fruit = fruits[left]
        count[left_fruit] -= 1
        if count[left_fruit] == 0:
            kind -= 1
        left += 1

    answer = max(answer, right - left + 1)

print(answer)