# 분할 정복을 이용한 거듭제곱
def power(a, n):
    if n == 0:
        return 1

    half = power(a, n // 2)
    if n % 2:
        return (half * half * a) % MOD
    else:
        return (half * half) % MOD

MOD = 1_000_000_007

M = int(input())

answer = 0
for _ in range(M):
    N, S = map(int, input().split())
    answer += S * power(N, MOD - 2) % MOD    # 페르마의 소정리 + 모듈로 곱셈 역원

print(answer % MOD)