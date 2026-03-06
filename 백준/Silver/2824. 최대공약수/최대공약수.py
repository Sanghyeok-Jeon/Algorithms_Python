import sys
import math

def solve():
    input = sys.stdin.readline
    n = int(input().strip())
    A = list(map(int, input().split()))
    m = int(input().strip())
    B = list(map(int, input().split()))

    MOD = 10**9

    ans = 1          
    big = False      
    ans_mod = 1      

    for i in range(n):
        a = A[i]
        if a == 1:
            continue

        for j in range(m):
            if a == 1:
                break
            b = B[j]
            if b == 1:
                continue

            g = math.gcd(a, b)
            if g > 1:
                # 결과에 g를 곱한다
                if not big:
                    ans *= g
                    if ans >= MOD:
                        big = True
                        ans_mod = ans % MOD
                else:
                    ans_mod = (ans_mod * (g % MOD)) % MOD

                a //= g
                B[j] //= g

    if not big:
        print(ans)
    else:
        print(f"{ans_mod:09d}")

if __name__ == "__main__":
    solve()