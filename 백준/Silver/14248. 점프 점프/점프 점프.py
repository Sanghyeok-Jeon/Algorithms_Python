import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n = int(input().strip())
    a = list(map(int, input().split()))
    s = int(input().strip()) - 1  # 0-index

    visited = [False] * n
    q = deque([s])
    visited[s] = True

    while q:
        i = q.popleft()
        jump = a[i]

        for ni in (i - jump, i + jump):
            if 0 <= ni < n and not visited[ni]:
                visited[ni] = True
                q.append(ni)

    print(sum(visited))

if __name__ == "__main__":
    solve()