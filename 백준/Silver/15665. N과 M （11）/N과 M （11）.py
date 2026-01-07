import sys
input = sys.stdin.readline

def dfs(sequence, depth):
    if depth == m:
        print(*sequence)
        return

    for num in numbers:
        dfs(sequence + [num], depth + 1)

n, m = map(int, input().split())
numbers = sorted(set(map(int, input().split())))

dfs([], 0)