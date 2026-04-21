import sys

input = sys.stdin.readline

n, m = map(int, input().split())
money = [int(input()) for _ in range(n)]


def can_withdraw(k):
    count = 1
    remain = k

    for cost in money:
        if remain < cost:
            count += 1
            remain = k
        remain -= cost

    return count <= m


left = max(money)
right = sum(money)
answer = right

while left <= right:
    mid = (left + right) // 2

    if can_withdraw(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)