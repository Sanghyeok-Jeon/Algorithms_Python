import sys
input = sys.stdin.readline

def solve():
    n = int(input().strip())
    ingredients = [tuple(map(int, input().split())) for _ in range(n)]

    INF = 10**18
    ans = INF

    for mask in range(1, 1 << n):
        sour = 1
        bitter = 0
        for i in range(n):
            if mask & (1 << i):
                s, b = ingredients[i]
                sour *= s
                bitter += b
        diff = abs(sour - bitter)
        if diff < ans:
            ans = diff

    print(ans)

if __name__ == "__main__":
    solve()