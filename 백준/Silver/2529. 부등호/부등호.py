import sys

input = sys.stdin.readline

k = int(input())
signs = input().split()

visited = [False] * 10
answer = []


def valid(a, b, op):
    if op == '<':
        return a < b
    return a > b


def dfs(depth, nums):
    if depth == k + 1:
        answer.append(''.join(map(str, nums)))
        return

    for i in range(10):
        if not visited[i]:
            if depth == 0 or valid(nums[-1], i, signs[depth - 1]):
                visited[i] = True
                nums.append(i)
                dfs(depth + 1, nums)
                nums.pop()
                visited[i] = False


dfs(0, [])

print(answer[-1])
print(answer[0])