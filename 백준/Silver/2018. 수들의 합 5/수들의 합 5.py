import sys
input = sys.stdin.readline

N = int(input())

number = list(range(1, N + 1))
answer = 0
left = 0
right = 0
while right <= N:
    tmp_sum = sum(number[left:right + 1])
    if tmp_sum == N:
        answer += 1
        left += 1
        right += 1
    elif tmp_sum > N and left < right:
        left += 1
    else:
        right += 1

print(answer)