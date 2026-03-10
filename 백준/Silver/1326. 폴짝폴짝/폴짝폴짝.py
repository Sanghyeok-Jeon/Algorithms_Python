import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n = int(input().strip())
    a = [0] + list(map(int, input().split()))
    A, B = map(int, input().split())

    dist = [-1] * (n + 1)
    q = deque([A])
    dist[A] = 0

    while q:
        x = q.popleft()
        if x == B:
            break

        step = a[x]

        nx = x + step
        while nx <= n:
            if dist[nx] == -1:
                dist[nx] = dist[x] + 1
                q.append(nx)
            nx += step

        nx = x - step
        while nx >= 1:
            if dist[nx] == -1:
                dist[nx] = dist[x] + 1
                q.append(nx)
            nx -= step

    print(dist[B])

if __name__ == "__main__":
    solve()