import sys

def solve():
    input = sys.stdin.readline
    n = int(input().strip())
    g = [input().strip() for _ in range(n)]

    ans = 0
    for i in range(n):
        two = set()
        for j in range(n):
            if i == j:
                continue
            if g[i][j] == 'Y':
                two.add(j)
            else:
                for k in range(n):
                    if g[i][k] == 'Y' and g[k][j] == 'Y':
                        two.add(j)
                        break
        ans = max(ans, len(two))

    print(ans)

if __name__ == "__main__":
    solve()